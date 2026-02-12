import os
import yaml
import json
from pathlib import Path
from src.wineModel import logger
from box.config_box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(yaml_file_path:Path) -> ConfigBox:
      try:
            path = Path(yaml_file_path)

            with open(path, 'r') as f:
                  content = yaml.safe_load(path)
                  logger.info(f"yaml file: {yaml_file_path} is loaded successfully")
                  return ConfigBox(content)
      except BoxValueError:
            raise ValueError("yaml file is empty")
      except Exception as el:
            raise el


@ensure_annotations
def create_directory(path: Path, verbos=True):
      for path in path:
            os.makedirs(path, exist_ok=True)
            if verbos:
                  logger.info(f"Directory is created at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
      with open(path, 'w') as f:
            json.dump(data, f, indent=4)
      logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path):
      with open(path) as f:
            content = json.load(f)

      logger.info(f"json file loaded successfully from: {path}")
      return ConfigBox(content)