from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    selenoid_login: str
    selenoid_pass: str
    selenoid_url: str

    login_author_today: str
    pass_author_today: str

    wrong_login: str
    wrong_pass: str
    base_url: str
    run_in_selenoid: bool
    android_remote_url: str
    device_name: str
    android_wait_activity: str
    apk_path: str
    use_browserstack: bool
    model_config = SettingsConfigDict(env_file='.env')

class BstackConfig(BaseSettings):
    username: str = ''
    access_key: str = ''
    platform_name: str = ''
    platform_version: str = ''
    android_remote_url: str = ''
    device_name: str = ''
    app: str = ''
    model_config = SettingsConfigDict(env_file='.env.bstack')

config = Config()
bstack_config = BstackConfig()


