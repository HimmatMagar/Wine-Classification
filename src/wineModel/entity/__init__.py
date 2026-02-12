from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      url: str
      local_data_file: Path
      unzip_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
      root_dir: Path
      unzip_data_file: Path
      status_file: str
      schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
      root_dir: Path
      data_file: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
      root_dir: Path
      train_data: Path
      test_data: Path
      model: str
      alpha: float
      l1_ration: float
      target_column: str