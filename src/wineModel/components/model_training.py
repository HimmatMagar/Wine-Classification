import os
import joblib
import mlflow
import pandas as pd
from pathlib import Path
from src.wineModel import logger
from src.wineModel.utils import *
from sklearn.ensemble import RandomForestRegressor
from src.wineModel.entity import ModelTrainingConfig

class ModelTrainig:
      def __init__(self, config: ModelTrainingConfig):
            self.config = config
      
      def model_train(self):
            x_train = load_file(Path(self.config.train_data))
            y_train = load_file(Path(self.config.test_data))

            model = RandomForestRegressor(
                  n_estimators = self.config.n_estimators,
                  min_samples_split = self.config.min_samples_split,
                  min_samples_leaf = self.config.min_samples_leaf,
                  max_features = self.config.max_features
            )

            model.fit(x_train, y_train)

            mlflow.set_experiment("Wine quality model")
            mlflow.set_tracking_uri("http://127.0.0.1:5000/")

            with mlflow.start_run(run_name="RandomF-Model"):
                  mlflow.log_params({
                        "n_estimators": self.config.n_estimators,
                        "min_samples_split": self.config.min_samples_split,
                        "min_samples_leaf": self.config.min_samples_leaf,
                        "max_features": self.config.max_features
                  })
                  
                  mlflow.sklearn.log_model(model, "model")
            
            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model))
            logger.info("Model saved & logged to MLflow")