import os

directory_path = __file__.split(os.path.sep)
directory_path.pop(-1)
directory_path = os.path.sep.join(directory_path) + os.path.sep

if __name__ == '__main__':
    print(__name__)
    print(__doc__)
    print(__file__)
    print(__package__)
    print(directory_path)
