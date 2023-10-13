import shutil
import sys
from pathlib import Path

import build.__main__


if __name__ == '__main__':
    dist_path = Path("dist")

    if dist_path.exists() and dist_path.is_dir():
        for item in dist_path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

    build.__main__.main(sys.argv[1:], 'python -m tasks.build')
