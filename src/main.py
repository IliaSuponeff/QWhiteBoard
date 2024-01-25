import sys
from controllers.application import QWhiteBoardApplication


def main():
    app = QWhiteBoardApplication()
    sys.exit(app.execute())


if __name__ == '__main__':
    main()
