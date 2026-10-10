import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.inference_service import DiseaseClassifierService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "mobilenetv2_plant.pth")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "model", "class_names.json")

classifier_service = DiseaseClassifierService(MODEL_PATH, CLASS_NAMES_PATH)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load PyTorch model once on startup
    print("Starting up AgriNexus AI Fast microservice...")
    classifier_service.load_model()
    yield
    print("Shutting down AgriNexus AI Service...")

app = FastAPI(
    title="AgriNexus AI Crop Disease Analysis Microservice",
    description="PyTorch MobileNetV2 Disease Classification API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AgriNexus AI Disease Classifier Service is active"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model": "MobileNetV2",
        "device": "cpu",
        "supported_classes": len(classifier_service.class_names)
    }

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File uploaded must be an image (JPEG/PNG)")
    
    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")
    
    try:
        result = classifier_service.predict(contents)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")