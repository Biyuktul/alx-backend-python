# 0x03-Unittests_and_integration_tests

This directory contains Python code and tests focused on **unit testing** and **integration testing** for a GitHub organization client. The project demonstrates best practices for testing Python code, including the use of mocks, parameterized tests, and pycodestyle compliance.

## Contents

- **client.py**:  
  Implementation of `GithubOrgClient`, a client for fetching organization and repository data from the GitHub API.

- **utils.py**:  
  Utility functions and decorators, including:
  - `access_nested_map`: Safely access nested dictionary values.
  - `get_json`: Fetch JSON data from a URL.
  - `memoize`: Decorator for caching method results.

- **fixtures.py**:  
  Contains test payloads and fixtures used for integration and unit tests.

- **test_utils.py**:  
  Unit tests for the utility functions in `utils.py`, using `unittest` and `parameterized`.

- **test_client.py**:  
  Unit and integration tests for `GithubOrgClient`:
  - Uses `unittest`, `parameterized`, and `unittest.mock` for mocking and parameterization.
  - Demonstrates how to mock external API calls and test both public and license-filtered repository listings.
  - Shows how to use `@parameterized_class` for integration tests with different fixtures.

## Key Concepts Covered

- **Unit Testing**:  
  Writing isolated tests for functions and methods, using mocks to avoid real network calls.

- **Integration Testing**:  
  Testing how components work together, with only external dependencies (like HTTP requests) mocked.

- **Mocking**:  
  Using `unittest.mock.patch` and `PropertyMock` to replace functions and properties during tests.

- **Parameterized Testing**:  
  Using `@parameterized.expand` and `@parameterized_class` to run tests with multiple sets of inputs.

- **PyCodeStyle Compliance**:  
  Ensuring all code follows Python's style guidelines (PEP8), especially line length and spacing.

## How to Run Tests

From this directory, run:
```bash
python3 -m unittest test_utils.py
python3 -m unittest test_client.py
```
