# Green Blob Detection System 🎯

A computer vision system for detecting green blobs in images using OpenCV. The project includes both a main detection script and an interactive parameter tuning tool.

## Features ✨
- Green blob detection using HSV color space
- Noise reduction using morphological operations
- Interactive parameter tuning interface
- Real-time visualization of detection results

## Requirements 📋
- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation 🚀
```bash
pip install opencv-python numpy
```

## Usage 🛠️

### Main Detection Script
```bash
python blob_detection.py
```
The script will:
1. Load and process the input image
2. Convert to HSV color space
3. Apply color thresholding
4. Perform noise reduction
5. Detect blobs
6. Display results with detected blobs marked in red

### Parameter Tuning Tool
```bash
python tuning_script.py
```
Use the interactive interface to:
- Adjust HSV thresholds in real-time
- Fine-tune detection parameters
- View immediate results
- Press 'q' to quit

## Parameters ⚙️

### HSV Thresholds
- H: 48-82 (Hue range for green)
- S: 12-255 (Saturation range)
- V: 0-255 (Value range)

### Blob Detection Parameters
- Filter by area: Disabled
- Filter by circularity: Disabled
- Filter by convexity: Disabled
- Filter by inertia: Disabled
- Filter by color: Enabled
- Blob color: 255 (white)

## Output 📊
- Original image with detected blobs marked in red
- Console output of blob coordinates
- Interactive mask visualization

## Notes 📝
- Input image should be named "TestImage.png"
- HSV values can be fine-tuned using the tuning script
- Morphological operations help reduce noise and fill holes

## Project Structure 📁
```
.
├── blob_detection.py    # Main detection script
├── tuning_script.py     # Interactive parameter tuning tool
├── TestImage.png        # Sample input image
└── README.md           # This file
```
