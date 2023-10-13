import shutil
import sys
from pathlib import Path

import build.__main__


def clean_directory(path: Path) -> None:
    if path.exists() and path.is_dir():
        for item in path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)


if __name__ == '__main__':
    clean_directory(Path("dist"))
    build.__main__.main(sys.argv[1:], 'python -m tasks.build')
