import pandas as pd
import json

def readCSV():

    file = "data_preprocessed.csv"
    df = pd.read_csv(file)
    print("Sample data shape:", df.shape)

    # takes a long time!
    # Gets all the unique values and counts for each product, csource, date, and state
    # run once only :)
    df = preprocessRow(df)

    ''' Done with processing csource; exporting entire df to csv file '''
    df.to_csv('csource_subset.csv')

def preprocessRow(df):

    return df

if __name__=="__main__":
    readCSV()
