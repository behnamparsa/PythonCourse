#!./venv/bin/python

import pandas as pd # type: ignore
import numpy as np # type: ignore

def main():
    df = pd.read_csv("mall_customers.csv", index_col=0)
    df.columns = ['Gender', 'Age', 'Income', 'Spending']

    print(df)

    df = df.drop('Gender', axis=1)

    corr = df.corr()
    np.fill_diagonal(corr.values, 1)

    print(corr)


if __name__ == "__main__":  
    main()
