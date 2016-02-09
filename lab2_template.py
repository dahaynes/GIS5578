#GIS 5578
#Lab 2

#import modules
import arcpy

#Set geodatbase location
gdb_location = r"c:\work\global_datasets.gdb"
arcpy.env.workspace = gdb_location

#This function returns a list of all feature classes found within the geodatabase
AllFeatureClasses = arcpy.ListFeatureClasses()


#This will return for a specific FeatureClass all of the fields.
# Make sure to return field type
for field in arcpy.ListFields(feature):
    print field.name

#
mycsv = open(r"", "w")

mycsv.write("%s, %s" % (field1, field2))