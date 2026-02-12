import os
import joblib
import pandas as pd
from src.wineModel import logger
from sklearn.linear_model import ElasticNet
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

            model = ElasticNet(
                  alpha=self.config.alpha,
                  l1_ratio=self.config.l1_ration,
                  random_state=42
            )

            model.fit(x_train, y_train)

            joblib.dump(model, os.path.join(self.config.root_dir, self.config.model))
            logger.info("Model saved successfully")