import os
from src.wineModel import logger
import pandas as pd
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
            scaler = StandardScaler()
            x_scale = scaler.fit_transform(x)

            x_scaled_df = pd.DataFrame(x_scale, columns=x.columns)
            y_df = pd.DataFrame(y, columns=['quality'])

            return x_scaled_df, y_df
      
      def train_test_split(self):
            x, y = self.scaled_data()
            x_train, x_val, y_train, y_val = train_test_split(x, y, test_size = 0.25, random_state=42)

            train = pd.concat([x_train, y_train], axis=1)
            test = pd.concat([x_val, y_val], axis=1)
            
            train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info("Splitted data into train test split")
            logger.info(train.shape)
            logger.info(test.shape)