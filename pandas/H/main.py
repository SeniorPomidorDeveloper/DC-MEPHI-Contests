import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    strategys = data[data['Domains'].str.contains('Strategy Games')]
    raitings = pd.to_numeric(strategys['Rating Average'].str.replace(',', '.'),
                             downcast='float')
    print(round(raitings.mean(), 2))


if __name__ == '__main__':
    main()
