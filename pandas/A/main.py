import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.stdin, header=None)
    print(*data.shape, sep='\n')


if __name__ == '__main__':
    main()
