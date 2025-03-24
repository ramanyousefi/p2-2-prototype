# AI-Powered Smart Home Intrusion Detection

A prototype for an AI-powered intrusion detection system using YOLOv8 object detection. This prototype demonstrates the core functionality of detecting humans and pets in images/videos.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Unix/MacOS
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the detector on an image:
   ```bash
   python intrusion_detector.py --input path/to/image.jpg
   ```

The detector will:
- Load a pretrained YOLOv8 model
- Detect humans, cats and dogs in the image
- Report any detections with confidence scores

## Features

- Uses YOLOv8 pretrained model for fast and accurate detection
- Focuses on relevant classes (humans, cats, dogs) 
- Configurable confidence threshold (default 0.5)
- Simple command line interface

## Project Structure

```
.
├── README.md
├── requirements.txt
├── intrusion_detector.py
└── venv/
```

## Test Dataset

For testing, we use the [Human Detection Dataset](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset) from Kaggle. This dataset provides a variety of images for testing human detection capabilities.

## Next Steps
- Add video processing support
- Implement real-time visualization
- Add false alarm analysis
- Add detection threshold configuration
- Add statistics collection 