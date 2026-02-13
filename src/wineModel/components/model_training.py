import os
import joblib
import pandas as pd
from src.wineModel import logger
from sklearn.ensemble import RandomForestRegressor
from src.wineModel.entity import ModelTrainingConfig

class ModelTrainig:
      def __init__(self, config: ModelTrainingConfig):
            self.config = config
      
      def model_train(self):
            train_data = pd.read_csv(self.config.train_data)
            test_data = pd.read_csv(self.config.test_data)

            x_train = train_data.drop(columns='quality')
            x_val = test_data.drop(columns='quality')
            y_train = train_data[['quality']]
            y_val = test_data[['quality']]

            model = RandomForestRegressor(
                  n_estimators = self.config.n_estimators,
                  min_samples_split = self.config.min_samples_split,
                  min_samples_leaf = self.config.min_samples_leaf,
                  max_features = self.config.max_features
            )

            model.fit(x_train, y_train)

            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model))
            logger.info("Model saved successfully")