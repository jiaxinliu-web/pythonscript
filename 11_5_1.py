import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\Liu"
env.overwriteOutput = True

fc = "us_major_cities.shp"
fieldName0 = "NAME"
fieldName1 = "POPULATION"
print "worked"

#rows = arcpy.da.SearchCursor(fc) #rows is a cursor object, when using with, add da
row = rows.next() #row is also a object, next method called from cursor object which returned row object, if for loop, it doesnot need.

#while row:
    #print row.NAME
    #print row.getValue(fieldName0), row.getValue(fieldName1)
    #row = rows.next()
##for row in rows:
##    totalPopulation += row.getValue(fieldName1)
##        recordsCounted += 1
##    #print row.getValue(fieldName0)

average = 0
totalPopulation = 0
recordsCounted = 0
with arcpy.da.SearchCursor(fc,("NAME","POPULATION")) as cursor: #if without "POPULATION", ("NAME",) like that
    for row in cursor:
        totalPopulation += row[1]
        recordsCounted += 1.0
        #print row[0], row[1]
        

average = totalPopulation/recordsCounted
print "Average population for each major cities is " + (average) #counts would be a float and int/float=float
        