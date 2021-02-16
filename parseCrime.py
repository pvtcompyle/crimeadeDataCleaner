#import datetime
import pandas as pd
import glob
import urllib.request

def main():
    # download latest
    print('Downloading Denver crime data ...')
    url = 'https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv'
    urllib.request.urlretrieve(url, 'crime.csv')
    print('Download complete .... \n\n')

    # define static input and output file names
    crimeReport = 'crime.csv'
    newFile = 'cleanCrime.csv'

    # create dataframe using infile
    df = pd.read_csv(crimeReport, sep=',')

    # parse dataframe columns to just needed columns
    df = df[['OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE', 'INCIDENT_ADDRESS', 'GEO_X', 'GEO_Y', 'GEO_LON', 'GEO_LAT']]
    
    # find lat and lon rows with no value and drop those rows from the dataframe
    df = df.dropna(subset=['GEO_LON', 'GEO_LAT'])
    
    # convert first occurrence dates to datetime format
    print('Converting dates to MySQL friendly DATETIME format ...')
    print('This may take several minutes.')
    df['FIRST_OCCURRENCE_DATE']=pd.to_datetime(df['FIRST_OCCURRENCE_DATE'])
    print('Conversion complete ... \n\n')
    
    # remove commas from all fields
    df = df.replace(',', '', regex=True)
    
    # write dataframe to file
    print('Writting new file ...')
    pd.DataFrame(df).to_csv(newFile, index=False, header=True)
    print('Write complete. Have a nice day. \n\n')
   
    print(df.info)


main()
