import sys
from pathlib import Path

# Add project root and backend to python path
root_dir = Path(__file__).resolve().parent.parent
backend_dir = root_dir / "backend"

for path in (root_dir, backend_dir):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

from backend.app import app
