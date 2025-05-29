from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    selenoid_login: str
    selenoid_pass: str
    selenoid_url: str

    login_author_today: str
    pass_author_today: str

    wrong_login: str
    wrong_pass: str

    model_config = SettingsConfigDict(env_file='.env')

config = Config()


