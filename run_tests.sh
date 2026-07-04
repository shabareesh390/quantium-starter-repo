#!/bin/bash
# Task 6: Automate Your Test Suite
#
# Activates the project's virtual environment, runs the test suite,
# and exits with 0 if all tests passed, or 1 otherwise.

# Activate the virtual environment (Windows-style venv layout)
source venv/Scripts/activate

# Run the test suite
pytest test_app.py

# Capture pytest's exit code
TEST_EXIT_CODE=$?

# Return 0 if tests passed, 1 otherwise
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi