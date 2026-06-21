import cv2
from pathlib import Path
from typing import Tuple

import typer

app = typer.Typer(help="FaceAI CLI: perform face detection on images, video, or webcam input.")

SUPPORTED_BACKENDS = {"haar", "cascade"}


def get_haar_parameters(confidence: float) -> dict:
    """Map confidence to Haar cascade detector parameters."""
    min_neighbors = max(3, min(10, int((1.0 - confidence) * 10 + 3)))
    scale_factor = 1.05 + (1.0 - confidence) * 0.1
    return {"scaleFactor": round(scale_factor, 2), "minNeighbors": min_neighbors, "minSize": (50, 50)}


def load_haar_detector() -> cv2.CascadeClassifier:
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(cascade_path)
    if detector.empty():
        raise RuntimeError(f"Unable to load Haar cascade classifier from {cascade_path}")
    return detector


def validate_backend(backend: str) -> str:
    backend = backend.lower()
    if backend not in SUPPORTED_BACKENDS:
        raise typer.BadParameter(f"Unsupported backend: {backend}. Supported backends: {', '.join(sorted(SUPPORTED_BACKENDS))}")
    return backend


def detect_faces(frame: cv2.Mat, detector: cv2.CascadeClassifier, confidence: float) -> list[tuple[int, int, int, int]]:
    params = get_haar_parameters(confidence)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, **params)
    return faces


def draw_faces(frame: cv2.Mat, faces: list[tuple[int, int, int, int]]) -> cv2.Mat:
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


def load_image(image_path: Path) -> cv2.Mat:
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Unable to load image: {image_path}")
    return image


@app.command(name="detect-image")
def detect_image(
    image_path: Path = typer.Argument(..., help="Path to the input image."),
    backend: str = typer.Option("haar", "--backend", "-b", help="Face detection backend."),
    confidence: float = typer.Option(0.5, "--confidence", "-c", min=0.0, max=1.0, help="Detection confidence (higher reduces false positives)."),
    output_path: Path = typer.Option(Path("output.jpg"), "--output", "-o", help="Path to save the output image."),
):
    """Detect faces in an image."""
    backend = validate_backend(backend)
    detector = load_haar_detector()
    image = load_image(image_path)
    faces = detect_faces(image, detector, confidence)

    typer.echo(f"Found {len(faces)} face(s) with backend '{backend}'.")
    output = draw_faces(image, faces)
    cv2.imwrite(str(output_path), output)
    typer.echo(f"Result saved to {output_path}")


@app.command(name="detect-video")
def detect_video(
    video_path: Path = typer.Argument(..., help="Path to the input video."),
    backend: str = typer.Option("haar", "--backend", "-b", help="Face detection backend."),
    confidence: float = typer.Option(0.5, "--confidence", "-c", min=0.0, max=1.0, help="Detection confidence (higher reduces false positives)."),
):
    """Detect faces in a video."""
    backend = validate_backend(backend)
    detector = load_haar_detector()

    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        typer.echo(f"Error: Unable to open video: {video_path}")
        raise typer.Exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = detect_faces(frame, detector, confidence)
        frame = draw_faces(frame, faces)
        cv2.imshow("Video Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


@app.command(name="detect-webcam")
def detect_webcam(
    backend: str = typer.Option("haar", "--backend", "-b", help="Face detection backend."),
    confidence: float = typer.Option(0.5, "--confidence", "-c", min=0.0, max=1.0, help="Detection confidence (higher reduces false positives)."),
):
    """Detect faces from a webcam."""
    backend = validate_backend(backend)
    detector = load_haar_detector()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        typer.echo("Error: Unable to open webcam.")
        raise typer.Exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            typer.echo("Error: Failed to grab frame.")
            break

        faces = detect_faces(frame, detector, confidence)
        frame = draw_faces(frame, faces)
        cv2.imshow("Webcam Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    app()
