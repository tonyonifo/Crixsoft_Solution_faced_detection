import cv2
import typer
from typing import Optional

app = typer.Typer()

@app.command()
def detect_image(image_path: str, backend: Optional[str] = "scrfd", confidence: float = 0.5):
    """Detect faces in an image."""
    image = cv2.imread(image_path)
    if image is None:
        typer.echo(f"Error: Unable to load image: {image_path}")
        raise typer.Exit(1)

    # Convert to grayscale for simplicity
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Haar cascades for simplicity here (you can replace with ONNX-based backend later)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    typer.echo(f"Found {len(faces)} face(s).")
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save or show
    cv2.imwrite("output.jpg", image)
    typer.echo("Result saved to output.jpg")

@app.command()
def detect_webcam(confidence: float = 0.5):
    """Detect faces from a webcam."""
    cap = cv2.VideoCapture(0)  # 0 is default webcam
    if not cap.isOpened():
        typer.echo("Error: Unable to open webcam.")
        raise typer.Exit(1)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            typer.echo("Error: Failed to grab frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Webcam Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

@app.command()
def detect_video(video_path: str, confidence: float = 0.5):
    """Detect faces in a video."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        typer.echo(f"Error: Unable to open video: {video_path}")
        raise typer.Exit(1)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Video Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    app()
