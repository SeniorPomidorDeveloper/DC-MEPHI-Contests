import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    print('Название_колонки', 'Количество_NaN', sep=',')
    for col in data.keys():
        data_col = data[col]
        print(col, data_col.isnull().sum(), sep=',')


if __name__ == '__main__':
    main()
