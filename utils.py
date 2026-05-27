"""Small helper functions for notebook experiments."""

from pathlib import Path

from PIL import Image


def ensure_project_dirs() -> None:
    """Create common project folders if they do not already exist."""
    for folder in ("recordings", "images", "outputs"):
        Path(folder).mkdir(parents=True, exist_ok=True)


def load_image(image_path: str | Path) -> Image.Image:
    """Load an image with Pillow for multimodal model experiments."""
    return Image.open(image_path)


def save_text_output(text: str, filename: str = "output.txt") -> Path:
    """Save text output from an agent run into the outputs folder."""
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename
    output_path.write_text(text, encoding="utf-8")
    return output_path


def get_latest_file(folder: str | Path, pattern: str = "*") -> Path | None:
    """Return the newest file in a folder, or None if no files match."""
    files = [path for path in Path(folder).glob(pattern) if path.is_file()]
    if not files:
        return None

    return max(files, key=lambda path: path.stat().st_mtime)
