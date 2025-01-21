import pandas as pd

# consume the data from the converted csv file
def consume(filename):
    df = pd.read_csv(filename,index_col=False)
    return df