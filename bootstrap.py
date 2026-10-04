from pathlib import Path
import base64
import zipfile
import io

ROOT = Path(__file__).resolve().parent
PARTS = ROOT / "cloud_parts"
TARGET = ROOT / "Dineflow_Cloud"

if not TARGET.exists():
    files = sorted(PARTS.glob("part*.txt"))
    if not files:
        raise SystemExit("No cloud package parts found.")
    encoded = "".join(p.read_text(encoding="utf-8").strip() for p in files)
    payload = base64.b64decode(encoded, validate=True)
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        zf.extractall(ROOT)

if not (TARGET / "app.py").exists():
    raise SystemExit("Dineflow cloud package extraction failed.")

print("Dineflow cloud package ready.")
