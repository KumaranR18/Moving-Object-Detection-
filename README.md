<h1 align="center">🚶‍♂️ Moving Object Detection 📹</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?logo=github&logoColor=white" alt="Contributions Welcome" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?logo=license&logoColor=white" alt="License" />
</div>

---

## ✨ About the Project

**Moving Object Detection** leverages **OpenCV** to detect moving objects in real-time. This lightweight solution dynamically processes video feeds to highlight objects with bounding boxes, making it ideal for applications like surveillance, safety monitoring, and activity tracking.

---

## 🛠️ Features

- 🚀 **Real-Time Object Detection**: Accurate and instantaneous movement tracking.
- 🎨 **Preprocessed Frames**: Uses Gaussian Blur for smooth image processing.
- ✅ **Adjustable Sensitivity**: Fine-tune detection sensitivity to suit your needs.
- 📷 **Efficient**: Optimized to work with most cameras seamlessly.

---

## 🌟 Benefits

- 🔍 **Enhanced Security**: Monitor and secure your surroundings effectively.
- ⚡ **Fast Processing**: Handles live feeds with minimal latency.
- 🎯 **Customizable**: Easy to modify parameters for specific use cases.

---

## 🔍 Use Cases

- 🏠 **Home Security**: Detect intruders or unauthorized movements.
- 🏢 **Workplace Safety**: Monitor restricted zones for compliance.
- 🌳 **Wildlife Observation**: Track animal movements in natural environments.
- 🏗️ **Construction Sites**: Ensure safety by observing ongoing activity.

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KumaranR18/Moving-Object-Detection.git
   cd Moving Object Detection
   ```
2. **Install dependencies:**
```bash
pip install opencv-python imutils
```
3. **Run the script:**
```bash
python Moving Object Detection.py
```
## 💻 Usage
1. Open the script and grant camera access.
2. Observe real-time movement detection with bounding boxes and updates.
3. Press **`q`** to exit the application.

---

## 🧠 How It Works
1. Captures the first frame from the video stream as the reference frame.
2. Converts the video feed to grayscale and applies Gaussian Blur for noise reduction.
3. Calculates the frame difference and thresholds the result.
4. Detects and processes contours, drawing bounding boxes around moving objects.

---

## 🤝 Contributions Welcome! 🌟
We love contributions!

- Fork this repository, make your changes, and submit a pull request.
- Found a bug or have an idea? Open an issue [here](https://github.com/KumaranR18/Moving-Object-Detection/issues).

Let’s build something amazing together!

---

## 📝 License
This project is licensed under the MIT License. See the License file for details.

