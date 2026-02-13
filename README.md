# a-test-automation

Simple, extendable test automation framework using Python, Playwright (async), pytest, requests, and dotenv. Includes sample UI, API, and performance (Locust) tests, plus Bitbucket Pipelines and Allure reporting.

## Prerequisites

- Python 3.12+
- Playwright browsers installed (`python -m playwright install`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m playwright install
```

## Environment configuration

Use `.env.dev`, `.env.test`, or `.env.preprod` to configure targets. Default is `dev`.

```bash
pytest --env dev
```

## Running tests

```bash
pytest --env dev --browser chromium
pytest --env test --browser webkit --headless
```

## Running API performance tests (Locust)

```bash
# CLI / headless
API_BASE_URL=https://jsonplaceholder.typicode.com \
locust -f tests/performance/locustfile.py --headless -u 10 -r 2 -t 1m

# Web UI
API_BASE_URL=https://jsonplaceholder.typicode.com \
locust -f tests/performance/locustfile.py
```

Notes:
- `LOCUST_HOST` has priority over `API_BASE_URL` when both are provided.
- Default host is `https://jsonplaceholder.typicode.com`.

## Allure reports

```bash
pytest --env dev --browser chromium --alluredir=allure-results
allure serve allure-results
```

## Project layout

```
.
├── bitbucket-pipelines.yml
├── pyproject.toml
├── src
│   └── a_test_automation
│       ├── config.py
│       └── pages
│           └── login_page.py
├── tests
│   ├── api
│   ├── performance
│   │   └── locustfile.py
│   └── ui
└── .env.dev
```
