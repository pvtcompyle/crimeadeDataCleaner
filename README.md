# crimeadeDataCleaner
This script was desingned specfically for pulling crime data in the Denver area for use in a specific application.  
https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-crime



Specifically, it pulls "Crime - Comma seperated values". It then drops some of the fields, strips out any rows with
null values in the geolocation data, and converts the dates to a MySQL friend DATETIME format, exporting the resultant
data set to a clean csv. 

The most notable benefit of this approach is that there appears to be some garbage data contained within the original 
download, which causes the import into MySQL to stall out for hours on end. 
