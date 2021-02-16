#import datetime
import pandas as pd
import glob
import urllib.request

def getcsv():
    extension = 'csv'
    files = glob.glob('*.{}'.format(extension))
    return(files)

def getDataFrame(file):
    data_frame = pd.read_csv(file, sep=',')
    return(data_frame)

def write_to_file(array, outfile):
    try:
        pd.DataFrame(array).to_csv(outfile, index=False, header=True)
    except:
        print('Could not write to ',outfile, ': Access Denied.')
        if not input('Try again? (y/n)') == 'y': return
        write_to_file(array, outfile)

def fixDates(inDate):
    print(inDate)

def main():
    # download latest
    url = 'https://www.denvergov.org/media/gis/DataCatalog/crime/csv/crime.csv'
    urllib.request.urlretrieve(url, 'crime.csv')

    # define static input and output file names
    crimeReport = 'crime.csv'
    newFile = 'cleanCrime.csv'

    # create dataframe using infile
    df = getDataFrame(crimeReport)

    # parse dataframe columns to just needed columns
    df = df[['OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'FIRST_OCCURRENCE_DATE', 'INCIDENT_ADDRESS', 'GEO_X', 'GEO_Y', 'GEO_LON', 'GEO_LAT']]
    
    # find lat and lon rows with no value and drop those rows from the dataframe
    df = df.dropna(subset=['GEO_LON', 'GEO_LAT'])
    
    # convert first occurrence dates to datetime format
    df['FIRST_OCCURRENCE_DATE']=pd.to_datetime(df['FIRST_OCCURRENCE_DATE'])
    
    # remove commas from all fields
    df = df.replace(',', '', regex=True)
    
    # write dataframe to file
    write_to_file(df, newFile)
    print(df.info)


main()