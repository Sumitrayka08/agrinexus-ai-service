import json
import os
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
from io import BytesIO
from utils.remedies import get_remedy

class DiseaseClassifierService:
    def __init__(self, model_path: str, class_names_path: str):
        self.device = torch.device("cpu")
        self.model_path = model_path
        self.class_names_path = class_names_path
        self.class_names = []
        self.model = None
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                [0.485, 0.456, 0.406],
                [0.229, 0.224, 0.225]
            )
        ])

    def load_model(self):
        print(f"Loading class names from {self.class_names_path}...")
        with open(self.class_names_path, "r") as f:
            self.class_names = json.load(f)

        print(f"Initializing MobileNetV2 architecture for {len(self.class_names)} classes...")
        self.model = models.mobilenet_v2(weights=None)
        self.model.classifier[1] = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(self.model.classifier[1].in_features, len(self.class_names))
        )

        print(f"Loading trained weights from {self.model_path}...")
        state_dict = torch.load(self.model_path, map_location=self.device, weights_only=True)
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)
        self.model.eval()
        print("MobileNetV2 Plant Disease Classifier loaded successfully!")

    def predict(self, image_bytes: bytes) -> dict:
        if self.model is None:
            raise RuntimeError("Model is not initialized")

        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.softmax(outputs, dim=1)[0]
            predicted_index = probabilities.argmax().item()
            confidence = float(probabilities[predicted_index].item() * 100)

        disease_name = self.class_names[predicted_index]
        remedy = get_remedy(disease_name)

        return {
            "disease": disease_name,
            "confidence": round(confidence, 2),
            "recommendation": remedy
        }

