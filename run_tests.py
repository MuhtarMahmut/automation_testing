import pytest
import sys
import os
from utilities.config_reader import ConfigReader

def run():
    # Default test target
    test_target = ConfigReader.get('DEFAULT',"testpaths")

    # If a specific test file or path is passed as argument
    if len(sys.argv) > 1:
        test_target = sys.argv[1]

    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    parallel_threads = ConfigReader.get('DEFAULT', 'parallel_threads')

    # Run pytest with desired options
    pytest_args = [
        test_target,
        "--html=reports/report.html",
        "--self-contained-html",
        "-n", parallel_threads,  # parallel execution
        "-v"
    ]

    pytest.main(pytest_args)

if __name__ == "__main__":
    run()
