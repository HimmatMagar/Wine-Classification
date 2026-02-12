import os
import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.wineModel.utils import *
from src.wineModel.entity import ModelEvaluationConfig
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error


class ModelEvaluation:
      def __init__(self, config: ModelEvaluationConfig):
            self.config = config

      def eval_mertic(self, actual, pred):
            mae = mean_absolute_error(actual, pred)
            mse = mean_squared_error(actual, pred)
            r2 = r2_score(actual, pred)

            return mae, mse, r2

      def test_model(self):
            test_data = pd.read_csv(self.config.test_data)
            model = joblib.load(self.config.model_path)

            x_val = test_data.drop(columns='quality')
            y_val = test_data[['quality']]

            y_pred = model.predict(x_val)

            (mae, mse, r2) = self.eval_mertic(y_val, y_pred)

            scoring = {
                  "MAE": mae,
                  "MSE": mse,
                  'R2 score': r2
            }

            save_json(path=Path(self.config.metric_file_name), data=scoring)