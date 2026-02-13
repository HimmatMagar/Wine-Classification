# Wine-Quality
###### Wine Quality is an end-to-end machine learning project that predicts wine quality based on their chemical properties. In this project, I implemented the Elastic Net algorithm to train the model, achieving a balance between Ridge and Lasso regression techniques for optimal performance.


### Project workflows
1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py


## How to run?
### Steps:

#### To make a conva environment
```bash
conda create -p venv python==3.11 -y
```

#### To activate conda environment
```bash
conda activate venv/
```

#### installing requirement
```bash
pip install -r requirements.txt
```


### Project Components
- artifacts: This folder is used for the data which are retrive from outsource like database, github
- config: This folder is used for the configuration for data ingestion, data validation
- research: This folder is used for research before writing moduler coding
- src/components: This folder is used to write a main logic for data ingestion, data validation
- src/config: This folder is used to configure the filepath for the data ingestion, data validation
- src/constants: Used for the filepath
- src/entity: Used to makea custom return type
- src/pipeline: Used to make a pipeline
- src/utils: Used to make a commonly used function like file loading
- src/constructor: Used to write a logs related file
- tempalte: Used for forntend
- main: Main end point for the pipeline
- app: Used to write a api
- Paras.yaml: Used to store the Model parameter
- schema.yaml: Used to store the column name of the datasets
- setup.py: Used to setup the project
- template.py: Used to make a folder structure automatically
- artificate/data_ingestion: This folder contain the data that are retrive from out sourcing
- artificate/data_transformation: This folder contain the train and test file which are prepared using feature engeneering
- artificate/data_validation: This folder contain status.txt that check the column
- artificate/model_trainer: This folder contain actual ML model