from ultralytics import YOLO
import cv2
import argparse
from pathlib import Path

class IntrusionDetector:
    def __init__(self):
        # Load pretrained YOLOv8 model
        self.model = YOLO('yolov8n.pt')
        
        # Classes we're interested in (from COCO dataset)
        self.target_classes = {
            'person': 0,
            'cat': 15,
            'dog': 16
        }
    
    def process_image(self, image_path):
        # Read image
        img = cv2.imread(str(image_path))
        if img is None:
            raise ValueError(f"Could not read image: {image_path}")
            
        # Run detection
        results = self.model(img)[0]
        
        # Process detections
        detections = []
        for box in results.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            
            # Get class name
            class_name = results.names[class_id]
            
            if class_name in self.target_classes and confidence > 0.5:
                detections.append({
                    'class': class_name,
                    'confidence': confidence
                })
        
        return detections

def main():
    parser = argparse.ArgumentParser(description='Smart Home Intrusion Detection System')
    parser.add_argument('--input', type=str, required=True, help='Path to image or video file')
    args = parser.parse_args()
    
    detector = IntrusionDetector()
    
    try:
        detections = detector.process_image(args.input)
        
        if not detections:
            print("No intrusion detected")
        else:
            print("\nDetections found:")
            for d in detections:
                print(f"- {d['class']} (confidence: {d['confidence']:.2f})")
                
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 