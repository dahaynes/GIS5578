#GIS 5578
#Lab 2

#import modules
import arcpy

#Set geodatbase location
gdb_location = r"c:\test\global_datasets.gdb"
arcpy.env.workspace = gdb_location

#This function returns a list of all feature classes found within the geodatabase
AllFeatureClasses = arcpy.ListFeatureClasses()


#Choose a single feature class and assign to the variable feature
feature = r"%s\%s" % (, )

#Get the list of fields
for field in arcpy.ListFields(feature):
    print field.name



#Loops through all fields
cursor = arcpy.da.SearchCursor(feature, field.name)
for rec in cursor:
    print rec


