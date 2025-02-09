import argparse
from pathlib import Path

from src.LLMs.LLMBase import LLMBase
from src.utils.utils import open_json_from_path


class Smolvlm(LLMBase):
    def __init__(self, prompt_path: Path, image_folder_path: Path):
        self.prompt_path = prompt_path
        self.image_folder_path: image_folder_path

    def load_prompt(self) -> list[dict]:
        message = [open_json_from_path(self.prompt_path)]
        return message

    def load_images(self):
        images_paths = self.image_folder_path.rglob("*.png")
        for file_path in images_paths:
            print(file_path)

    def load_model(self):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        "This code will be used to generate OCRs from an image using Smolvlm-instruct-256M")
    parser.add_argument("-image_folder", "--i", required=True, type=Path)
    parser.add_argument("--prompt_path", "-p", required=True, type=Path)
    args = parser.parse_args()
    smolvlm = Smolvlm(args.prompt_path, args.image_folder)
    message = smolvlm.load_prompt()
    image_paths = smolvlm.load_images()
