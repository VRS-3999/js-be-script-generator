import os
from pathlib import Path

import uvicorn

if __name__ == "__main__":
    src_dir = Path(__file__).resolve().parent / "src"
    if src_dir.exists() and src_dir.is_dir():
        os.chdir(src_dir)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8045,
        log_level="info",
        reload=True)
