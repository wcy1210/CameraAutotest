import sys
from run import Manual_run

def get_args():
    return sys.argv[1:]


if __name__ == '__main__':
    argv = get_args()
    Manual_run.