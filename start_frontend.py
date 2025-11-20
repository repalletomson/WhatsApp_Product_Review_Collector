#!/usr/bin/env python3
"""Start frontend helper.

Usage: python start_frontend.py

This script will:
- ensure frontend dependencies are installed (npm install)
- run `npm start` in the frontend directory

Run from repository root.
"""
import os
import shlex
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FRONTEND = ROOT / "frontend"


def run(cmd, **kwargs):
    print(f"$ {' '.join(cmd)}")
    return subprocess.check_call(cmd, **kwargs)


def ensure_node_deps():
    node_modules = FRONTEND / "node_modules"
    if not node_modules.exists():
        print("Installing frontend node dependencies (npm install)...")
        run(["npm", "install"], cwd=str(FRONTEND))
    else:
        print("node_modules exists; skipping npm install")


def start_frontend():
    print("Starting frontend dev server on http://localhost:3000 ...")
    run(["npm", "start"], cwd=str(FRONTEND))


def main():
    os.chdir(str(ROOT))
    ensure_node_deps()
    start_frontend()


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        sys.exit(e.returncode)
