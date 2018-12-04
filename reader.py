import pandas as pd
import json

def readCSV():
    stateCodes = getStateCodes()

    file = "data.csv"
    df = pd.read_csv(file)
    print("Original data:", df.shape)

    df = deleteColumns(df)

    ''' Renaming some columns for readability '''
    df = df.rename(index=str, columns={"Product Reporting": "Product", "csource (eVar20) (evar20)": "CSource"})

    ''' Separate countries and states '''
    df = processCountryStates(df)

    ''' Delete non-US rows '''
    df = getUSRecords(df)
    print("Only US Records:", df.shape)
    df.drop(columns=['Country'], inplace = True)

    # sampling only 30% of data
    df = df.sample(frac=0.3)

    ''' Separate date '''
    df = processDate(df)

    df.Product.fillna("unknown", inplace=True)
    print("Replaced product with unknowns")

    df.CSource.fillna("unknown", inplace=True)
    print("Replaced csource with unknowns")

    # takes a long time!
    # Gets all the unique values and counts for each product, csource, date, and state
    # run once only :)
    df = preprocessRow(df)

    # Add state code column
    state = str(df['State'][1]).strip()
    code = stateCodes[state]
    df['State Code'] = df['State'].replace('(.*)', code, regex=True)

    # removing the comma at the end of every Month value
    df['Month'] = df['Month'].str[:-1].astype(int)

    ''' Done with preprocessing; exporting entire df to csv file '''
    df.to_csv('data_subset.csv')
    print("Wrote", df.shape[0], "rows to data_subset.csv")

def preprocessRow(df):
    csources = {}
    products = {}
    states = {}
    dates = {}
    print("Preprocessing rows in df...")
    for idx, row in df.iterrows():
        print(idx)
        prd = str(row['Product']).strip()
        count = products.get(prd, 0)
        products[prd] = count + 1

        csrc = str(row['CSource']).strip()
        count = csources.get(csrc, 0)
        csources[csrc] = count + 1

        st = str(row['State']).strip()
        count = states.get(st, 0)
        states[st] = count + 1

        dt = str(row['Date']).strip()
        count = dates.get(dt, 0)
        dates[dt] = count + 1

    # write all the dictionaries to files
    print("Done iterating df; printing keys and values to files...")
    f = open("output/products.txt", "w")
    products = {'products': products}
    f.write(json.dumps(products))
    f.close()

    f = open("output/csources.txt", "w")
    csources = {'csources': csources}
    f.write(json.dumps(csources))
    f.close()

    f = open("output/states.txt", "w")
    states = {'states': states}
    f.write(json.dumps(states))
    f.close()

    f = open("output/dates.txt", "w")
    dates = {'dates': dates}
    f.write(json.dumps(dates))
    f.close()

    return df

def getStateCodes():
    states = {
        "alabama": 1,
        "alaska": 2,
        "arizona": 4,
        "arkansas": 5,
        "california": 6,
        "colorado": 8,
        "connecticut": 9,
        "delaware": 10,
        "florida": 12,
        "georgia": 13,
        "hawaii": 15,
        "idaho": 16,
        "illinois": 17,
        "indiana": 18,
        "iowa": 19,
        "kansas": 20,
        "kentucky": 21,
        "louisiana": 22,
        "maine": 23,
        "maryland": 24,
        "massachusetts": 25,
        "michigan": 26,
        "minnesota": 27,
        "mississippi": 28,
        "missouri": 29,
        "montana": 30,
        "nebraska": 31,
        "nevada": 32,
        "new hampshire": 33,
        "new jersey": 34,
        "new mexico": 35,
        "new york": 36,
        "north carolina": 37,
        "north dakota": 38,
        "ohio": 39,
        "oklahoma": 39,
        "oregon": 41,
        "pennsylvania": 42,
        "rhode island": 44,
        "south carolina": 45,
        "south dakota": 46,
        "tennessee": 47,
        "texas": 48,
        "utah": 49,
        "vermont": 50,
        "virginia": 51,
        "washington": 53,
        "west virginia": 54,
        "wisconsin": 55,
        "wyoming": 56,
    }
    return states

def getUSRecords(df):
    return df.loc[df['Country'] == 'united states)']

def processDate(df):
    new = df['Date'].str.split(" ", n=2, expand=True)
    df['Day'] = new[0]
    df['Month'] = new[1]
    return df

def processCountryStates(df):
    new = df["GeoSegmentation States"].str.split("(", n=1, expand=True)
    df['State'] = new[0]
    df['Country'] = new[1]
    df.drop(columns=['GeoSegmentation States'], inplace=True)
    return df

def deleteColumns(df):
    df.drop(['Mobile Device Type', 'qformuid (evar1)', 'FormStart (ev57) (event57)',
             'Form Engagement 1 (ev11) (event11)', 'Form Engagement 2 (ev12) (event12)',
             'Form Conversion (ev59) (event59)', 'FCS Qform Optin Completed (ev373) (event373)',
             'FCS Client Signup Completed (ev73) (event73)', 'Lender Not Matched (ev522) (event522)',
             'FormSubmit in Express Offers (ev58) (event58)', 'Lenders Matched (ev501) (event501)',
             'Page Views', 'Credit Card Apply Clicked (ev69) (event69)', 'MyLT Session Started (ev189) (event189)',
             'Express No Offers (ev13) (event13)', 'Express Visited (ev290) (event290)',
             'cchannel  (eVar19) (evar19)', 'TreeAuthID (evar50)'], inplace=True, axis=1)

    print("Shape after dropping columns:", df.shape)
    return df

if __name__=="__main__":
    readCSV()
