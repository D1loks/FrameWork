import pytest
import time
import logging
from datetime import datetime
from ..utils.screenshot_utils import *
from ..utils.email_utils import send_email
from ..utils.property_utils import get_property

# Логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Глобальна змінна для результатів тестів
suite_result = []


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_protocol(item, nextitem):
    """Цей хук виконуватиметься перед початком кожного тесту"""
    logger.info(f"About to begin executing test {item.nodeid}")
    item.start_time = time.time()  # Записуємо час початку тесту
    return None  # Продовжуємо виконання тесту


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Цей хук фіксує результати виконання тесту (успіх/невдача)"""
    if call.when == "call":
        if call.excinfo is None:
            # Тест пройшов успішно
            duration = time.time() - item.start_time
            result = f"\nTest {item.nodeid} has passed on {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            suite_result.append(result)
            logger.info(f"Test {item.nodeid} passed in {duration:.2f} seconds")
        else:
            # Тест не пройшов
            duration = time.time() - item.start_time
            result = f"\nTest {item.nodeid} has failed on {datetime.now().strftime('%Y-%m-%d %H:%M')}. Error: {call.excinfo[1]}"
            suite_result.append(result)
            logger.error(f"Test {item.nodeid} failed in {duration:.2f} seconds. Error: {call.excinfo[1]}")

            # Знімок екрану при невдачі
            capture_screenshot(item.nodeid)

            # Відправка email (якщо це налаштовано)
            email_enabled = get_property('email')
            if email_enabled.lower() == 'true':
                send_email(f"Test {item.nodeid} failed", result)

    return call  # Повертаємо результат виконання тесту


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Цей хук виконується після завершення сесії тестування"""
    if exitstatus == 0:
        logger.info("All tests passed.")
    else:
        logger.error("Some tests failed.")

    # Надсилаємо фінальні результати
    if get_property("email").lower() == "true":
        email_results = "\n".join(suite_result)
        send_email("Test Suite Results", email_results)


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(session, config, items):
    """Цей хук виконується перед запуском тестів"""
    for item in items:
        logger.info(f"Collecting test {item.nodeid}")

    return items


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    """Цей хук фіксує звіти про виконання тесту"""
    if report.when == "call":
        logger.info(f"Test {report.nodeid} finished with status {report.outcome}")
    return report

