from dataclasses import dataclass
import os
from dotenv import load_dotenv


def load_env(env_name: str) -> None:
    env_file = f".env.{env_name}"
    load_dotenv(env_file, override=False)


@dataclass(frozen=True)
class Settings:
    ui_base_url: str
    api_base_url: str
    login_user: str
    login_password: str
    chatbot_api_url: str
    chatbot_api_key: str
    chatbot_api_key_header: str
    chatbot_api_key_prefix: str
    chatbot_system_prompt_field: str
    chatbot_question_field: str
    chatbot_answer_field: str


def get_settings(env_name: str) -> Settings:
    load_env(env_name)
    return Settings(
        ui_base_url=os.getenv("UI_BASE_URL", ""),
        api_base_url=os.getenv("API_BASE_URL", ""),
        login_user=os.getenv("LOGIN_USER", ""),
        login_password=os.getenv("LOGIN_PASSWORD", ""),
        chatbot_api_url=os.getenv("CHATBOT_API_URL", ""),
        chatbot_api_key=os.getenv("CHATBOT_API_KEY", ""),
        chatbot_api_key_header=os.getenv("CHATBOT_API_KEY_HEADER", "Authorization"),
        chatbot_api_key_prefix=os.getenv("CHATBOT_API_KEY_PREFIX", "Bearer"),
        chatbot_system_prompt_field=os.getenv("CHATBOT_SYSTEM_PROMPT_FIELD", "system_prompt"),
        chatbot_question_field=os.getenv("CHATBOT_QUESTION_FIELD", "question"),
        chatbot_answer_field=os.getenv("CHATBOT_ANSWER_FIELD", "answer"),
    )
