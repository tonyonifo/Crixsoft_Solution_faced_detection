# 👁️ FaceAI CLI

> **A lightweight, single-file AI face detection CLI for Python and Termux.**

FaceAI CLI is a minimal command-line application that performs face detection on images, videos, or a live webcam using OpenCV. Designed as a **single Python script**, it is easy to copy, modify, and run on desktops, Linux servers, Raspberry Pi, and Android devices using Termux.

---

## ✨ Features

- 📷 Detect faces in images
- 🎥 Detect faces in video files
- 📹 Real-time webcam detection
- 🖥️ Simple Typer-powered CLI
- 📱 Termux compatible
- 📦 Single-file architecture
- ⚡ Lightweight and portable
- 🛠️ Easy to extend

---

# Screenshot

> *(Coming Soon)*

---

# Project Structure

```text
.
├── faceai.py
└── README.md
```

Everything lives inside one Python file.

---

# Requirements

- Python 3.10+
- OpenCV
- Typer
- Rich (optional)

---

# Installation

## Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate

pip install typer rich opencv-python
```

## Windows

```powershell
python -m venv .venv

.venv\Scripts\activate

pip install typer rich opencv-python
```

## Termux

```bash
pkg update
pkg upgrade

pkg install python

pip install --upgrade pip

pip install typer rich opencv-python
```

---

# Running

Display help

```bash
python faceai.py --help
```

---

## Detect Faces in an Image

```bash
python faceai.py detect-image image.jpg
```

Example output

```text
Found 3 face(s).
Result saved to output.jpg
```

---

## Detect Faces in a Video

```bash
python faceai.py detect-video movie.mp4
```

Press **Q** to quit.

---

## Detect Faces from Webcam

```bash
python faceai.py detect-webcam
```

Press **Q** to exit.

---

# Detection Pipeline

```
Input
   │
   ▼
Load Image / Video
   │
   ▼
Convert to Grayscale
   │
   ▼
Haar Cascade Detection
   │
   ▼
Draw Bounding Boxes
   │
   ▼
Save / Display Result
```

---

# Current Detection Engine

The current version uses OpenCV's built-in **Haar Cascade** detector.

### Advantages

- Fast
- Lightweight
- Offline
- No model downloads
- Excellent for learning

### Limitations

- Sensitive to lighting
- Poor profile-face detection
- Limited rotation support
- Lower accuracy than modern deep learning models

---

# Planned AI Backends

Future releases may support:

- SCRFD
- RetinaFace
- YuNet
- BlazeFace
- MediaPipe
- ONNX Runtime
- TensorRT
- OpenVINO

---

# Roadmap

## Version 1

- ✅ Image detection
- ✅ Video detection
- ✅ Webcam detection

## Version 2

- Face embeddings
- Face recognition
- Confidence thresholds
- JSON output
- CSV export
- Batch processing

## Version 3

- GPU acceleration
- Folder scanning
- Recursive search
- Face tracking
- Similarity search
- Duplicate detection

## Version 4

- Celebrity recognition
- Emotion detection
- Age estimation
- Gender estimation
- Face clustering
- Face quality scoring
- REST API
- Docker support

---

# Example Commands

```bash
python faceai.py detect-image family.jpg

python faceai.py detect-video wedding.mp4

python faceai.py detect-webcam
```

---

# Current Limitations

- Haar Cascade detector
- No GPU acceleration
- No face recognition
- No embeddings
- No identity matching
- No tracking
- No batch mode
- No API
- No reports

---

# Future Enterprise Features

- REST API
- Docker image
- GitHub Actions
- Automated tests
- Plugin architecture
- AI model manager
- ONNX Runtime
- CUDA support
- Face database
- Vector search
- Person re-identification
- Live surveillance mode
- Privacy controls
- Configuration profiles

---

# Why FaceAI?

FaceAI aims to provide a simple, portable, and extensible foundation for computer vision projects. Whether you're experimenting with AI on a laptop or building tools in Termux on Android, FaceAI offers an approachable starting point that can evolve into a production-ready vision toolkit.

---

# Contributing

Contributions are welcome.

Ideas include:

- Better detectors
- Faster inference
- New AI backends
- Performance improvements
- Mobile optimization
- Additional export formats
- Documentation enhancements

---

# License

This project is licensed under the MIT License.

---

## Vision

> **Build once. Run anywhere. Detect faces everywhere.**

FaceAI CLI is designed to grow from a lightweight educational tool into a modular, enterprise-grade computer vision platform capable of powering desktop, cloud, embedded, and mobile AI workflows.
