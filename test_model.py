import json
import os
import sys
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "mobilenetv2_plant.pth")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "model", "class_names.json")

print("Loading class names...")
with open(CLASS_NAMES_PATH, "r") as file:
    class_names = json.load(file)
print(f"Number of classes: {len(class_names)}")

print("Creating MobileNetV2 model...")
model = models.mobilenet_v2(weights=None)
model.classifier[1] = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(model.classifier[1].in_features, len(class_names))
)

print(f"Loading trained weights from {MODEL_PATH}...")
state_dict = torch.load(MODEL_PATH, map_location="cpu", weights_only=True)
model.load_state_dict(state_dict)
model.eval()
print("Model loaded successfully!")

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])

# If an image path is provided as argument, use it; otherwise test with dummy tensor
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    image_path = sys.argv[1]
    print(f"Loading image from {image_path}...")
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)
else:
    print("Testing with random tensor...")
    input_tensor = torch.randn(1, 3, 224, 224)

print("Running prediction...")
with torch.no_grad():
    output = model(input_tensor)
    probabilities = torch.softmax(output, dim=1)[0]
    predicted_index = probabilities.argmax().item()
    confidence = probabilities[predicted_index].item() * 100

predicted_class = class_names[predicted_index]

print()
print("==============================")
print(" AGRINEXUS AI PREDICTION")
print("==============================")
print("Disease/Class :", predicted_class)
print("Confidence    :", f"{confidence:.2f}%")
print("==============================")