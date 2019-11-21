import arcpy
from arcpy import env
env.workspace = r"H:\PythonGIS\youngsang\data\data\geoportal.gdb"
env.overwriteOutput = True

fc = "Grocer"
desc = arcpy.Describe(fc)
#print desc.fields.name
#for item in desc.fields:
#    print item.name, item.type, item.length
fieldList = arcpy.ListFields(fc)
for item in fieldList:
    print item.name, item.type
    
fcList = arcpy.ListFeatureClasses(feature_type = "Point")
print fcList
try:
    for item in fcList:
        arcpy.Buffer_analysis(item, item + "_Out", "1000 Meter")
except:
    print arcpy.GetMessages()

print "success!!!" 