import os
import numpy as np
import pandas as pd
from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.wineModel.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, we need to replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputField(BaseModel):
      alcohol: Annotated[float, Field(..., description="Enter the alcohol level of wine")]
      fixed_acidity: Annotated[float, Field(..., description="Enter the fixed acidity level of wine")]
      volatile_acidity: Annotated[float, Field(..., description="Enter the volatile acidity level of wine")]
      citric_acid: Annotated[float, Field(..., description="Enter the citric level of wine")]
      residual_sugar: Annotated[float, Field(..., description="Enter the residual sugar level of wine")]
      chlorides: Annotated[float, Field(..., description="Enter the chlorides level of wine")]
      free_sulfur_dioxide: Annotated[float, Field(..., description="Enter the free sulfur dioxide level of wine")]
      total_sulfur_dioxide: Annotated[float, Field(..., description="Enter the total sulfur dioxide level of wine")]
      density: Annotated[float, Field(..., description="Enter the density level of wine")]
      pH: Annotated[float, Field(..., description="Enter the pH level of wine")]
      sulphates: Annotated[float, Field(..., description="Enter the sulphates level of wine")]
      wine_type: Annotated[int, Field(..., description="Enter the wine type")]


@app.get('/')
def home():
      return "<p>This is from </p>"

@app.get('/train')
def training():
      os.system("main.py")
      return "Training successfully"

obj = PredictionPipeline()

@app.post('/predict')
def predict(input: InputField):
      input = np.array(
            [
                  [
                        input.fixed_acidity,
                        input.volatile_acidity,
                        input.citric_acid,
                        input.residual_sugar,
                        input.chlorides,
                        input.free_sulfur_dioxide,
                        input.total_sulfur_dioxide,
                        input.density,
                        input.pH,
                        input.sulphates,
                        input.alcohol,
                        input.wine_type
                  ]
            ]
      )

      prediction = obj.prediction(input)

      return JSONResponse(status_code=200, content={'prediction': float(prediction[0])})


if __name__ == "__main__":
      import uvicorn
      uvicorn.run(app, host="127.0.0.1", port=8000)
