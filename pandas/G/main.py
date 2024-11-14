import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    years = data["Year Published"]
    mean = (2021 * years.shape[0] - years.sum()) / years.shape[0]
    print(round(mean, 2))


if __name__ == '__main__':
    main()
