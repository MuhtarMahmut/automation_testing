import pytest
import sys
import os
from utilities.config_reader import ConfigReader


SPECIFIC_TEST_FILE = None  # fileName.py or None
SPECIFIC_TEST = "borrow_books_test.py::test_borrow_books_link"  # fileName.py::testFunctionName or None
TAG = None  # tagName or None
WORKERS = 1  # 1 or greater number
RETRIES = 0  # 0 or greater number


def run():
    os.makedirs("reports", exist_ok=True)

    test_target = f"./{ConfigReader.get_pytest('pytest','testpaths')}"

    if SPECIFIC_TEST and SPECIFIC_TEST_FILE:
        raise RuntimeError("Invalid Test(s) Path selected")
    elif SPECIFIC_TEST_FILE:
        test_target += f"/{SPECIFIC_TEST_FILE}"
    elif SPECIFIC_TEST:
        test_target += f"/{SPECIFIC_TEST}"

    if len(sys.argv) > 1:
        test_target = sys.argv[1]

    pytest_args = [
        test_target,
        "--html=reports/report.html",
        "--self-contained-html",
        "-n", str(WORKERS),
        "-v",
        "--reruns", str(RETRIES)
    ]

    if TAG:
        pytest_args += ["-m", TAG]

    # Run pytest
    pytest.main(pytest_args)


if __name__ == "__main__":
    run()
