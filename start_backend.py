#!/usr/bin/env python3
"""Start backend helper.

Usage: python start_backend.py

This script will:
- ensure a virtual environment exists under ./backend/venv
- install requirements from backend/requirements.txt
- seed demo data (runs backend/demo_data.py)
- start the uvicorn server

Run from repository root.
"""
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "backend"
VENV = BACKEND / "venv"


def run(cmd, **kwargs):
    print(f"$ {' '.join(cmd)}")
    return subprocess.check_call(cmd, **kwargs)


def ensure_venv():
    if not VENV.exists():
        print("Creating virtual environment...")
        run([sys.executable, "-m", "venv", str(VENV)])


def install_requirements():
    pip = VENV / ("Scripts/pip.exe" if os.name == "nt" else "bin/pip")
    req = BACKEND / "requirements.txt"
    if req.exists():
        print("Installing backend requirements...")
        run([str(pip), "install", "-r", str(req)])
    else:
        print("No requirements.txt found in backend/; skipping install")


def seed_demo_data():
    demo = BACKEND / "demo_data.py"
    if demo.exists():
        print("Seeding demo data...")
        py = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        run([str(py), str(demo)], cwd=str(BACKEND))
    else:
        print("No demo_data.py found; skipping seeding")


def start_uvicorn():
    py = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    print("Starting uvicorn on http://0.0.0.0:8000 ...")
    run([str(py), "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"], cwd=str(BACKEND))


def main():
    os.chdir(str(ROOT))
    ensure_venv()
    install_requirements()
    seed_demo_data()
    start_uvicorn()


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(e.returncode)
