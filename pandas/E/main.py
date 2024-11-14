import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    print(*data[data['Возраст'] > 35]['Имя'])


if __name__ == '__main__':
    main()
