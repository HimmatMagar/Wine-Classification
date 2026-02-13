from src.wineModel.utils import *
from src.wineModel.constants import *
from src.wineModel.entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainingConfig, ModelEvaluationConfig

class ConfigurationManager:
      def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH
      ):
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)

            create_directory([self.config.artifacts_root])
            
      
      def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.data_ingestion

            create_directory([config.root_dir])
            
            data_ingestion_config = DataIngestionConfig(
                  root_dir=config.root_dir,
                  url = config.source_url,
                  local_data_file = config.local_data_file,
                  unzip_file=config.unzip_dir
            )
            return data_ingestion_config
      
      
      def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            schema = self.schema.COLUMNS

            create_directory([config.root_dir])

            get_data_validation = DataValidationConfig(
                  root_dir=config.root_dir,
                  unzip_data_file=config.unzip_data_dir,
                  status_file=config.STATUS_FILE,
                  schema=schema
            )
            return get_data_validation
      
      
      def get_data_transformation_config(self) -> DataTransformationConfig:
            config = self.config.data_transformation

            create_directory([config.root_dir])

            get_data_transformation = DataTransformationConfig(
                  root_dir=config.root_dir,
                  data_file=config.data_file,
            )

            return get_data_transformation
      

      def get_model_training_config(self) -> ModelTrainingConfig:
            config = self.config.model_trainer
            params = self.params.RandomForest
            schema = self.schema.TARGET_COLUMN

            create_directory([config.root_dir])

            model_train_config = ModelTrainingConfig(
                  root_dir = config.root_dir,
                  train_data = config.train_data,
                  test_data = config.test_data,
                  model = config.model,
                  n_estimators = params.n_estimators,
                  min_samples_split = params.min_samples_split,
                  min_samples_leaf = params.min_samples_leaf,
                  max_features = params.max_features,
                  target_column = schema.name
            )
            return model_train_config
      

      def get_model_evaluation_config(self) -> ModelEvaluationConfig:
            config = self.config.model_evaluation
            params = self.params.RandomForest
            schema = self.schema.TARGET_COLUMN

            create_directory([config.root_dir])

            model_eval = ModelEvaluationConfig(
                  root_dir = config.root_dir,
                  test_data = config.test_data,
                  model_path = config.model_path,
                  all_params = params,
                  metric_file_name = config.metric_file_name,
                  target_column = schema.name
            )

            return model_eval