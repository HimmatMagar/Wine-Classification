from wineModel import logger
from wineModel.components.model_training import ModelTrainig
from wineModel.config import ConfigurationManager


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()
            model = ModelTrainig(config=model_training_config)
            model.model_train()
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelTrainingPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e