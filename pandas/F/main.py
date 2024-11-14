import numpy as np
import pandas as pd
import sys


def main():
    data = pd.read_csv(sys.argv[1])
    thems = data["Domains"].str.split(',').apply(lambda x: np.array(x))
    thems = thems.to_numpy()
    thems = np.concatenate(thems)
    thems = pd.Series(thems).value_counts()
    max_n = thems.max()
    thems = thems[thems == max_n].sort_index()
    for name in thems.keys():
        print(name, int(max_n))


if __name__ == '__main__':
    main()
