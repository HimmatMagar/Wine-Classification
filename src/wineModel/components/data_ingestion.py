import os
import zipfile
import urllib.request as r
from src.wineModel import logger
from src.wineModel.entity.configuration import DataIngestionConfig


class DataIngestion:
      def __init__(self, config: DataIngestionConfig):
            self.config = config

      def download_file(self):
            if not os.path.exists(self.config.local_data_file):
                  filename, header = r.urlretrieve(
                        url = self.config.url,
                        filename = self.config.local_data_file
                  )
                  logger.info(f"{filename} download with following info: \n{header}")
            else:
                  logger.info("File is already exist")
      
      
      def extract_zip_file(self):
            unzip_file = self.config.unzip_file
            os.makedirs(unzip_file, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as f:
                  f.extractall(unzip_file)