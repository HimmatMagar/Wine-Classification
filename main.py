from src.wineModel import logger
from src.wineModel.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wineModel.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"


try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataIngestionTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Data Validation stage"
try:
      logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
      obj = DataValidationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
except Exception as e:
      logger.exception(e)
      raise e