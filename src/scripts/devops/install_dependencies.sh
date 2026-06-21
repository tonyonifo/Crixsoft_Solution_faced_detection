#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 is not installed."
  exit 1
fi

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Install system libraries required by OpenCV on Ubuntu/Debian-based systems.
if command -v apt-get >/dev/null 2>&1; then
  if [ "$(id -u)" -eq 0 ]; then
    apt-get update
    apt-get install -y libgl1 libglib2.0-0
  elif command -v sudo >/dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y libgl1 libglib2.0-0
  else
    echo "Warning: apt-get found but sudo is not available. Skipping system package installation."
  fi
fi

source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Dependencies installed into .venv"
echo "Activate the environment with: source .venv/bin/activate"
echo "Run the CLI with: python faceai.py --help"
