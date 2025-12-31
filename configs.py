from pathlib import Path


BASE_DIR = Path(__file__).parent.resolve()
ENV_PATH = Path.joinpath(BASE_DIR, ".env")
BASE_URL = "https://api.telegram.org/"
