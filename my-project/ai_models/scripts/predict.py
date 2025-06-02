import torch
from torchvision import transforms
from PIL import Image
import os

# Load the trained model
model = torch.load(os.path.join(os.path.dirname(__file__), '../models/model.pth'))
model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict(image_path):
    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(image)
    
    # Get the predicted class
    _, predicted = torch.max(output, 1)
    return predicted.item()

if __name__ == "__main__":
    # Example usage
    image_path = 'path_to_your_image.jpg'  # Replace with your image path
    prediction = predict(image_path)
    print(f'Predicted class: {prediction}')