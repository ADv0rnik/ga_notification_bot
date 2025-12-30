from pathlib import Path


BASE_DIR = Path(__file__).parent.resolve()
ENV_PATH = Path.joinpath(BASE_DIR, ".env")
print(ENV_PATH)
