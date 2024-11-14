import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    names = data['Имя'].unique()
    names.sort()
    print(*names)


if __name__ == '__main__':
    main()
