from src.wineModel import logger
from src.wineModel.components.model_evaluation import ModelEvaluation
from src.wineModel.config import ConfigurationManager


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_eval = ModelEvaluation(config=model_evaluation_config)
            model_eval.test_model()
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvaluationPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e