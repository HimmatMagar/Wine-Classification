# Wine Quality Prediction

## Overview

Wine Quality Prediction is an end-to-end machine learning project that predicts the quality of wine based on its chemical properties. This project implements a Random Forest Regressor algorithm to train a model that achieves optimal performance in predicting wine quality scores.

The project includes a complete ML pipeline from data ingestion to model deployment, along with a web interface for real-time predictions.

## Problem Statement

Winemakers and consumers often need to assess wine quality without relying solely on subjective tasting. Chemical analysis provides objective data that can be used to predict quality scores. This project addresses the challenge of automating wine quality assessment by building a predictive model using physicochemical properties such as acidity, sugar content, alcohol level, and more.

The goal is to provide an accurate, data-driven method for quality prediction that can assist in:
- Quality control during production
- Consumer decision-making
- Research and development in winemaking

## Features

- **End-to-End ML Pipeline**: Complete workflow from data collection to model deployment
- **Data Validation**: Automated validation of input data against predefined schemas
- **Model Training**: Random Forest Regressor with configurable hyperparameters
- **Web API**: FastAPI-based REST API for real-time predictions
- **Interactive Web Interface**: User-friendly HTML form for inputting wine parameters
- **Modular Architecture**: Well-structured codebase with separate components for each stage
- **Logging and Monitoring**: Comprehensive logging for debugging and monitoring

## Tech Stack

- **Programming Language**: Python 3.11
- **Machine Learning**: scikit-learn (Random Forest Regressor)
- **Web Framework**: FastAPI
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Configuration**: PyYAML
- **API Server**: uvicorn
- **Version Control**: DVC (Data Version Control)
- **Experiment Tracking**: MLflow

## Installation

### Prerequisites

- Python 3.11 or higher
- conda (recommended for environment management)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Wine-Quality-Prediction
   ```

2. **Create a conda environment**:
   ```bash
   conda create -p venv python==3.11 -y
   ```

3. **Activate the environment**:
   ```bash
   conda activate venv/
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

Run the main training pipeline:
```bash
python main.py
```

This will execute the following stages:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation

### Running the Web Application

Start the FastAPI server:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:8000`

### Making Predictions

- **Via Web Interface**: Open `http://127.0.0.1:8000` in your browser and use the form to input wine parameters.
- **Via API**: Send a POST request to `/predict` with JSON data containing the wine parameters.

## Project Structure

```
Wine-Quality-Prediction/
├── app.py                          # FastAPI application for predictions
├── main.py                         # Main training pipeline
├── requirements.txt                # Python dependencies
├── setup.py                        # Package setup
├── params.yaml                     # Model hyperparameters
├── config/
│   └── config.yaml                 # Configuration file
├── schema.yaml                     # Data schema validation
├── artifacts/                      # Generated artifacts
│   ├── data_ingestion/
│   ├── data_transformation/
│   ├── data_validation/
│   ├── model_trainer/
│   └── model_evaluation/
├── research/                       # Jupyter notebooks for experimentation
├── src/
│   └── wineModel/
│       ├── components/             # Core ML components
│       ├── config/                 # Configuration management
│       ├── constants/              # File paths and constants
│       ├── entity/                 # Custom data structures
│       ├── pipeline/               # Pipeline orchestrators
│       └── utils/                  # Utility functions
├── templates/
│   └── index.html                  # Web interface template
└── README.md                       # Project documentation
```

## API Documentation

### Endpoints

#### GET /
Returns a simple welcome message.

#### GET /train
Triggers the model training pipeline.

#### POST /predict
Predicts wine quality based on input parameters.

**Request Body**:
```json
{
  "fixed_acidity": 7.0,
  "volatile_acidity": 0.3,
  "citric_acid": 0.3,
  "residual_sugar": 2.0,
  "chlorides": 0.08,
  "free_sulfur_dioxide": 15.0,
  "total_sulfur_dioxide": 50.0,
  "density": 0.995,
  "pH": 3.2,
  "sulphates": 0.5,
  "alcohol": 11.5,
  "wine_type": 1
}
```

**Response**:
```json
{
  "prediction": 6.2
}
```

## Configuration

The project uses YAML files for configuration:

- `config/config.yaml`: Defines paths and parameters for each pipeline stage
- `params.yaml`: Contains model hyperparameters
- `schema.yaml`: Defines data validation rules

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset source: Wine Quality Dataset (UCI Machine Learning Repository)
- Inspired by various ML engineering best practices
- schema.yaml: Used to store the column name of the datasets
- setup.py: Used to setup the project
- template.py: Used to make a folder structure automatically
- artificate/data_ingestion: This folder contain the data that are retrive from out sourcing
- artificate/data_transformation: This folder contain the train and test file which are prepared using feature engeneering
- artificate/data_validation: This folder contain status.txt that check the column
- artificate/model_trainer: This folder contain actual ML model
