import pandas as pd

def consume(filename):
    df = pd.read_csv(filename,index_col=False)
    return df