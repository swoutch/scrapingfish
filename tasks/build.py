import sys

import build.__main__


if __name__ == '__main__':
    build.__main__.main(sys.argv[1:], 'python -m tasks.build')
