import mlflow
from wineModel import logger
from wineModel.config import ConfigurationManager
from wineModel.utils.mlflow_config import configure_mlflow, load_run_id
from wineModel.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()

            configure_mlflow("Wine-Quality-Prediction")
            run_id = load_run_id()

            try:
                  with open("artifacts/model_id.txt", 'r') as f:
                        model_id = f.read()
            except FileNotFoundError as e:
                  raise e

            with mlflow.start_run(run_id=run_id):
                  model_eval = ModelEvaluation(config=model_evaluation_config)
                  evaluation = model_eval.test_model()

                  mlflow.log_metrics({
                        "Mean Absolute Error": evaluation['MAE'],
                        "Mean Squared Error": evaluation['MSE'],
                        "R2 score": evaluation['R2_score']
                  })

                  # if evaluation['MAE'] <= 0.5 and evaluation['MSE'] <= 0.3 and evaluation['R2_score'] >= 0.85:
                  model = mlflow.register_model(
                        model_uri = f"models:/{model_id}",
                        name="Wine-Quality-Model"
                  )
                  logger.info("Model register successfully in model registry")

                  client = mlflow.tracking.MlflowClient()
                  client.transition_model_version_stage(
                        name="Wine-Quality-Model",
                        version=model.version,
                        stage="Staging"
                  )
                  # else:
                  #       logger.warning("failed to register the model into model registry")

            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelEvaluationPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e