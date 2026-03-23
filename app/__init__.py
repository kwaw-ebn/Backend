from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Malaria Prediction API",
    description="Backend API for malaria prediction and Nigeria map data",
    version="1.0.0"
)

origins = [
    "https://your-username.github.io",  # frontend URL
    "http://localhost:5500"             # local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
