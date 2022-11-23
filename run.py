import pandas as pd
import numpy as np
import sys

def read_data(d):
    if d == 'test'
    try:
        data=pd.read_csv('test/2_test.csv', index_col=0)
        return data
    except:
        print('data read unsuccessful.')

if __name__ == "__main__":
    print(read_data(sys.argv[1]))