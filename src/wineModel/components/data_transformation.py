import os
import joblib
import pandas as pd
from src.wineModel import logger
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from src.wineModel.entity import DataTransformationConfig


class DataTransformation:
      def __init__(self, config: DataTransformationConfig):
            self.config = config

      
      def scaled_data(self):
            df = pd.read_csv(self.config.data_file)

            x = df.drop(columns="quality")
            y = df['quality']

            x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.25, random_state=42)

            scaler = StandardScaler()
            x_train_scale = scaler.fit_transform(x_train)
            x_val_scale = scaler.transform(x_val)

            joblib.dump(x_train_scale, os.path.join(self.config.root_dir, 'x_train.pkl'))
            joblib.dump(x_val_scale, os.path.join(self.config.root_dir, 'x_val.pkl'))
            joblib.dump(y_train, os.path.join(self.config.root_dir, 'y_train.pkl'))
            joblib.dump(y_val, os.path.join(self.config.root_dir, 'y_val.pkl'))

            logger.info("Splitted data into train test split")