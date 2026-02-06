from __future__ import annotations

from dataclasses import dataclass

import requests


@dataclass(frozen=True)
class ChatbotClientConfig:
    endpoint: str
    api_key: str
    api_key_header: str = "Authorization"
    api_key_prefix: str = "Bearer"
    system_prompt_field: str = "system_prompt"
    question_field: str = "question"
    answer_field: str = "answer"


class ChatbotClient:
    def __init__(self, config: ChatbotClientConfig) -> None:
        self._config = config

    def ask(self, system_prompt: str, question: str, timeout: int = 30) -> str:
        headers = {"Content-Type": "application/json"}
        if self._config.api_key:
            key_value = self._config.api_key
            if self._config.api_key_prefix:
                key_value = f"{self._config.api_key_prefix} {key_value}".strip()
            headers[self._config.api_key_header] = key_value

        payload = {
            self._config.system_prompt_field: system_prompt,
            self._config.question_field: question,
        }

        response = requests.post(
            self._config.endpoint,
            json=payload,
            headers=headers,
            timeout=timeout,
        )
        response.raise_for_status()
        data = response.json()
        answer = data.get(self._config.answer_field, "")
        if not isinstance(answer, str):
            raise ValueError(
                f"Expected string in response field '{self._config.answer_field}', got {type(answer)!r}",
            )
        return answer
