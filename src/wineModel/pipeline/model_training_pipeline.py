import mlflow
from wineModel import logger
from wineModel.config import ConfigurationManager
from wineModel.utils.mlflow_config import configure_mlflow, save_run_id
from wineModel.components.model_training import ModelTrainig


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()

            configure_mlflow(experiment_name="Wine-Quality-Prediction")

            with mlflow.start_run(run_name="wine-model") as run:
                  try:
                        mlflow.log_params({
                              "n_estimators": model_training_config.n_estimators,
                              "min_samples_split": model_training_config.min_samples_split,
                              "min_samples_leaf": model_training_config.min_samples_leaf,
                              "max_features": model_training_config.max_features
                        })
                        wine_model = ModelTrainig(config=model_training_config)
                        model = wine_model.model_train()

                        logged_model = mlflow.sklearn.log_model(
                              sk_model=model,
                              name="model"
                        )
                        logger.info("Model logged successfully")

                        with open("artifacts/model_id.txt", 'w') as f:
                              f.write(logged_model.model_id)
                        logger.info("Model id saved in artifacts/model_id.txt")

                        save_run_id(run.info.run_id)
                        logger.info("Run id saved successfully")
                  except Exception as e:
                        raise e
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = ModelTrainingPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e