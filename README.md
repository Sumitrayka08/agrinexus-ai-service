# AgriNexus AI - Plant Disease Classification Microservice 🌿🤖

PyTorch MobileNetV2 computer vision microservice built with FastAPI for plant pathology and crop leaf disease detection.

## 🚀 API Endpoints

- `GET /` - Root status check
- `GET /health` - Microservice health status, device info, and class count
- `POST /predict` - Accepts multipart form data with image file (`file`) and returns predicted disease, confidence percentage, and remedy recommendations.

## 🏗️ Model Details
- **Architecture**: MobileNetV2 fine-tuned on 38 plant disease classes
- **Weights File**: `model/mobilenetv2_plant.pth` (8.9 MB)
- **Input Resolution**: 224x224 RGB
- **Inference Runtime**: CPU (Torch & Torchvision)

## ☁️ Deployment on Render

1. Create a new **Web Service** on Render connected to this repository.
2. Configure settings:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
3. Once deployed, configure the base URL in your Spring Boot backend's `AI_SERVICE_URL` environment variable.
