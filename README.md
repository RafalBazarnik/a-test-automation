# a-test-automation

Simple, extendable test automation framework using Python, Playwright (async), pytest, requests, dotenv, and deepeval.

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

### AI testing env vars

For AI tests, configure your `.env.<env>` file with:

```dotenv
CHATBOT_API_URL=https://your-api/chat
CHATBOT_API_KEY=your-api-key
CHATBOT_API_KEY_HEADER=Authorization
CHATBOT_API_KEY_PREFIX=Bearer
CHATBOT_SYSTEM_PROMPT_FIELD=system_prompt
CHATBOT_QUESTION_FIELD=question
CHATBOT_ANSWER_FIELD=answer
SYSTEM_PROMPT=You are a helpful assistant.
OPENAI_API_KEY=your-openai-key-for-deepeval-judge
```

`SYSTEM_PROMPT` can be overridden at runtime with `--system-prompt`.

## Running tests

### Standard suites

```bash
pytest --env dev --browser chromium
pytest --env test --browser webkit --headless
```

### AI suites (deepeval)

```bash
# all AI tests
pytest --env dev -m ai

# safety only (toxicity + jailbreak checks)
pytest --env dev -m safety

# smoke AI checks
pytest --env dev -m "ai and smoke"
```

### Run a single test

```bash
pytest --env dev tests/ai/test_safety.py::test_jailbreak_resistance
```

### Run tests in parallel

```bash
# auto worker count
pytest --env dev -n auto

# parallel AI smoke suite
pytest --env dev -n 4 -m "ai and smoke"
```

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
│       ├── ai_client.py
│       ├── config.py
│       └── pages
│           └── login_page.py
├── tests
│   ├── ai
│   ├── api
│   └── ui
└── .env.dev
```
