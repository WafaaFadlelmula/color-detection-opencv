# Multi-Color Detection with OpenCV

This project demonstrates real-time **color detection** using OpenCV. It captures video from your webcam and detects the colors **Red**, **Yellow**, **Green**, and **Blue**. When a color is detected, a **bounding box** is drawn around the object, and the color name is displayed.

## Prerequisites

Before running the project, you need to have the following installed:

- Python 3.x
- OpenCV (`opencv-python` package)
- PIL (Pillow) library

You can install the necessary dependencies using `pip`:

```bash
pip install opencv-python pillow numpy
```

# How to Run the Code 
1. Clone this repository or copy the code into a Python file (e.g., color_detection.py).
2. Run the Python file in your terminal or IDE:
```bash
python color_detection.py
```

3. The program will open your webcam feed and start detecting the colors Red, Yellow, Green, and Blue.

4. When a color is detected, it will display a bounding box around the detected area and show the color name above it.

5. To stop the program, press 'q'.

# How It Works
- Color Detection: The code converts the captured frames from BGR to HSV color space using cv2.cvtColor(). In HSV, it's easier to isolate specific colors.

- HSV Color Thresholding: Using cv2.inRange(), the program generates a mask for the target color based on its HSV range.

- Bounding Boxes and Text: When a color is detected, the program draws a bounding box around the detected region and adds a label showing the color name.

# Supported Colors
The program currently supports the following colors:
- **Red**
- **Yellow**
- **Green**
- **Blue**

# Project Structure
color-detection/ │ ├── color_detection.py # Main code for color detection ├── utils.py # Helper functions for color limit calculations └── README.md # This README file

# Customization and Extension

You can customize and extend the project in the following ways:

- **Add More Colors**: To detect additional colors, you can define their HSV ranges in the `get_color_limits()` function in `utils.py`.
- **Change Detection Logic**: Modify the color detection logic to suit your requirements, such as detecting shapes or patterns.
- **Improve Accuracy**: Experiment with different color ranges and thresholds to improve the detection accuracy.
