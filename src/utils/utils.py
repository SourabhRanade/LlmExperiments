import json
from pathlib import Path


def open_json_from_path(json_file_path: Path) -> dict:
    with open(json_file_path) as f:
        content = json.load(f)
    return content
