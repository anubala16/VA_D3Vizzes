import pandas as pd

def readCSV():
    file = "data.csv"
    df = pd.read_csv(file)
    print("Original data:", df.shape)
    nullCount = df.isnull().sum()
    print("Original null count:\n", nullCount)
    df = deleteColumns(df)
    nullCount = df.isnull().sum()
    print("Nulls after deleting columns:\n----------------\n", nullCount)

    printUniqueValues(df, "geo states")
    printUniqueValues(df, "product")
    printUniqueValues(df, "csource")

def deleteColumns(df):
    df = df.drop(['Mobile Device Type', 'qformuid (evar1)', 'FormStart (ev57) (event57)',
                  'Form Engagement 1 (ev11) (event11)', 'Form Engagement 2 (ev12) (event12)',
                  'Form Conversion (ev59) (event59)', 'FCS Qform Optin Completed (ev373) (event373)',
                  'FCS Client Signup Completed (ev73) (event73)', 'Lender Not Matched (ev522) (event522)',
                  'FormSubmit in Express Offers (ev58) (event58)', 'Lenders Matched (ev501) (event501)',
                  'Page Views', 'Credit Card Apply Clicked (ev69) (event69)', 'MyLT Session Started (ev189) (event189)',
                  'Express No Offers (ev13) (event13)', 'Express Visited (ev290) (event290)', 'cchannel  (eVar19) (evar19)'], axis=1)
    print("After dropping columns:", df.shape)
    return df

# Not sure what rows to delete yet
def deleteRows(df):
    df[df.notnull(df['', '', ''])]

    return df

def printUniqueValues(df, var):
    print("Calculating unique values for", var)
    var = var.lower()
    if "product" in var:
        unique = df['Product Reporting'].unique()
        print("\nUnique Products:\n", unique)
    elif "csourse" in var:
        unique = df['csource (eVar20) (evar20)'].unique()
        print("\nUnique CSource:\n", unique)
    elif "geo" in var:
        unique = df['GeoSegmentation States'].unique()
        print("\nUnique States:\n", unique)

    print('\n------------------------------------------\n')

def preprocessData():
    return

if __name__=="__main__":
    readCSV()
    preprocessData()
