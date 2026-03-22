import mlflow
from pathlib import Path


class PredictionPipeline:
      def __init__(self):
            self.model = mlflow.pyfunc.load_model(
                  "models:/Wine-Quality-Model/Production"
            )
      
      def prediction(self, data):
            prediction = self.model.predict(data)
            return prediction
      
      