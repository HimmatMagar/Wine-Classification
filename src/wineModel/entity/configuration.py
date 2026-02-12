from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      url: str
      local_data_file: Path
      unzip_file: Path