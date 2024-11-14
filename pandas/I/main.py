import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    res = data['ScreenResolution'].str.split(' ').apply(lambda x: x[-1])
    res = res.str.split('x')
    data['width'] = pd.to_numeric(res.apply(lambda x: x[0]))
    data['height'] = pd.to_numeric(res.apply(lambda x: x[1]))
    dioganal = (data['width'] ** 2 + data['height'] ** 2) ** 0.5
    data['PPI'] = dioganal / data['Inches']
    print(round(data['PPI'].mean(), 2))


if __name__ == '__main__':
    main()
