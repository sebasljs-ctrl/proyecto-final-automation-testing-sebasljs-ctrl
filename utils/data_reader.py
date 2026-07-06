import json
from pathlib import Path

from utils.config import DATA_DIR


def read_json(filename):
    file_path = Path(DATA_DIR) / filename
    with file_path.open(encoding="utf-8") as file:
        return json.load(file)

