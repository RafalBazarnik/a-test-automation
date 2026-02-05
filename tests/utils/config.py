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


def get_settings(env_name: str) -> Settings:
    load_env(env_name)
    return Settings(
        ui_base_url=os.getenv("UI_BASE_URL", ""),
        api_base_url=os.getenv("API_BASE_URL", ""),
        login_user=os.getenv("LOGIN_USER", ""),
        login_password=os.getenv("LOGIN_PASSWORD", ""),
    )
