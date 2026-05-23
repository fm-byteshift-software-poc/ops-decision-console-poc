from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "ops-decision-console-poc"
    app_env: str = "development"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000

    hf_api_token: str
    hf_model_id: str = "meta-llama/Llama-3.1-8B-Instruct:cerebras"
    hf_base_url: str = "https://router.huggingface.co/v1"

    database_url: str = "sqlite:///:memory:"


settings = Settings()