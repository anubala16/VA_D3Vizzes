import pandas as pd
import json
from pprint import pprint

def readCSrcDict():
    csrc = {}
    with open('output/csources.txt') as json_file:
        data = json.load(json_file)
    csrc = data['csources']
    return csrc

def readCSV(csrc):
    file = "data_subset80k.csv"
    df = pd.read_csv(file)
    print("Sample data shape:", df.shape)

    # takes a long time!
    df['CSrc Simplified'] = df.apply(lambda row: simplifyCSrc(row, csrc), axis=1)
    df['CSrc Freq'] = df.groupby('CSrc Simplified')['CSrc Simplified'].transform('count')

    ''' Done with processing csource; exporting entire df to csv file '''
    df.to_csv('csource_subset.csv')

def simplifyCSrc(row, csrc_dict):
    src = str(row['CSource']).strip().lower()

    #-------Super Partners >=8500 ---------
    if 'google' in src:
        return 'google'
    if 'yahoo' in src:
        return 'yahoo'
    if 'facebook' in src:
        return 'facebook'
    if 'tree' in src:
        return 'Lending Tree/Partners'
    if 'bing' in src:
        return 'bing'
    if 'aol' in src:
        return 'aol'
    if 'unknown' in src or 'undefined' in src:
        return 'unknown'
    if 'mail' in src:
        return 'email'
    if 'criteo' in src:
        return 'criteo'
    if 'msn' in src or 'outlook' in src:
        return 'microsoft'
    if 'toboola' in src:
        return 'taboola'
    if 'realtor' in src:
        return 'realtor.com'

    #-----Strong partners >=1500-8000-------
    if 'weather' in src:
        return 'weather'
    if 'nafdigital' in src:
        return 'nafdigital'
    if 'stringo' in src:
        return 'stringo'
    if 'cnn' in src:
        return 'cnn'
    if 'pandora' in src:
        return 'pandora'
    if 'apple' in src:
        return 'apple'
    if 'tronc' in src:
        return 'tronc'
    if 'nasdaq' in src:
        return 'nasdaq'

    #------decent sources--------
    if 'outbrain' in src:
        return 'outbrain'
    if 'xfinity' in src:
        return 'xfinity'
    if 'magni' in src:
        return 'magnifymoney'

    #-----Others-----
    else:
        return 'other'

if __name__=="__main__":
    csrc = readCSrcDict()
    readCSV(csrc)
