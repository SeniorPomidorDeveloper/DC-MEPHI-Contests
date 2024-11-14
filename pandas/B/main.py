import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    names = data['Имя'].value_counts()
    names = names[names == names.max()]
    names = names.sort_index(ascending=True)
    for name in names.keys():
        print(name, names.max())


if __name__ == '__main__':
    main()
