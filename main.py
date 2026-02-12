from src.wineModel import logger
from src.wineModel.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"


try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e