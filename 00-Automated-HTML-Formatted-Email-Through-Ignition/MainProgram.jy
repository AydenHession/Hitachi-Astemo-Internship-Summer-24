from java.io import File
from javax.imageio import ImageIO

#importing the Time library for the date and the time. 
from time import sleep
import datetime

# Importing the necessary modules for email sending
from java.nio.file import Files
from java.nio.file import Paths

#Defining The Station Object Class
class StationObject:
	def __init__(self, Station, NGA, NGB, NGC, NGD, NGE, NGF):
		self.Station = Station
		self.NGA = NGA
		self.NGB = NGB
		self.NGC = NGC
		self.NGD = NGD
		self.NGE = NGE
		self.NGF = NGF

def format_value(value):
    return "0" if value == 0 else "{:.2f}".format(value)
    
def format_quantity(value):
	return "0" if value == 0 else "{:.0f}".format(value)

def Main():


	#Getting Times & Dates
	todays_date = datetime.date.today().strftime('_%m_%d_%y')
	current_time = datetime.datetime.now().strftime('_%H_%M')
	
	#Station Object Array
	StationObjectArray = [58]
	
	
	#PARTS
	#SourceA/Block {2}/Station {1}/Data/Dashboard/NGParts/NGPart1st.value
	
	#PERCENTS
	#SourceA/Block {1}/Station {2}/Data/Dashboard/NG Percent 1st
	
	#Block A
	#1016
	#1st Column
	TagPathNGA_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1016_value = system.tag.readBlocking([TagPathNGA_1016])[0].value
	StringA_1016 = format_quantity(TagNGA_1016_value)
	
	TagPathNGB_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NG Percent 1st"
	TagNGB_1016_value = system.tag.readBlocking([TagPathNGB_1016])[0].value
	#StringB_1016 = format_value(TagNGB_1016_value)
	StringB_1016 = format_value(TagNGB_1016_value)
	
	#2nd Column
	TagPathNGC_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1016_value = system.tag.readBlocking([TagPathNGC_1016])[0].value
	StringC_1016 = format_quantity(TagNGC_1016_value)
	
	TagPathNGD_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NG Percent 2nd"
	TagNGD_1016_value = system.tag.readBlocking([TagPathNGD_1016])[0].value
	#StringD_1016 = format_value(TagNGD_1016_value)
	StringD_1016 = format_value(TagNGD_1016_value)
	
	#3rd Column
	TagPathNGE_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1016_value = system.tag.readBlocking([TagPathNGE_1016])[0].value
	StringE_1016 = format_quantity(TagNGE_1016_value)
	
	TagPathNGF_1016 = "SourceA/Block A/Station 1016/Data/Dashboard/NG Percent 3rd"
	TagNGF_1016_value = system.tag.readBlocking([TagPathNGF_1016])[0].value
	#StringF_1016 = format_value(TagNGF_1016_value)
	StringF_1016 = format_value(TagNGF_1016_value)
	
	#Adding 1016 To Object Array
	#Object_1016 = StationObject("1016", TagNGA_1016_value, TagNGB_1016_value, TagNGC_1016_value, TagNGD_1016_value, TagNGE_1016_value, TagNGF_1016_value)
	#StationObjectArray.append(Object_1016)
	#/1016
	
	#1020
	#1st Column
	TagPathNGA_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1020_value = system.tag.readBlocking([TagPathNGA_1020])[0].value
	StringA_1020 = format_quantity(TagNGA_1020_value)
	
	TagPathNGB_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NG Percent 1st"
	TagNGB_1020_value = system.tag.readBlocking([TagPathNGB_1020])[0].value
	StringB_1020 = format_value(TagNGB_1020_value)
	
	#2nd Column
	TagPathNGC_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1020_value = system.tag.readBlocking([TagPathNGC_1020])[0].value
	StringC_1020 = format_quantity(TagNGC_1020_value)
	
	TagPathNGD_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NG Percent 2nd"
	TagNGD_1020_value = system.tag.readBlocking([TagPathNGD_1020])[0].value
	StringD_1020 = format_value(TagNGD_1020_value)
	
	#3rd Column
	TagPathNGE_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1020_value = system.tag.readBlocking([TagPathNGE_1020])[0].value
	StringE_1020 = format_quantity(TagNGE_1020_value)
	
	TagPathNGF_1020 = "SourceA/Block A/Station 1020/Data/Dashboard/NG Percent 3rd"
	TagNGF_1020_value = system.tag.readBlocking([TagPathNGF_1020])[0].value
	StringF_1020 = format_value(TagNGF_1020_value)
	
	#Adding 1020 To Object Array
	Object_1020 = StationObject("1020", TagNGA_1020_value, TagNGB_1020_value, TagNGC_1020_value, TagNGD_1020_value, TagNGE_1020_value, TagNGF_1020_value)
	StationObjectArray.append(Object_1020)
	#/1020
	
	#1030
	#1st Column
	TagPathNGA_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1030_value = system.tag.readBlocking([TagPathNGA_1030])[0].value
	StringA_1030 = format_quantity(TagNGA_1030_value)
	
	TagPathNGB_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NG Percent 1st"
	TagNGB_1030_value = system.tag.readBlocking([TagPathNGB_1030])[0].value
	StringB_1030 = format_value(TagNGB_1030_value)
	
	#2nd Column
	TagPathNGC_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1030_value = system.tag.readBlocking([TagPathNGC_1030])[0].value
	StringC_1030 = format_quantity(TagNGC_1030_value)
	
	TagPathNGD_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NG Percent 2nd"
	TagNGD_1030_value = system.tag.readBlocking([TagPathNGD_1030])[0].value
	StringD_1030 = format_value(TagNGD_1030_value)
	
	#3rd Column
	TagPathNGE_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1030_value = system.tag.readBlocking([TagPathNGE_1030])[0].value
	StringE_1030 = format_quantity(TagNGE_1030_value)
	
	TagPathNGF_1030 = "SourceA/Block A/Station 1030/Data/Dashboard/NG Percent 3rd"
	TagNGF_1030_value = system.tag.readBlocking([TagPathNGF_1030])[0].value
	StringF_1030 = format_value(TagNGF_1030_value)
	
	#Adding 1030 To Object Array
	Object_1030 = StationObject("1030", TagNGA_1030_value, TagNGB_1030_value, TagNGC_1030_value, TagNGD_1030_value, TagNGE_1030_value, TagNGF_1030_value)
	StationObjectArray.append(Object_1030)
	#/1030
	
	#1040
	#1st Column
	TagPathNGA_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1040_value = system.tag.readBlocking([TagPathNGA_1040])[0].value
	StringA_1040 = format_quantity(TagNGA_1040_value)
	
	TagPathNGB_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NG Percent 1st"
	TagNGB_1040_value = system.tag.readBlocking([TagPathNGB_1040])[0].value
	StringB_1040 = format_value(TagNGB_1040_value)
	
	#2nd Column
	TagPathNGC_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1040_value = system.tag.readBlocking([TagPathNGC_1040])[0].value
	StringC_1040 = format_quantity(TagNGC_1040_value)
	
	TagPathNGD_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NG Percent 2nd"
	TagNGD_1040_value = system.tag.readBlocking([TagPathNGD_1040])[0].value
	StringD_1040 = format_value(TagNGD_1040_value)
	
	#3rd Column
	TagPathNGE_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1040_value = system.tag.readBlocking([TagPathNGE_1040])[0].value
	StringE_1040 = format_quantity(TagNGE_1040_value)
	
	TagPathNGF_1040 = "SourceA/Block A/Station 1040/Data/Dashboard/NG Percent 3rd"
	TagNGF_1040_value = system.tag.readBlocking([TagPathNGF_1040])[0].value
	StringF_1040 = format_value(TagNGF_1040_value)
	
	#Adding 1040 To Object Array
	Object_1040 = StationObject("1040", TagNGA_1040_value, TagNGB_1040_value, TagNGC_1040_value, TagNGD_1040_value, TagNGE_1040_value, TagNGF_1040_value)
	StationObjectArray.append(Object_1040)
	#/1040
	
	#1048
	#1st Column
	TagPathNGA_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1048_value = system.tag.readBlocking([TagPathNGA_1048])[0].value
	StringA_1048 = format_quantity(TagNGA_1048_value)
	
	TagPathNGB_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NG Percent 1st"
	TagNGB_1048_value = system.tag.readBlocking([TagPathNGB_1048])[0].value
	StringB_1048 = format_value(TagNGB_1048_value)
	
	#2nd Column
	TagPathNGC_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1048_value = system.tag.readBlocking([TagPathNGC_1048])[0].value
	StringC_1048 = format_quantity(TagNGC_1048_value)
	
	TagPathNGD_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NG Percent 2nd"
	TagNGD_1048_value = system.tag.readBlocking([TagPathNGD_1048])[0].value
	StringD_1048 = format_value(TagNGD_1048_value)
	
	#3rd Column
	TagPathNGE_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1048_value = system.tag.readBlocking([TagPathNGE_1048])[0].value
	StringE_1048 = format_quantity(TagNGE_1048_value)
	
	TagPathNGF_1048 = "SourceA/Block A/Station 1048/Data/Dashboard/NG Percent 3rd"
	TagNGF_1048_value = system.tag.readBlocking([TagPathNGF_1048])[0].value
	StringF_1048 = format_value(TagNGF_1048_value)
	
	#Adding 1048 To Object Array
	Object_1048 = StationObject("1048", TagNGA_1048_value, TagNGB_1048_value, TagNGC_1048_value, TagNGD_1048_value, TagNGE_1048_value, TagNGF_1048_value)
	StationObjectArray.append(Object_1048)
	#/1048
	
	#1050
	#1st Column
	TagPathNGA_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1050_value = system.tag.readBlocking([TagPathNGA_1050])[0].value
	StringA_1050 = format_quantity(TagNGA_1050_value)
	
	TagPathNGB_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NG Percent 1st"
	TagNGB_1050_value = system.tag.readBlocking([TagPathNGB_1050])[0].value
	StringB_1050 = format_value(TagNGB_1050_value)
	
	#2nd Column
	TagPathNGC_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1050_value = system.tag.readBlocking([TagPathNGC_1050])[0].value
	StringC_1050 = format_quantity(TagNGC_1050_value)
	
	TagPathNGD_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NG Percent 2nd"
	TagNGD_1050_value = system.tag.readBlocking([TagPathNGD_1050])[0].value
	StringD_1050 = format_value(TagNGD_1050_value)
	
	#3rd Column
	TagPathNGE_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1050_value = system.tag.readBlocking([TagPathNGE_1050])[0].value
	StringE_1050 = format_quantity(TagNGE_1050_value)
	
	TagPathNGF_1050 = "SourceA/Block A/Station 1050/Data/Dashboard/NG Percent 3rd"
	TagNGF_1050_value = system.tag.readBlocking([TagPathNGF_1050])[0].value
	StringF_1050 = format_value(TagNGF_1050_value)
	
	#Adding 1050 To Object Array
	Object_1050 = StationObject("1050", TagNGA_1050_value, TagNGB_1050_value, TagNGC_1050_value, TagNGD_1050_value, TagNGE_1050_value, TagNGF_1050_value)
	StationObjectArray.append(Object_1050)
	#/1050
	
	#1060
	#1st Column
	TagPathNGA_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1060_value = system.tag.readBlocking([TagPathNGA_1060])[0].value
	StringA_1060 = format_quantity(TagNGA_1060_value)
	
	TagPathNGB_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NG Percent 1st"
	TagNGB_1060_value = system.tag.readBlocking([TagPathNGB_1060])[0].value
	StringB_1060 = format_value(TagNGB_1060_value)
	
	#2nd Column
	TagPathNGC_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1060_value = system.tag.readBlocking([TagPathNGC_1060])[0].value
	StringC_1060 = format_quantity(TagNGC_1060_value)
	
	TagPathNGD_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NG Percent 2nd"
	TagNGD_1060_value = system.tag.readBlocking([TagPathNGD_1060])[0].value
	StringD_1060 = format_value(TagNGD_1060_value)
	
	#3rd Column
	TagPathNGE_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1060_value = system.tag.readBlocking([TagPathNGE_1060])[0].value
	StringE_1060 = format_quantity(TagNGE_1060_value)
	
	TagPathNGF_1060 = "SourceA/Block A/Station 1060/Data/Dashboard/NG Percent 3rd"
	TagNGF_1060_value = system.tag.readBlocking([TagPathNGF_1060])[0].value
	StringF_1060 = format_value(TagNGF_1060_value)
	
	#Adding 1060 To Object Array
	Object_1060 = StationObject("1060", TagNGA_1060_value, TagNGB_1060_value, TagNGC_1060_value, TagNGD_1060_value, TagNGE_1060_value, TagNGF_1060_value)
	StationObjectArray.append(Object_1060)
	#/1060
	
	#1070
	#1st Column
	TagPathNGA_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1070_value = system.tag.readBlocking([TagPathNGA_1070])[0].value
	StringA_1070 = format_quantity(TagNGA_1070_value)
	
	TagPathNGB_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NG Percent 1st"
	TagNGB_1070_value = system.tag.readBlocking([TagPathNGB_1070])[0].value
	StringB_1070 = format_value(TagNGB_1070_value)
	
	#2nd Column
	TagPathNGC_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1070_value = system.tag.readBlocking([TagPathNGC_1070])[0].value
	StringC_1070 = format_quantity(TagNGC_1070_value)
	
	TagPathNGD_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NG Percent 2nd"
	TagNGD_1070_value = system.tag.readBlocking([TagPathNGD_1070])[0].value
	StringD_1070 = format_value(TagNGD_1070_value)
	
	#3rd Column
	TagPathNGE_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1070_value = system.tag.readBlocking([TagPathNGE_1070])[0].value
	StringE_1070 = format_quantity(TagNGE_1070_value)
	
	TagPathNGF_1070 = "SourceA/Block A/Station 1070/Data/Dashboard/NG Percent 3rd"
	TagNGF_1070_value = system.tag.readBlocking([TagPathNGF_1070])[0].value
	StringF_1070 = format_value(TagNGF_1070_value)
	
	#Adding 1070 To Object Array
	Object_1070 = StationObject("1070", TagNGA_1070_value, TagNGB_1070_value, TagNGC_1070_value, TagNGD_1070_value, TagNGE_1070_value, TagNGF_1070_value)
	StationObjectArray.append(Object_1070)
	#/1070
	
	#1071
	#1st Column
	TagPathNGA_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1071_value = system.tag.readBlocking([TagPathNGA_1071])[0].value
	StringA_1071 = format_quantity(TagNGA_1071_value)
	
	TagPathNGB_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NG Percent 1st"
	TagNGB_1071_value = system.tag.readBlocking([TagPathNGB_1071])[0].value
	StringB_1071 = format_value(TagNGB_1071_value)
	
	#2nd Column
	TagPathNGC_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1071_value = system.tag.readBlocking([TagPathNGC_1071])[0].value
	StringC_1071 = format_quantity(TagNGC_1071_value)
	
	TagPathNGD_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NG Percent 2nd"
	TagNGD_1071_value = system.tag.readBlocking([TagPathNGD_1071])[0].value
	StringD_1071 = format_value(TagNGD_1071_value)
	
	#3rd Column
	TagPathNGE_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1071_value = system.tag.readBlocking([TagPathNGE_1071])[0].value
	StringE_1071 = format_quantity(TagNGE_1071_value)
	
	TagPathNGF_1071 = "SourceA/Block A/Station 1071/Data/Dashboard/NG Percent 3rd"
	TagNGF_1071_value = system.tag.readBlocking([TagPathNGF_1071])[0].value
	StringF_1071 = format_value(TagNGF_1071_value)
	
	#Adding 1071 To Object Array
	Object_1071 = StationObject("1071", TagNGA_1071_value, TagNGB_1071_value, TagNGC_1071_value, TagNGD_1071_value, TagNGE_1071_value, TagNGF_1071_value)
	StationObjectArray.append(Object_1071)
	#/1071
	
	#1072
	#1st Column
	TagPathNGA_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1072_value = system.tag.readBlocking([TagPathNGA_1072])[0].value
	StringA_1072 = format_quantity(TagNGA_1072_value)
	
	TagPathNGB_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NG Percent 1st"
	TagNGB_1072_value = system.tag.readBlocking([TagPathNGB_1072])[0].value
	StringB_1072 = format_value(TagNGB_1072_value)
	
	#2nd Column
	TagPathNGC_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1072_value = system.tag.readBlocking([TagPathNGC_1072])[0].value
	StringC_1072 = format_quantity(TagNGC_1072_value)
	
	TagPathNGD_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NG Percent 2nd"
	TagNGD_1072_value = system.tag.readBlocking([TagPathNGD_1072])[0].value
	StringD_1072 = format_value(TagNGD_1072_value)
	
	#3rd Column
	TagPathNGE_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1072_value = system.tag.readBlocking([TagPathNGE_1072])[0].value
	StringE_1072 = format_quantity(TagNGE_1072_value)
	
	TagPathNGF_1072 = "SourceA/Block A/Station 1072/Data/Dashboard/NG Percent 3rd"
	TagNGF_1072_value = system.tag.readBlocking([TagPathNGF_1072])[0].value
	StringF_1072 = format_value(TagNGF_1072_value)
	
	#Adding 1072 To Object Array
	Object_1072 = StationObject("1072", TagNGA_1072_value, TagNGB_1072_value, TagNGC_1072_value, TagNGD_1072_value, TagNGE_1072_value, TagNGF_1072_value)
	StationObjectArray.append(Object_1072)
	#/1072
	
	#1080
	#1st Column
	TagPathNGA_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1080_value = system.tag.readBlocking([TagPathNGA_1080])[0].value
	StringA_1080 = format_quantity(TagNGA_1080_value)
	
	TagPathNGB_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NG Percent 1st"
	TagNGB_1080_value = system.tag.readBlocking([TagPathNGB_1080])[0].value
	StringB_1080 = format_value(TagNGB_1080_value)
	
	#2nd Column
	TagPathNGC_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1080_value = system.tag.readBlocking([TagPathNGC_1080])[0].value
	StringC_1080 = format_quantity(TagNGC_1080_value)
	
	TagPathNGD_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NG Percent 2nd"
	TagNGD_1080_value = system.tag.readBlocking([TagPathNGD_1080])[0].value
	StringD_1080 = format_value(TagNGD_1080_value)
	
	#3rd Column
	TagPathNGE_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1080_value = system.tag.readBlocking([TagPathNGE_1080])[0].value
	StringE_1080 = format_quantity(TagNGE_1080_value)
	
	TagPathNGF_1080 = "SourceA/Block A/Station 1080/Data/Dashboard/NG Percent 3rd"
	TagNGF_1080_value = system.tag.readBlocking([TagPathNGF_1080])[0].value
	StringF_1080 = format_value(TagNGF_1080_value)
	
	#Adding 1080 To Object Array
	Object_1080 = StationObject("1080", TagNGA_1080_value, TagNGB_1080_value, TagNGC_1080_value, TagNGD_1080_value, TagNGE_1080_value, TagNGF_1080_value)
	StationObjectArray.append(Object_1080)
	#/1080
	#/Block A
	
	
	#Block B
	#1100
	#1st Column
	TagPathNGA_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1100_value = system.tag.readBlocking([TagPathNGA_1100])[0].value
	StringA_1100 = format_quantity(TagNGA_1100_value)
	
	TagPathNGB_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NG Percent 1st"
	TagNGB_1100_value = system.tag.readBlocking([TagPathNGB_1100])[0].value
	StringB_1100 = format_value(TagNGB_1100_value)
	
	#2nd Column
	TagPathNGC_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1100_value = system.tag.readBlocking([TagPathNGC_1100])[0].value
	StringC_1100 = format_quantity(TagNGC_1100_value)
	
	TagPathNGD_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NG Percent 2nd"
	TagNGD_1100_value = system.tag.readBlocking([TagPathNGD_1100])[0].value
	StringD_1100 = format_value(TagNGD_1100_value)
	
	#3rd Column
	TagPathNGE_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1100_value = system.tag.readBlocking([TagPathNGE_1100])[0].value
	StringE_1100 = format_quantity(TagNGE_1100_value)
	
	TagPathNGF_1100 = "SourceA/Block B/Station 1100/Data/Dashboard/NG Percent 3rd"
	TagNGF_1100_value = system.tag.readBlocking([TagPathNGF_1100])[0].value
	StringF_1100 = format_value(TagNGF_1100_value)
	
	#Adding 1100 To Object Array
	Object_1100 = StationObject("1100", TagNGA_1100_value, TagNGB_1100_value, TagNGC_1100_value, TagNGD_1100_value, TagNGE_1100_value, TagNGF_1100_value)
	StationObjectArray.append(Object_1100)
	#/1100
	
	#1101
	#1st Column
	TagPathNGA_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1101_value = system.tag.readBlocking([TagPathNGA_1101])[0].value
	StringA_1101 = format_quantity(TagNGA_1101_value)
	
	TagPathNGB_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NG Percent 1st"
	TagNGB_1101_value = system.tag.readBlocking([TagPathNGB_1101])[0].value
	StringB_1101 = format_value(TagNGB_1101_value)
	
	#2nd Column
	TagPathNGC_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1101_value = system.tag.readBlocking([TagPathNGC_1101])[0].value
	StringC_1101 = format_quantity(TagNGC_1101_value)
	
	TagPathNGD_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NG Percent 2nd"
	TagNGD_1101_value = system.tag.readBlocking([TagPathNGD_1101])[0].value
	StringD_1101 = format_value(TagNGD_1101_value)
	
	#3rd Column
	TagPathNGE_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1101_value = system.tag.readBlocking([TagPathNGE_1101])[0].value
	StringE_1101 = format_quantity(TagNGE_1101_value)
	
	TagPathNGF_1101 = "SourceA/Block B/Station 1101/Data/Dashboard/NG Percent 3rd"
	TagNGF_1101_value = system.tag.readBlocking([TagPathNGF_1101])[0].value
	StringF_1101 = format_value(TagNGF_1101_value)
	
	#Adding 1101 To Object Array
	#Object_1101 = StationObject("1101", TagNGA_1101_value, TagNGB_1101_value, TagNGC_1101_value, TagNGD_1101_value, TagNGE_1101_value, TagNGF_1101_value)
	#StationObjectArray.append(Object_1101)
	#/1101
	
	#1110
	#1st Column
	TagPathNGA_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1110_value = system.tag.readBlocking([TagPathNGA_1110])[0].value
	StringA_1110 = format_quantity(TagNGA_1110_value)
	
	TagPathNGB_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NG Percent 1st"
	TagNGB_1110_value = system.tag.readBlocking([TagPathNGB_1110])[0].value
	StringB_1110 = format_value(TagNGB_1110_value)
	
	#2nd Column
	TagPathNGC_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1110_value = system.tag.readBlocking([TagPathNGC_1110])[0].value
	StringC_1110 = format_quantity(TagNGC_1110_value)
	
	TagPathNGD_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NG Percent 2nd"
	TagNGD_1110_value = system.tag.readBlocking([TagPathNGD_1110])[0].value
	StringD_1110 = format_value(TagNGD_1110_value)
	
	#3rd Column
	TagPathNGE_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1110_value = system.tag.readBlocking([TagPathNGE_1110])[0].value
	StringE_1110 = format_quantity(TagNGE_1110_value)
	
	TagPathNGF_1110 = "SourceA/Block B/Station 1110/Data/Dashboard/NG Percent 3rd"
	TagNGF_1110_value = system.tag.readBlocking([TagPathNGF_1110])[0].value
	StringF_1110 = format_value(TagNGF_1110_value)
	
	#Adding 1110 To Object Array
	Object_1110 = StationObject("1110", TagNGA_1110_value, TagNGB_1110_value, TagNGC_1110_value, TagNGD_1110_value, TagNGE_1110_value, TagNGF_1110_value)
	StationObjectArray.append(Object_1110)
	#/1110
	
	#1120
	#1st Column
	TagPathNGA_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1120_value = system.tag.readBlocking([TagPathNGA_1120])[0].value
	StringA_1120 = format_quantity(TagNGA_1120_value)
	
	TagPathNGB_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NG Percent 1st"
	TagNGB_1120_value = system.tag.readBlocking([TagPathNGB_1120])[0].value
	StringB_1120 = format_value(TagNGB_1120_value)
	
	#2nd Column
	TagPathNGC_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1120_value = system.tag.readBlocking([TagPathNGC_1120])[0].value
	StringC_1120 = format_quantity(TagNGC_1120_value)
	
	TagPathNGD_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NG Percent 2nd"
	TagNGD_1120_value = system.tag.readBlocking([TagPathNGD_1120])[0].value
	StringD_1120 = format_value(TagNGD_1120_value)
	
	#3rd Column
	TagPathNGE_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1120_value = system.tag.readBlocking([TagPathNGE_1120])[0].value
	StringE_1120 = format_quantity(TagNGE_1120_value)
	
	TagPathNGF_1120 = "SourceA/Block B/Station 1120/Data/Dashboard/NG Percent 3rd"
	TagNGF_1120_value = system.tag.readBlocking([TagPathNGF_1120])[0].value
	StringF_1120 = format_value(TagNGF_1120_value)
	
	#Adding 1120 To Object Array
	Object_1120 = StationObject("1120", TagNGA_1120_value, TagNGB_1120_value, TagNGC_1120_value, TagNGD_1120_value, TagNGE_1120_value, TagNGF_1120_value)
	StationObjectArray.append(Object_1120)
	#/1120
	
	#1500
	#1st Column
	TagPathNGA_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1500_value = system.tag.readBlocking([TagPathNGA_1500])[0].value
	StringA_1500 = format_quantity(TagNGA_1500_value)
	
	TagPathNGB_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NG Percent 1st"
	TagNGB_1500_value = system.tag.readBlocking([TagPathNGB_1500])[0].value
	StringB_1500 = format_value(TagNGB_1500_value)
	
	#2nd Column
	TagPathNGC_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1500_value = system.tag.readBlocking([TagPathNGC_1500])[0].value
	StringC_1500 = format_quantity(TagNGC_1500_value)
	
	TagPathNGD_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NG Percent 2nd"
	TagNGD_1500_value = system.tag.readBlocking([TagPathNGD_1500])[0].value
	StringD_1500 = format_value(TagNGD_1500_value)
	
	#3rd Column
	TagPathNGE_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1500_value = system.tag.readBlocking([TagPathNGE_1500])[0].value
	StringE_1500 = format_quantity(TagNGE_1500_value)
	
	TagPathNGF_1500 = "SourceA/Block B/Station 1500/Data/Dashboard/NG Percent 3rd"
	TagNGF_1500_value = system.tag.readBlocking([TagPathNGF_1500])[0].value
	StringF_1500 = format_value(TagNGF_1500_value)
	
	#Adding 1500 To Object Array
	Object_1500 = StationObject("1500", TagNGA_1500_value, TagNGB_1500_value, TagNGC_1500_value, TagNGD_1500_value, TagNGE_1500_value, TagNGF_1500_value)
	StationObjectArray.append(Object_1500)
	#/1500
	
	
	
	#1510
	#1st Column
	TagPathNGA_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1510_value = system.tag.readBlocking([TagPathNGA_1510])[0].value
	StringA_1510 = format_quantity(TagNGA_1510_value)
	
	TagPathNGB_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NG Percent 1st"
	TagNGB_1510_value = system.tag.readBlocking([TagPathNGB_1510])[0].value
	StringB_1510 = format_value(TagNGB_1510_value)
	
	#2nd Column
	TagPathNGC_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1510_value = system.tag.readBlocking([TagPathNGC_1510])[0].value
	StringC_1510 = format_quantity(TagNGC_1510_value)
	
	TagPathNGD_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NG Percent 2nd"
	TagNGD_1510_value = system.tag.readBlocking([TagPathNGD_1510])[0].value
	StringD_1510 = format_value(TagNGD_1510_value)
	
	#3rd Column
	TagPathNGE_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1510_value = system.tag.readBlocking([TagPathNGE_1510])[0].value
	StringE_1510 = format_quantity(TagNGE_1510_value)
	
	TagPathNGF_1510 = "SourceA/Block B/Station 1510/Data/Dashboard/NG Percent 3rd"
	TagNGF_1510_value = system.tag.readBlocking([TagPathNGF_1510])[0].value
	StringF_1510 = format_value(TagNGF_1510_value)
	
	#Adding 1510 To Object Array
	Object_1510 = StationObject("1510", TagNGA_1510_value, TagNGB_1510_value, TagNGC_1510_value, TagNGD_1510_value, TagNGE_1510_value, TagNGF_1510_value)
	StationObjectArray.append(Object_1510)
	#/1510
	
	#1530
	#1st Column
	TagPathNGA_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1530_value = system.tag.readBlocking([TagPathNGA_1530])[0].value
	StringA_1530 = format_quantity(TagNGA_1530_value)
	
	TagPathNGB_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NG Percent 1st"
	TagNGB_1530_value = system.tag.readBlocking([TagPathNGB_1530])[0].value
	StringB_1530 = format_value(TagNGB_1530_value)
	
	#2nd Column
	TagPathNGC_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1530_value = system.tag.readBlocking([TagPathNGC_1530])[0].value
	StringC_1530 = format_quantity(TagNGC_1530_value)
	
	TagPathNGD_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NG Percent 2nd"
	TagNGD_1530_value = system.tag.readBlocking([TagPathNGD_1530])[0].value
	StringD_1530 = format_value(TagNGD_1530_value)
	
	#3rd Column
	TagPathNGE_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1530_value = system.tag.readBlocking([TagPathNGE_1530])[0].value
	StringE_1530 = format_quantity(TagNGE_1530_value)
	
	TagPathNGF_1530 = "SourceA/Block B/Station 1530/Data/Dashboard/NG Percent 3rd"
	TagNGF_1530_value = system.tag.readBlocking([TagPathNGF_1530])[0].value
	StringF_1530 = format_value(TagNGF_1530_value)
	
	#Adding 1530 To Object Array
	Object_1530 = StationObject("1530", TagNGA_1530_value, TagNGB_1530_value, TagNGC_1530_value, TagNGD_1530_value, TagNGE_1530_value, TagNGF_1530_value)
	StationObjectArray.append(Object_1530)
	#/1530
	
	#1140
	#1st Column
	TagPathNGA_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1140_value = system.tag.readBlocking([TagPathNGA_1140])[0].value
	StringA_1140 = format_quantity(TagNGA_1140_value)
	
	TagPathNGB_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NG Percent 1st"
	TagNGB_1140_value = system.tag.readBlocking([TagPathNGB_1140])[0].value
	StringB_1140 = format_value(TagNGB_1140_value)
	
	#2nd Column
	TagPathNGC_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1140_value = system.tag.readBlocking([TagPathNGC_1140])[0].value
	StringC_1140 = format_quantity(TagNGC_1140_value)
	
	TagPathNGD_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NG Percent 2nd"
	TagNGD_1140_value = system.tag.readBlocking([TagPathNGD_1140])[0].value
	StringD_1140 = format_value(TagNGD_1140_value)
	
	#3rd Column
	TagPathNGE_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1140_value = system.tag.readBlocking([TagPathNGE_1140])[0].value
	StringE_1140 = format_quantity(TagNGE_1140_value)
	
	TagPathNGF_1140 = "SourceA/Block B/Station 1140/Data/Dashboard/NG Percent 3rd"
	TagNGF_1140_value = system.tag.readBlocking([TagPathNGF_1140])[0].value
	StringF_1140 = format_value(TagNGF_1140_value)
	
	#Adding 1140 To Object Array
	Object_1140 = StationObject("1140", TagNGA_1140_value, TagNGB_1140_value, TagNGC_1140_value, TagNGD_1140_value, TagNGE_1140_value, TagNGF_1140_value)
	StationObjectArray.append(Object_1140)
	#/1140
	
	#1142
	#1st Column
	TagPathNGA_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1142_value = system.tag.readBlocking([TagPathNGA_1142])[0].value
	StringA_1142 = format_quantity(TagNGA_1142_value)
	
	TagPathNGB_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NG Percent 1st"
	TagNGB_1142_value = system.tag.readBlocking([TagPathNGB_1142])[0].value
	StringB_1142 = format_value(TagNGB_1142_value)
	
	#2nd Column
	TagPathNGC_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1142_value = system.tag.readBlocking([TagPathNGC_1142])[0].value
	StringC_1142 = format_quantity(TagNGC_1142_value)
	
	TagPathNGD_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NG Percent 2nd"
	TagNGD_1142_value = system.tag.readBlocking([TagPathNGD_1142])[0].value
	StringD_1142 = format_value(TagNGD_1142_value)
	
	#3rd Column
	TagPathNGE_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1142_value = system.tag.readBlocking([TagPathNGE_1142])[0].value
	StringE_1142 = format_quantity(TagNGE_1142_value)
	
	TagPathNGF_1142 = "SourceA/Block B/Station 1142/Data/Dashboard/NG Percent 3rd"
	TagNGF_1142_value = system.tag.readBlocking([TagPathNGF_1142])[0].value
	StringF_1142 = format_value(TagNGF_1142_value)
	
	#Adding 1142 To Object Array
	Object_1142 = StationObject("1142", TagNGA_1142_value, TagNGB_1142_value, TagNGC_1142_value, TagNGD_1142_value, TagNGE_1142_value, TagNGF_1142_value)
	StationObjectArray.append(Object_1142)
	#/1142
	
	#1150
	#1st Column
	TagPathNGA_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1150_value = system.tag.readBlocking([TagPathNGA_1150])[0].value
	StringA_1150 = format_quantity(TagNGA_1150_value)
	
	TagPathNGB_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NG Percent 1st"
	TagNGB_1150_value = system.tag.readBlocking([TagPathNGB_1150])[0].value
	StringB_1150 = format_value(TagNGB_1150_value)
	
	#2nd Column
	TagPathNGC_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1150_value = system.tag.readBlocking([TagPathNGC_1150])[0].value
	StringC_1150 = format_quantity(TagNGC_1150_value)
	
	TagPathNGD_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NG Percent 2nd"
	TagNGD_1150_value = system.tag.readBlocking([TagPathNGD_1150])[0].value
	StringD_1150 = format_value(TagNGD_1150_value)
	
	#3rd Column
	TagPathNGE_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1150_value = system.tag.readBlocking([TagPathNGE_1150])[0].value
	StringE_1150 = format_quantity(TagNGE_1150_value)
	
	TagPathNGF_1150 = "SourceA/Block B/Station 1150/Data/Dashboard/NG Percent 3rd"
	TagNGF_1150_value = system.tag.readBlocking([TagPathNGF_1150])[0].value
	StringF_1150 = format_value(TagNGF_1150_value)
	
	#Adding 1150 To Object Array
	Object_1150 = StationObject("1150", TagNGA_1150_value, TagNGB_1150_value, TagNGC_1150_value, TagNGD_1150_value, TagNGE_1150_value, TagNGF_1150_value)
	StationObjectArray.append(Object_1150)
	#/1150
	
	#1160
	#1st Column
	TagPathNGA_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1160_value = system.tag.readBlocking([TagPathNGA_1160])[0].value
	StringA_1160 = format_quantity(TagNGA_1160_value)
	
	TagPathNGB_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NG Percent 1st"
	TagNGB_1160_value = system.tag.readBlocking([TagPathNGB_1160])[0].value
	StringB_1160 = format_value(TagNGB_1160_value)
	
	#2nd Column
	TagPathNGC_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1160_value = system.tag.readBlocking([TagPathNGC_1160])[0].value
	StringC_1160 = format_quantity(TagNGC_1160_value)
	
	TagPathNGD_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NG Percent 2nd"
	TagNGD_1160_value = system.tag.readBlocking([TagPathNGD_1160])[0].value
	StringD_1160 = format_value(TagNGD_1160_value)
	
	#3rd Column
	TagPathNGE_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1160_value = system.tag.readBlocking([TagPathNGE_1160])[0].value
	StringE_1160 = format_quantity(TagNGE_1160_value)
	
	TagPathNGF_1160 = "SourceA/Block B/Station 1160/Data/Dashboard/NG Percent 3rd"
	TagNGF_1160_value = system.tag.readBlocking([TagPathNGF_1160])[0].value
	StringF_1160 = format_value(TagNGF_1160_value)
	
	#Adding 1160 To Object Array
	Object_1160 = StationObject("1160", TagNGA_1160_value, TagNGB_1160_value, TagNGC_1160_value, TagNGD_1160_value, TagNGE_1160_value, TagNGF_1160_value)
	StationObjectArray.append(Object_1160)
	#/1160
	
	#1161
	#1st Column
	TagPathNGA_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1161_value = system.tag.readBlocking([TagPathNGA_1161])[0].value
	StringA_1161 = format_quantity(TagNGA_1161_value)
	
	TagPathNGB_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NG Percent 1st"
	TagNGB_1161_value = system.tag.readBlocking([TagPathNGB_1161])[0].value
	StringB_1161 = format_value(TagNGB_1161_value)
	
	#2nd Column
	TagPathNGC_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1161_value = system.tag.readBlocking([TagPathNGC_1161])[0].value
	StringC_1161 = format_quantity(TagNGC_1161_value)
	
	TagPathNGD_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NG Percent 2nd"
	TagNGD_1161_value = system.tag.readBlocking([TagPathNGD_1161])[0].value
	StringD_1161 = format_value(TagNGD_1161_value)
	
	#3rd Column
	TagPathNGE_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1161_value = system.tag.readBlocking([TagPathNGE_1161])[0].value
	StringE_1161 = format_quantity(TagNGE_1161_value)
	
	TagPathNGF_1161 = "SourceA/Block B/Station 1161/Data/Dashboard/NG Percent 3rd"
	TagNGF_1161_value = system.tag.readBlocking([TagPathNGF_1161])[0].value
	StringF_1161 = format_value(TagNGF_1161_value)
	
	#Adding 1161 To Object Array
	Object_1161 = StationObject("1161", TagNGA_1161_value, TagNGB_1161_value, TagNGC_1161_value, TagNGD_1161_value, TagNGE_1161_value, TagNGF_1161_value)
	StationObjectArray.append(Object_1161)
	#/1161
	
	#1170
	#1st Column
	TagPathNGA_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1170_value = system.tag.readBlocking([TagPathNGA_1170])[0].value
	StringA_1170 = format_quantity(TagNGA_1170_value)
	
	TagPathNGB_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NG Percent 1st"
	TagNGB_1170_value = system.tag.readBlocking([TagPathNGB_1170])[0].value
	StringB_1170 = format_value(TagNGB_1170_value)
	
	#2nd Column
	TagPathNGC_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1170_value = system.tag.readBlocking([TagPathNGC_1170])[0].value
	StringC_1170 = format_quantity(TagNGC_1170_value)
	
	TagPathNGD_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NG Percent 2nd"
	TagNGD_1170_value = system.tag.readBlocking([TagPathNGD_1170])[0].value
	StringD_1170 = format_value(TagNGD_1170_value)
	
	#3rd Column
	TagPathNGE_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1170_value = system.tag.readBlocking([TagPathNGE_1170])[0].value
	StringE_1170 = format_quantity(TagNGE_1170_value)
	
	TagPathNGF_1170 = "SourceA/Block B/Station 1170/Data/Dashboard/NG Percent 3rd"
	TagNGF_1170_value = system.tag.readBlocking([TagPathNGF_1170])[0].value
	StringF_1170 = format_value(TagNGF_1170_value)
	
	#Adding 1170 To Object Array
	Object_1170 = StationObject("1170", TagNGA_1170_value, TagNGB_1170_value, TagNGC_1170_value, TagNGD_1170_value, TagNGE_1170_value, TagNGF_1170_value)
	StationObjectArray.append(Object_1170)
	#/1170
	#/Block B
	
	#Block C
	#1180
	#1st Column
	TagPathNGA_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1180_value = system.tag.readBlocking([TagPathNGA_1180])[0].value
	StringA_1180 = format_quantity(TagNGA_1180_value)
	
	TagPathNGB_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NG Percent 1st"
	TagNGB_1180_value = system.tag.readBlocking([TagPathNGB_1180])[0].value
	StringB_1180 = format_value(TagNGB_1180_value)
	
	#2nd Column
	TagPathNGC_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1180_value = system.tag.readBlocking([TagPathNGC_1180])[0].value
	StringC_1180 = format_quantity(TagNGC_1180_value)
	
	TagPathNGD_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NG Percent 2nd"
	TagNGD_1180_value = system.tag.readBlocking([TagPathNGD_1180])[0].value
	StringD_1180 = format_value(TagNGD_1180_value)
	
	#3rd Column
	TagPathNGE_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1180_value = system.tag.readBlocking([TagPathNGE_1180])[0].value
	StringE_1180 = format_quantity(TagNGE_1180_value)
	
	TagPathNGF_1180 = "SourceA/Block C/Station 1180/Data/Dashboard/NG Percent 3rd"
	TagNGF_1180_value = system.tag.readBlocking([TagPathNGF_1180])[0].value
	StringF_1180 = format_value(TagNGF_1180_value)
	
	#Adding 1180 To Object Array
	Object_1180 = StationObject("1180", TagNGA_1180_value, TagNGB_1180_value, TagNGC_1180_value, TagNGD_1180_value, TagNGE_1180_value, TagNGF_1180_value)
	StationObjectArray.append(Object_1180)
	#/1180
	
	#1200
	#1st Column
	TagPathNGA_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1200_value = system.tag.readBlocking([TagPathNGA_1200])[0].value
	StringA_1200 = format_quantity(TagNGA_1200_value)
	
	TagPathNGB_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NG Percent 1st"
	TagNGB_1200_value = system.tag.readBlocking([TagPathNGB_1200])[0].value
	StringB_1200 = format_value(TagNGB_1200_value)
	
	#2nd Column
	TagPathNGC_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1200_value = system.tag.readBlocking([TagPathNGC_1200])[0].value
	StringC_1200 = format_quantity(TagNGC_1200_value)
	
	TagPathNGD_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NG Percent 2nd"
	TagNGD_1200_value = system.tag.readBlocking([TagPathNGD_1200])[0].value
	StringD_1200 = format_value(TagNGD_1200_value)
	
	#3rd Column
	TagPathNGE_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1200_value = system.tag.readBlocking([TagPathNGE_1200])[0].value
	StringE_1200 = format_quantity(TagNGE_1200_value)
	
	TagPathNGF_1200 = "SourceA/Block C/Station 1200/Data/Dashboard/NG Percent 3rd"
	TagNGF_1200_value = system.tag.readBlocking([TagPathNGF_1200])[0].value
	StringF_1200 = format_value(TagNGF_1200_value)
	
	#Adding 1200 To Object Array
	Object_1200 = StationObject("1200", TagNGA_1200_value, TagNGB_1200_value, TagNGC_1200_value, TagNGD_1200_value, TagNGE_1200_value, TagNGF_1200_value)
	StationObjectArray.append(Object_1200)
	#/1200
	
	#1205
	#1st Column
	TagPathNGA_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1205_value = system.tag.readBlocking([TagPathNGA_1205])[0].value
	StringA_1205 = format_quantity(TagNGA_1205_value)
	
	TagPathNGB_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NG Percent 1st"
	TagNGB_1205_value = system.tag.readBlocking([TagPathNGB_1205])[0].value
	StringB_1205 = format_value(TagNGB_1205_value)
	
	#2nd Column
	TagPathNGC_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1205_value = system.tag.readBlocking([TagPathNGC_1205])[0].value
	StringC_1205 = format_quantity(TagNGC_1205_value)
	
	TagPathNGD_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NG Percent 2nd"
	TagNGD_1205_value = system.tag.readBlocking([TagPathNGD_1205])[0].value
	StringD_1205 = format_value(TagNGD_1205_value)
	
	#3rd Column
	TagPathNGE_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1205_value = system.tag.readBlocking([TagPathNGE_1205])[0].value
	StringE_1205 = format_quantity(TagNGE_1205_value)
	
	TagPathNGF_1205 = "SourceA/Block C/Station 1205/Data/Dashboard/NG Percent 3rd"
	TagNGF_1205_value = system.tag.readBlocking([TagPathNGF_1205])[0].value
	StringF_1205 = format_value(TagNGF_1205_value)
	
	#Adding 1205 To Object Array
	Object_1205 = StationObject("1205", TagNGA_1205_value, TagNGB_1205_value, TagNGC_1205_value, TagNGD_1205_value, TagNGE_1205_value, TagNGF_1205_value)
	StationObjectArray.append(Object_1205)
	#/1205
	
	#1210
	#1st Column
	TagPathNGA_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1210_value = system.tag.readBlocking([TagPathNGA_1210])[0].value
	StringA_1210 = format_quantity(TagNGA_1210_value)
	
	TagPathNGB_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NG Percent 1st"
	TagNGB_1210_value = system.tag.readBlocking([TagPathNGB_1210])[0].value
	StringB_1210 = format_value(TagNGB_1210_value)
	
	#2nd Column
	TagPathNGC_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1210_value = system.tag.readBlocking([TagPathNGC_1210])[0].value
	StringC_1210 = format_quantity(TagNGC_1210_value)
	
	TagPathNGD_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NG Percent 2nd"
	TagNGD_1210_value = system.tag.readBlocking([TagPathNGD_1210])[0].value
	StringD_1210 = format_value(TagNGD_1210_value)
	
	#3rd Column
	TagPathNGE_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1210_value = system.tag.readBlocking([TagPathNGE_1210])[0].value
	StringE_1210 = format_quantity(TagNGE_1210_value)
	
	TagPathNGF_1210 = "SourceA/Block C/Station 1210/Data/Dashboard/NG Percent 3rd"
	TagNGF_1210_value = system.tag.readBlocking([TagPathNGF_1210])[0].value
	StringF_1210 = format_value(TagNGF_1210_value)
	
	#Adding 1210 To Object Array
	Object_1210 = StationObject("1210", TagNGA_1210_value, TagNGB_1210_value, TagNGC_1210_value, TagNGD_1210_value, TagNGE_1210_value, TagNGF_1210_value)
	StationObjectArray.append(Object_1210)
	#/1210
	
	#1620
	#1st Column
	TagPathNGA_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1620_value = system.tag.readBlocking([TagPathNGA_1620])[0].value
	StringA_1620 = format_quantity(TagNGA_1620_value)
	
	TagPathNGB_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NG Percent 1st"
	TagNGB_1620_value = system.tag.readBlocking([TagPathNGB_1620])[0].value
	StringB_1620 = format_value(TagNGB_1620_value)
	
	#2nd Column
	TagPathNGC_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1620_value = system.tag.readBlocking([TagPathNGC_1620])[0].value
	StringC_1620 = format_quantity(TagNGC_1620_value)
	
	TagPathNGD_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NG Percent 2nd"
	TagNGD_1620_value = system.tag.readBlocking([TagPathNGD_1620])[0].value
	StringD_1620 = format_value(TagNGD_1620_value)
	
	#3rd Column
	TagPathNGE_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1620_value = system.tag.readBlocking([TagPathNGE_1620])[0].value
	StringE_1620 = format_quantity(TagNGE_1620_value)
	
	TagPathNGF_1620 = "SourceA/Block C/Station 1620/Data/Dashboard/NG Percent 3rd"
	TagNGF_1620_value = system.tag.readBlocking([TagPathNGF_1620])[0].value
	StringF_1620 = format_value(TagNGF_1620_value)
	
	#Adding 1620 To Object Array
	Object_1620 = StationObject("1620", TagNGA_1620_value, TagNGB_1620_value, TagNGC_1620_value, TagNGD_1620_value, TagNGE_1620_value, TagNGF_1620_value)
	StationObjectArray.append(Object_1620)
	#/1620
	
	#1630
	#1st Column
	TagPathNGA_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1630_value = system.tag.readBlocking([TagPathNGA_1630])[0].value
	StringA_1630 = format_quantity(TagNGA_1630_value)
	
	TagPathNGB_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NG Percent 1st"
	TagNGB_1630_value = system.tag.readBlocking([TagPathNGB_1630])[0].value
	StringB_1630 = format_value(TagNGB_1630_value)
	
	#2nd Column
	TagPathNGC_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1630_value = system.tag.readBlocking([TagPathNGC_1630])[0].value
	StringC_1630 = format_quantity(TagNGC_1630_value)
	
	TagPathNGD_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NG Percent 2nd"
	TagNGD_1630_value = system.tag.readBlocking([TagPathNGD_1630])[0].value
	StringD_1630 = format_value(TagNGD_1630_value)
	
	#3rd Column
	TagPathNGE_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1630_value = system.tag.readBlocking([TagPathNGE_1630])[0].value
	StringE_1630 = format_quantity(TagNGE_1630_value)
	
	TagPathNGF_1630 = "SourceA/Block C/Station 1630/Data/Dashboard/NG Percent 3rd"
	TagNGF_1630_value = system.tag.readBlocking([TagPathNGF_1630])[0].value
	StringF_1630 = format_value(TagNGF_1630_value)
	
	#Adding 1630 To Object Array
	Object_1630 = StationObject("1630", TagNGA_1630_value, TagNGB_1630_value, TagNGC_1630_value, TagNGD_1630_value, TagNGE_1630_value, TagNGF_1630_value)
	StationObjectArray.append(Object_1630)
	#/1630
	
	#1640
	#1st Column
	TagPathNGA_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1640_value = system.tag.readBlocking([TagPathNGA_1640])[0].value
	StringA_1640 = format_quantity(TagNGA_1640_value)
	
	TagPathNGB_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NG Percent 1st"
	TagNGB_1640_value = system.tag.readBlocking([TagPathNGB_1640])[0].value
	StringB_1640 = format_value(TagNGB_1640_value)
	
	#2nd Column
	TagPathNGC_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1640_value = system.tag.readBlocking([TagPathNGC_1640])[0].value
	StringC_1640 = format_quantity(TagNGC_1640_value)
	
	TagPathNGD_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NG Percent 2nd"
	TagNGD_1640_value = system.tag.readBlocking([TagPathNGD_1640])[0].value
	StringD_1640 = format_value(TagNGD_1640_value)
	
	#3rd Column
	TagPathNGE_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1640_value = system.tag.readBlocking([TagPathNGE_1640])[0].value
	StringE_1640 = format_quantity(TagNGE_1640_value)
	
	TagPathNGF_1640 = "SourceA/Block C/Station 1640/Data/Dashboard/NG Percent 3rd"
	TagNGF_1640_value = system.tag.readBlocking([TagPathNGF_1640])[0].value
	StringF_1640 = format_value(TagNGF_1640_value)
	
	#Adding 1640 To Object Array
	Object_1640 = StationObject("1640", TagNGA_1640_value, TagNGB_1640_value, TagNGC_1640_value, TagNGD_1640_value, TagNGE_1640_value, TagNGF_1640_value)
	StationObjectArray.append(Object_1640)
	#/1640
	
	#1650
	#1st Column
	TagPathNGA_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1650_value = system.tag.readBlocking([TagPathNGA_1650])[0].value
	StringA_1650 = format_quantity(TagNGA_1650_value)
	
	TagPathNGB_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NG Percent 1st"
	TagNGB_1650_value = system.tag.readBlocking([TagPathNGB_1650])[0].value
	StringB_1650 = format_value(TagNGB_1650_value)
	
	#2nd Column
	TagPathNGC_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1650_value = system.tag.readBlocking([TagPathNGC_1650])[0].value
	StringC_1650 = format_quantity(TagNGC_1650_value)
	
	TagPathNGD_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NG Percent 2nd"
	TagNGD_1650_value = system.tag.readBlocking([TagPathNGD_1650])[0].value
	StringD_1650 = format_value(TagNGD_1650_value)
	
	#3rd Column
	TagPathNGE_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1650_value = system.tag.readBlocking([TagPathNGE_1650])[0].value
	StringE_1650 = format_quantity(TagNGE_1650_value)
	
	TagPathNGF_1650 = "SourceA/Block C/Station 1650/Data/Dashboard/NG Percent 3rd"
	TagNGF_1650_value = system.tag.readBlocking([TagPathNGF_1650])[0].value
	StringF_1650 = format_value(TagNGF_1650_value)
	
	#Adding 1650 To Object Array
	Object_1650 = StationObject("1650", TagNGA_1650_value, TagNGB_1650_value, TagNGC_1650_value, TagNGD_1650_value, TagNGE_1650_value, TagNGF_1650_value)
	StationObjectArray.append(Object_1650)
	#/1650
	
	#1220
	#1st Column
	TagPathNGA_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1220_value = system.tag.readBlocking([TagPathNGA_1220])[0].value
	StringA_1220 = format_quantity(TagNGA_1220_value)
	
	TagPathNGB_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NG Percent 1st"
	TagNGB_1220_value = system.tag.readBlocking([TagPathNGB_1220])[0].value
	StringB_1220 = format_value(TagNGB_1220_value)
	
	#2nd Column
	TagPathNGC_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1220_value = system.tag.readBlocking([TagPathNGC_1220])[0].value
	StringC_1220 = format_quantity(TagNGC_1220_value)
	
	TagPathNGD_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NG Percent 2nd"
	TagNGD_1220_value = system.tag.readBlocking([TagPathNGD_1220])[0].value
	StringD_1220 = format_value(TagNGD_1220_value)
	
	#3rd Column
	TagPathNGE_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1220_value = system.tag.readBlocking([TagPathNGE_1220])[0].value
	StringE_1220 = format_quantity(TagNGE_1220_value)
	
	TagPathNGF_1220 = "SourceA/Block C/Station 1220/Data/Dashboard/NG Percent 3rd"
	TagNGF_1220_value = system.tag.readBlocking([TagPathNGF_1220])[0].value
	StringF_1220 = format_value(TagNGF_1220_value)
	
	#Adding 1220 To Object Array
	Object_1220 = StationObject("1220", TagNGA_1220_value, TagNGB_1220_value, TagNGC_1220_value, TagNGD_1220_value, TagNGE_1220_value, TagNGF_1220_value)
	StationObjectArray.append(Object_1220)
	#/1220
	
	#1230
	#1st Column
	TagPathNGA_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1230_value = system.tag.readBlocking([TagPathNGA_1230])[0].value
	StringA_1230 = format_quantity(TagNGA_1230_value)
	
	TagPathNGB_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NG Percent 1st"
	TagNGB_1230_value = system.tag.readBlocking([TagPathNGB_1230])[0].value
	StringB_1230 = format_value(TagNGB_1230_value)
	
	#2nd Column
	TagPathNGC_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1230_value = system.tag.readBlocking([TagPathNGC_1230])[0].value
	StringC_1230 = format_quantity(TagNGC_1230_value)
	
	TagPathNGD_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NG Percent 2nd"
	TagNGD_1230_value = system.tag.readBlocking([TagPathNGD_1230])[0].value
	StringD_1230 = format_value(TagNGD_1230_value)
	
	#3rd Column
	TagPathNGE_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1230_value = system.tag.readBlocking([TagPathNGE_1230])[0].value
	StringE_1230 = format_quantity(TagNGE_1230_value)
	
	TagPathNGF_1230 = "SourceA/Block C/Station 1230/Data/Dashboard/NG Percent 3rd"
	TagNGF_1230_value = system.tag.readBlocking([TagPathNGF_1230])[0].value
	StringF_1230 = format_value(TagNGF_1230_value)
	
	#Adding 1230 To Object Array
	Object_1230 = StationObject("1230", TagNGA_1230_value, TagNGB_1230_value, TagNGC_1230_value, TagNGD_1230_value, TagNGE_1230_value, TagNGF_1230_value)
	StationObjectArray.append(Object_1230)
	#/1230
	
	#1240
	#1st Column
	TagPathNGA_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1240_value = system.tag.readBlocking([TagPathNGA_1240])[0].value
	StringA_1240 = format_quantity(TagNGA_1240_value)
	
	TagPathNGB_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NG Percent 1st"
	TagNGB_1240_value = system.tag.readBlocking([TagPathNGB_1240])[0].value
	StringB_1240 = format_value(TagNGB_1240_value)
	
	#2nd Column
	TagPathNGC_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1240_value = system.tag.readBlocking([TagPathNGC_1240])[0].value
	StringC_1240 = format_quantity(TagNGC_1240_value)
	
	TagPathNGD_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NG Percent 2nd"
	TagNGD_1240_value = system.tag.readBlocking([TagPathNGD_1240])[0].value
	StringD_1240 = format_value(TagNGD_1240_value)
	
	#3rd Column
	TagPathNGE_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1240_value = system.tag.readBlocking([TagPathNGE_1240])[0].value
	StringE_1240 = format_quantity(TagNGE_1240_value)
	
	TagPathNGF_1240 = "SourceA/Block C/Station 1240/Data/Dashboard/NG Percent 3rd"
	TagNGF_1240_value = system.tag.readBlocking([TagPathNGF_1240])[0].value
	StringF_1240 = format_value(TagNGF_1240_value)
	
	#Adding 1240 To Object Array
	Object_1240 = StationObject("1240", TagNGA_1240_value, TagNGB_1240_value, TagNGC_1240_value, TagNGD_1240_value, TagNGE_1240_value, TagNGF_1240_value)
	StationObjectArray.append(Object_1240)
	#/1240
	
	#1241
	#1st Column
	TagPathNGA_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1241_value = system.tag.readBlocking([TagPathNGA_1241])[0].value
	StringA_1241 = format_quantity(TagNGA_1241_value)
	
	TagPathNGB_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NG Percent 1st"
	TagNGB_1241_value = system.tag.readBlocking([TagPathNGB_1241])[0].value
	StringB_1241 = format_value(TagNGB_1241_value)
	
	#2nd Column
	TagPathNGC_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1241_value = system.tag.readBlocking([TagPathNGC_1241])[0].value
	StringC_1241 = format_quantity(TagNGC_1241_value)
	
	TagPathNGD_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NG Percent 2nd"
	TagNGD_1241_value = system.tag.readBlocking([TagPathNGD_1241])[0].value
	StringD_1241 = format_value(TagNGD_1241_value)
	
	#3rd Column
	TagPathNGE_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1241_value = system.tag.readBlocking([TagPathNGE_1241])[0].value
	StringE_1241 = format_quantity(TagNGE_1241_value)
	
	TagPathNGF_1241 = "SourceA/Block C/Station 1241/Data/Dashboard/NG Percent 3rd"
	TagNGF_1241_value = system.tag.readBlocking([TagPathNGF_1241])[0].value
	StringF_1241 = format_value(TagNGF_1241_value)
	
	#Adding 1241 To Object Array
	Object_1241 = StationObject("1241", TagNGA_1241_value, TagNGB_1241_value, TagNGC_1241_value, TagNGD_1241_value, TagNGE_1241_value, TagNGF_1241_value)
	StationObjectArray.append(Object_1241)
	#/1241
	
	#1245
	#1st Column
	TagPathNGA_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1245_value = system.tag.readBlocking([TagPathNGA_1245])[0].value
	StringA_1245 = format_quantity(TagNGA_1245_value)
	
	TagPathNGB_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NG Percent 1st"
	TagNGB_1245_value = system.tag.readBlocking([TagPathNGB_1245])[0].value
	StringB_1245 = format_value(TagNGB_1245_value)
	
	#2nd Column
	TagPathNGC_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1245_value = system.tag.readBlocking([TagPathNGC_1245])[0].value
	StringC_1245 = format_quantity(TagNGC_1245_value)
	
	TagPathNGD_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NG Percent 2nd"
	TagNGD_1245_value = system.tag.readBlocking([TagPathNGD_1245])[0].value
	StringD_1245 = format_value(TagNGD_1245_value)
	
	#3rd Column
	TagPathNGE_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1245_value = system.tag.readBlocking([TagPathNGE_1245])[0].value
	StringE_1245 = format_quantity(TagNGE_1245_value)
	
	TagPathNGF_1245 = "SourceA/Block C/Station 1245/Data/Dashboard/NG Percent 3rd"
	TagNGF_1245_value = system.tag.readBlocking([TagPathNGF_1245])[0].value
	StringF_1245 = format_value(TagNGF_1245_value)
	
	#Adding 1245 To Object Array
	Object_1245 = StationObject("1245", TagNGA_1245_value, TagNGB_1245_value, TagNGC_1245_value, TagNGD_1245_value, TagNGE_1245_value, TagNGF_1245_value)
	StationObjectArray.append(Object_1245)
	#/1245
	
	#1260
	#1st Column
	TagPathNGA_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1260_value = system.tag.readBlocking([TagPathNGA_1260])[0].value
	StringA_1260 = format_quantity(TagNGA_1260_value)
	
	TagPathNGB_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NG Percent 1st"
	TagNGB_1260_value = system.tag.readBlocking([TagPathNGB_1260])[0].value
	StringB_1260 = format_value(TagNGB_1260_value)
	
	#2nd Column
	TagPathNGC_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1260_value = system.tag.readBlocking([TagPathNGC_1260])[0].value
	StringC_1260 = format_quantity(TagNGC_1260_value)
	
	TagPathNGD_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NG Percent 2nd"
	TagNGD_1260_value = system.tag.readBlocking([TagPathNGD_1260])[0].value
	StringD_1260 = format_value(TagNGD_1260_value)
	
	#3rd Column
	TagPathNGE_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1260_value = system.tag.readBlocking([TagPathNGE_1260])[0].value
	StringE_1260 = format_quantity(TagNGE_1260_value)
	
	TagPathNGF_1260 = "SourceA/Block C/Station 1260/Data/Dashboard/NG Percent 3rd"
	TagNGF_1260_value = system.tag.readBlocking([TagPathNGF_1260])[0].value
	StringF_1260 = format_value(TagNGF_1260_value)
	
	#Adding 1260 To Object Array
	Object_1260 = StationObject("1260", TagNGA_1260_value, TagNGB_1260_value, TagNGC_1260_value, TagNGD_1260_value, TagNGE_1260_value, TagNGF_1260_value)
	StationObjectArray.append(Object_1260)
	#/1260
	#/Block C
	
	
	#Block D
	#1300
	#1st Column
	TagPathNGA_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1300_value = system.tag.readBlocking([TagPathNGA_1300])[0].value
	StringA_1300 = format_quantity(TagNGA_1300_value)
	
	TagPathNGB_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NG Percent 1st"
	TagNGB_1300_value = system.tag.readBlocking([TagPathNGB_1300])[0].value
	StringB_1300 = format_value(TagNGB_1300_value)
	
	#2nd Column
	TagPathNGC_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1300_value = system.tag.readBlocking([TagPathNGC_1300])[0].value
	StringC_1300 = format_quantity(TagNGC_1300_value)
	
	TagPathNGD_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NG Percent 2nd"
	TagNGD_1300_value = system.tag.readBlocking([TagPathNGD_1300])[0].value
	StringD_1300 = format_value(TagNGD_1300_value)
	
	#3rd Column
	TagPathNGE_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1300_value = system.tag.readBlocking([TagPathNGE_1300])[0].value
	StringE_1300 = format_quantity(TagNGE_1300_value)
	
	TagPathNGF_1300 = "SourceA/Block D/Station 1300/Data/Dashboard/NG Percent 3rd"
	TagNGF_1300_value = system.tag.readBlocking([TagPathNGF_1300])[0].value
	StringF_1300 = format_value(TagNGF_1300_value)
	
	#Adding 1300 To Object Array
	Object_1300 = StationObject("1300", TagNGA_1300_value, TagNGB_1300_value, TagNGC_1300_value, TagNGD_1300_value, TagNGE_1300_value, TagNGF_1300_value)
	StationObjectArray.append(Object_1300)
	#/1300
	
	#1310
	#1st Column
	TagPathNGA_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1310_value = system.tag.readBlocking([TagPathNGA_1310])[0].value
	StringA_1310 = format_quantity(TagNGA_1310_value)
	
	TagPathNGB_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NG Percent 1st"
	TagNGB_1310_value = system.tag.readBlocking([TagPathNGB_1310])[0].value
	StringB_1310 = format_value(TagNGB_1310_value)
	
	#2nd Column
	TagPathNGC_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1310_value = system.tag.readBlocking([TagPathNGC_1310])[0].value
	StringC_1310 = format_quantity(TagNGC_1310_value)
	
	TagPathNGD_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NG Percent 2nd"
	TagNGD_1310_value = system.tag.readBlocking([TagPathNGD_1310])[0].value
	StringD_1310 = format_value(TagNGD_1310_value)
	
	#3rd Column
	TagPathNGE_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1310_value = system.tag.readBlocking([TagPathNGE_1310])[0].value
	StringE_1310 = format_quantity(TagNGE_1310_value)
	
	TagPathNGF_1310 = "SourceA/Block D/Station 1310/Data/Dashboard/NG Percent 3rd"
	TagNGF_1310_value = system.tag.readBlocking([TagPathNGF_1310])[0].value
	StringF_1310 = format_value(TagNGF_1310_value)
	
	#Adding 1310 To Object Array
	Object_1310 = StationObject("1310", TagNGA_1310_value, TagNGB_1310_value, TagNGC_1310_value, TagNGD_1310_value, TagNGE_1310_value, TagNGF_1310_value)
	StationObjectArray.append(Object_1310)
	#/1310
	
	#1320
	#1st Column
	TagPathNGA_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1320_value = system.tag.readBlocking([TagPathNGA_1320])[0].value
	StringA_1320 = format_quantity(TagNGA_1320_value)
	
	TagPathNGB_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NG Percent 1st"
	TagNGB_1320_value = system.tag.readBlocking([TagPathNGB_1320])[0].value
	StringB_1320 = format_value(TagNGB_1320_value)
	
	#2nd Column
	TagPathNGC_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1320_value = system.tag.readBlocking([TagPathNGC_1320])[0].value
	StringC_1320 = format_quantity(TagNGC_1320_value)
	
	TagPathNGD_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NG Percent 2nd"
	TagNGD_1320_value = system.tag.readBlocking([TagPathNGD_1320])[0].value
	StringD_1320 = format_value(TagNGD_1320_value)
	
	#3rd Column
	TagPathNGE_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1320_value = system.tag.readBlocking([TagPathNGE_1320])[0].value
	StringE_1320 = format_quantity(TagNGE_1320_value)
	
	TagPathNGF_1320 = "SourceA/Block D/Station 1320/Data/Dashboard/NG Percent 3rd"
	TagNGF_1320_value = system.tag.readBlocking([TagPathNGF_1320])[0].value
	StringF_1320 = format_value(TagNGF_1320_value)
	
	#Adding 1320 To Object Array
	Object_1320 = StationObject("1320", TagNGA_1320_value, TagNGB_1320_value, TagNGC_1320_value, TagNGD_1320_value, TagNGE_1320_value, TagNGF_1320_value)
	StationObjectArray.append(Object_1320)
	#/1320
	
	#1720
	#1st Column
	TagPathNGA_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1720_value = system.tag.readBlocking([TagPathNGA_1720])[0].value
	StringA_1720 = format_quantity(TagNGA_1720_value)
	
	TagPathNGB_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NG Percent 1st"
	TagNGB_1720_value = system.tag.readBlocking([TagPathNGB_1720])[0].value
	StringB_1720 = format_value(TagNGB_1720_value)
	
	#2nd Column
	TagPathNGC_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1720_value = system.tag.readBlocking([TagPathNGC_1720])[0].value
	StringC_1720 = format_quantity(TagNGC_1720_value)
	
	TagPathNGD_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NG Percent 2nd"
	TagNGD_1720_value = system.tag.readBlocking([TagPathNGD_1720])[0].value
	StringD_1720 = format_value(TagNGD_1720_value)
	
	#3rd Column
	TagPathNGE_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1720_value = system.tag.readBlocking([TagPathNGE_1720])[0].value
	StringE_1720 = format_quantity(TagNGE_1720_value)
	
	TagPathNGF_1720 = "SourceA/Block D/Station 1720/Data/Dashboard/NG Percent 3rd"
	TagNGF_1720_value = system.tag.readBlocking([TagPathNGF_1720])[0].value
	StringF_1720 = format_value(TagNGF_1720_value)
	
	#Adding 1720 To Object Array
	Object_1720 = StationObject("1720", TagNGA_1720_value, TagNGB_1720_value, TagNGC_1720_value, TagNGD_1720_value, TagNGE_1720_value, TagNGF_1720_value)
	StationObjectArray.append(Object_1720)
	#/1720
	
	#1730
	#1st Column
	TagPathNGA_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1730_value = system.tag.readBlocking([TagPathNGA_1730])[0].value
	StringA_1730 = format_quantity(TagNGA_1730_value)
	
	TagPathNGB_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NG Percent 1st"
	TagNGB_1730_value = system.tag.readBlocking([TagPathNGB_1730])[0].value
	StringB_1730 = format_value(TagNGB_1730_value)
	
	#2nd Column
	TagPathNGC_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1730_value = system.tag.readBlocking([TagPathNGC_1730])[0].value
	StringC_1730 = format_quantity(TagNGC_1730_value)
	
	TagPathNGD_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NG Percent 2nd"
	TagNGD_1730_value = system.tag.readBlocking([TagPathNGD_1730])[0].value
	StringD_1730 = format_value(TagNGD_1730_value)
	
	#3rd Column
	TagPathNGE_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1730_value = system.tag.readBlocking([TagPathNGE_1730])[0].value
	StringE_1730 = format_quantity(TagNGE_1730_value)
	
	TagPathNGF_1730 = "SourceA/Block D/Station 1730/Data/Dashboard/NG Percent 3rd"
	TagNGF_1730_value = system.tag.readBlocking([TagPathNGF_1730])[0].value
	StringF_1730 = format_value(TagNGF_1730_value)
	
	#Adding 1730 To Object Array
	Object_1730 = StationObject("1730", TagNGA_1730_value, TagNGB_1730_value, TagNGC_1730_value, TagNGD_1730_value, TagNGE_1730_value, TagNGF_1730_value)
	StationObjectArray.append(Object_1730)
	#/1730
	
	#1340
	#1st Column
	TagPathNGA_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1340_value = system.tag.readBlocking([TagPathNGA_1340])[0].value
	StringA_1340 = format_quantity(TagNGA_1340_value)
	
	TagPathNGB_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NG Percent 1st"
	TagNGB_1340_value = system.tag.readBlocking([TagPathNGB_1340])[0].value
	StringB_1340 = format_value(TagNGB_1340_value)
	
	#2nd Column
	TagPathNGC_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1340_value = system.tag.readBlocking([TagPathNGC_1340])[0].value
	StringC_1340 = format_quantity(TagNGC_1340_value)
	
	TagPathNGD_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NG Percent 2nd"
	TagNGD_1340_value = system.tag.readBlocking([TagPathNGD_1340])[0].value
	StringD_1340 = format_value(TagNGD_1340_value)
	
	#3rd Column
	TagPathNGE_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1340_value = system.tag.readBlocking([TagPathNGE_1340])[0].value
	StringE_1340 = format_quantity(TagNGE_1340_value)
	
	TagPathNGF_1340 = "SourceA/Block D/Station 1340/Data/Dashboard/NG Percent 3rd"
	TagNGF_1340_value = system.tag.readBlocking([TagPathNGF_1340])[0].value
	StringF_1340 = format_value(TagNGF_1340_value)
	
	#Adding 1340 To Object Array
	Object_1340 = StationObject("1340", TagNGA_1340_value, TagNGB_1340_value, TagNGC_1340_value, TagNGD_1340_value, TagNGE_1340_value, TagNGF_1340_value)
	StationObjectArray.append(Object_1340)
	#/1340
	
	#1341
	#1st Column
	TagPathNGA_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1341_value = system.tag.readBlocking([TagPathNGA_1341])[0].value
	StringA_1341 = format_quantity(TagNGA_1341_value)
	
	TagPathNGB_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NG Percent 1st"
	TagNGB_1341_value = system.tag.readBlocking([TagPathNGB_1341])[0].value
	StringB_1341 = format_value(TagNGB_1341_value)
	
	#2nd Column
	TagPathNGC_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1341_value = system.tag.readBlocking([TagPathNGC_1341])[0].value
	StringC_1341 = format_quantity(TagNGC_1341_value)
	
	TagPathNGD_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NG Percent 2nd"
	TagNGD_1341_value = system.tag.readBlocking([TagPathNGD_1341])[0].value
	StringD_1341 = format_value(TagNGD_1341_value)
	
	#3rd Column
	TagPathNGE_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1341_value = system.tag.readBlocking([TagPathNGE_1341])[0].value
	StringE_1341 = format_quantity(TagNGE_1341_value)
	
	TagPathNGF_1341 = "SourceA/Block D/Station 1341/Data/Dashboard/NG Percent 3rd"
	TagNGF_1341_value = system.tag.readBlocking([TagPathNGF_1341])[0].value
	StringF_1341 = format_value(TagNGF_1341_value)
	
	#Adding 1341 To Object Array
	Object_1341 = StationObject("1341", TagNGA_1341_value, TagNGB_1341_value, TagNGC_1341_value, TagNGD_1341_value, TagNGE_1341_value, TagNGF_1341_value)
	StationObjectArray.append(Object_1341)
	#/1341
	
	#1345
	#1st Column
	TagPathNGA_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1345_value = system.tag.readBlocking([TagPathNGA_1345])[0].value
	StringA_1345 = format_quantity(TagNGA_1345_value)
	
	TagPathNGB_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NG Percent 1st"
	TagNGB_1345_value = system.tag.readBlocking([TagPathNGB_1345])[0].value
	StringB_1345 = format_value(TagNGB_1345_value)
	
	#2nd Column
	TagPathNGC_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1345_value = system.tag.readBlocking([TagPathNGC_1345])[0].value
	StringC_1345 = format_quantity(TagNGC_1345_value)
	
	TagPathNGD_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NG Percent 2nd"
	TagNGD_1345_value = system.tag.readBlocking([TagPathNGD_1345])[0].value
	StringD_1345 = format_value(TagNGD_1345_value)
	
	#3rd Column
	TagPathNGE_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1345_value = system.tag.readBlocking([TagPathNGE_1345])[0].value
	StringE_1345 = format_quantity(TagNGE_1345_value)
	
	TagPathNGF_1345 = "SourceA/Block D/Station 1345/Data/Dashboard/NG Percent 3rd"
	TagNGF_1345_value = system.tag.readBlocking([TagPathNGF_1345])[0].value
	StringF_1345 = format_value(TagNGF_1345_value)
	
	#Adding 1345 To Object Array
	Object_1345 = StationObject("1345", TagNGA_1345_value, TagNGB_1345_value, TagNGC_1345_value, TagNGD_1345_value, TagNGE_1345_value, TagNGF_1345_value)
	StationObjectArray.append(Object_1345)
	#/1345
	#/Block D
	
	
	#Block E
	#1360
	#1st Column
	TagPathNGA_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1360_value = system.tag.readBlocking([TagPathNGA_1360])[0].value
	StringA_1360 = format_quantity(TagNGA_1360_value)
	
	TagPathNGB_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NG Percent 1st"
	TagNGB_1360_value = system.tag.readBlocking([TagPathNGB_1360])[0].value
	StringB_1360 = format_value(TagNGB_1360_value)
	
	#2nd Column
	TagPathNGC_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1360_value = system.tag.readBlocking([TagPathNGC_1360])[0].value
	StringC_1360 = format_quantity(TagNGC_1360_value)
	
	TagPathNGD_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NG Percent 2nd"
	TagNGD_1360_value = system.tag.readBlocking([TagPathNGD_1360])[0].value
	StringD_1360 = format_value(TagNGD_1360_value)
	
	#3rd Column
	TagPathNGE_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1360_value = system.tag.readBlocking([TagPathNGE_1360])[0].value
	StringE_1360 = format_quantity(TagNGE_1360_value)
	
	TagPathNGF_1360 = "SourceA/Block E/Station 1360/Data/Dashboard/NG Percent 3rd"
	TagNGF_1360_value = system.tag.readBlocking([TagPathNGF_1360])[0].value
	StringF_1360 = format_value(TagNGF_1360_value)
	
	#Adding 1360 To Object Array
	Object_1360 = StationObject("1360", TagNGA_1360_value, TagNGB_1360_value, TagNGC_1360_value, TagNGD_1360_value, TagNGE_1360_value, TagNGF_1360_value)
	StationObjectArray.append(Object_1360)
	#/1360
	
	#1370
	#1st Column
	TagPathNGA_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1370_value = system.tag.readBlocking([TagPathNGA_1370])[0].value
	StringA_1370 = format_quantity(TagNGA_1370_value)
	
	TagPathNGB_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NG Percent 1st"
	TagNGB_1370_value = system.tag.readBlocking([TagPathNGB_1370])[0].value
	StringB_1370 = format_value(TagNGB_1370_value)
	
	#2nd Column
	TagPathNGC_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1370_value = system.tag.readBlocking([TagPathNGC_1370])[0].value
	StringC_1370 = format_quantity(TagNGC_1370_value)
	
	TagPathNGD_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NG Percent 2nd"
	TagNGD_1370_value = system.tag.readBlocking([TagPathNGD_1370])[0].value
	StringD_1370 = format_value(TagNGD_1370_value)
	
	#3rd Column
	TagPathNGE_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1370_value = system.tag.readBlocking([TagPathNGE_1370])[0].value
	StringE_1370 = format_quantity(TagNGE_1370_value)
	
	TagPathNGF_1370 = "SourceA/Block E/Station 1370/Data/Dashboard/NG Percent 3rd"
	TagNGF_1370_value = system.tag.readBlocking([TagPathNGF_1370])[0].value
	StringF_1370 = format_value(TagNGF_1370_value)
	
	#Adding 1370 To Object Array
	Object_1370 = StationObject("1370", TagNGA_1370_value, TagNGB_1370_value, TagNGC_1370_value, TagNGD_1370_value, TagNGE_1370_value, TagNGF_1370_value)
	StationObjectArray.append(Object_1370)
	#/1370
	
	#1371
	#1st Column
	TagPathNGA_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1371_value = system.tag.readBlocking([TagPathNGA_1371])[0].value
	StringA_1371 = format_quantity(TagNGA_1371_value)
	
	TagPathNGB_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NG Percent 1st"
	TagNGB_1371_value = system.tag.readBlocking([TagPathNGB_1371])[0].value
	StringB_1371 = format_value(TagNGB_1371_value)
	
	#2nd Column
	TagPathNGC_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1371_value = system.tag.readBlocking([TagPathNGC_1371])[0].value
	StringC_1371 = format_quantity(TagNGC_1371_value)
	
	TagPathNGD_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NG Percent 2nd"
	TagNGD_1371_value = system.tag.readBlocking([TagPathNGD_1371])[0].value
	StringD_1371 = format_value(TagNGD_1371_value)
	
	#3rd Column
	TagPathNGE_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1371_value = system.tag.readBlocking([TagPathNGE_1371])[0].value
	StringE_1371 = format_quantity(TagNGE_1371_value)
	
	TagPathNGF_1371 = "SourceA/Block E/Station 1371/Data/Dashboard/NG Percent 3rd"
	TagNGF_1371_value = system.tag.readBlocking([TagPathNGF_1371])[0].value
	StringF_1371 = format_value(TagNGF_1371_value)
	
	#Adding 1371 To Object Array
	Object_1371 = StationObject("1371", TagNGA_1371_value, TagNGB_1371_value, TagNGC_1371_value, TagNGD_1371_value, TagNGE_1371_value, TagNGF_1371_value)
	StationObjectArray.append(Object_1371)
	#/1371
	
	#1375
	#1st Column
	TagPathNGA_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1375_value = system.tag.readBlocking([TagPathNGA_1375])[0].value
	StringA_1375 = format_quantity(TagNGA_1375_value)
	
	TagPathNGB_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NG Percent 1st"
	TagNGB_1375_value = system.tag.readBlocking([TagPathNGB_1375])[0].value
	StringB_1375 = format_value(TagNGB_1375_value)
	
	#2nd Column
	TagPathNGC_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1375_value = system.tag.readBlocking([TagPathNGC_1375])[0].value
	StringC_1375 = format_quantity(TagNGC_1375_value)
	
	TagPathNGD_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NG Percent 2nd"
	TagNGD_1375_value = system.tag.readBlocking([TagPathNGD_1375])[0].value
	StringD_1375 = format_value(TagNGD_1375_value)
	
	#3rd Column
	TagPathNGE_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1375_value = system.tag.readBlocking([TagPathNGE_1375])[0].value
	StringE_1375 = format_quantity(TagNGE_1375_value)
	
	TagPathNGF_1375 = "SourceA/Block E/Station 1375/Data/Dashboard/NG Percent 3rd"
	TagNGF_1375_value = system.tag.readBlocking([TagPathNGF_1375])[0].value
	StringF_1375 = format_value(TagNGF_1375_value)
	
	#Adding 1375 To Object Array
	Object_1375 = StationObject("1375", TagNGA_1375_value, TagNGB_1375_value, TagNGC_1375_value, TagNGD_1375_value, TagNGE_1375_value, TagNGF_1375_value)
	StationObjectArray.append(Object_1375)
	#/1375
	
	#1380
	#1st Column
	TagPathNGA_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1380_value = system.tag.readBlocking([TagPathNGA_1380])[0].value
	StringA_1380 = format_quantity(TagNGA_1380_value)
	
	TagPathNGB_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NG Percent 1st"
	TagNGB_1380_value = system.tag.readBlocking([TagPathNGB_1380])[0].value
	StringB_1380 = format_value(TagNGB_1380_value)
	
	#2nd Column
	TagPathNGC_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1380_value = system.tag.readBlocking([TagPathNGC_1380])[0].value
	StringC_1380 = format_quantity(TagNGC_1380_value)
	
	TagPathNGD_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NG Percent 2nd"
	TagNGD_1380_value = system.tag.readBlocking([TagPathNGD_1380])[0].value
	StringD_1380 = format_value(TagNGD_1380_value)
	
	#3rd Column
	TagPathNGE_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1380_value = system.tag.readBlocking([TagPathNGE_1380])[0].value
	StringE_1380 = format_quantity(TagNGE_1380_value)
	
	TagPathNGF_1380 = "SourceA/Block E/Station 1380/Data/Dashboard/NG Percent 3rd"
	TagNGF_1380_value = system.tag.readBlocking([TagPathNGF_1380])[0].value
	StringF_1380 = format_value(TagNGF_1380_value)
	
	#Adding 1380 To Object Array
	Object_1380 = StationObject("1380", TagNGA_1380_value, TagNGB_1380_value, TagNGC_1380_value, TagNGD_1380_value, TagNGE_1380_value, TagNGF_1380_value)
	StationObjectArray.append(Object_1380)
	#/1380
	
	#1381
	#1st Column
	TagPathNGA_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1381_value = system.tag.readBlocking([TagPathNGA_1381])[0].value
	StringA_1381 = format_quantity(TagNGA_1381_value)
	
	TagPathNGB_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NG Percent 1st"
	TagNGB_1381_value = system.tag.readBlocking([TagPathNGB_1381])[0].value
	StringB_1381 = format_value(TagNGB_1381_value)
	
	#2nd Column
	TagPathNGC_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1381_value = system.tag.readBlocking([TagPathNGC_1381])[0].value
	StringC_1381 = format_quantity(TagNGC_1381_value)
	
	TagPathNGD_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NG Percent 2nd"
	TagNGD_1381_value = system.tag.readBlocking([TagPathNGD_1381])[0].value
	StringD_1381 = format_value(TagNGD_1381_value)
	
	#3rd Column
	TagPathNGE_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1381_value = system.tag.readBlocking([TagPathNGE_1381])[0].value
	StringE_1381 = format_quantity(TagNGE_1381_value)
	
	TagPathNGF_1381 = "SourceA/Block E/Station 1381/Data/Dashboard/NG Percent 3rd"
	TagNGF_1381_value = system.tag.readBlocking([TagPathNGF_1381])[0].value
	StringF_1381 = format_value(TagNGF_1381_value)
	#Adding 1381 To Object Array
	Object_1381 = StationObject("1381", TagNGA_1381_value, TagNGB_1381_value, TagNGC_1381_value, TagNGD_1381_value, TagNGE_1381_value, TagNGF_1381_value)
	StationObjectArray.append(Object_1381)
	#/1381
	
	#1385
	#1st Column
	TagPathNGA_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1385_value = system.tag.readBlocking([TagPathNGA_1385])[0].value
	StringA_1385 = format_quantity(TagNGA_1385_value)
	
	TagPathNGB_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NG Percent 1st"
	TagNGB_1385_value = system.tag.readBlocking([TagPathNGB_1385])[0].value
	StringB_1385 = format_value(TagNGB_1385_value)
	
	#2nd Column
	TagPathNGC_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1385_value = system.tag.readBlocking([TagPathNGC_1385])[0].value
	StringC_1385 = format_quantity(TagNGC_1385_value)
	
	TagPathNGD_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NG Percent 2nd"
	TagNGD_1385_value = system.tag.readBlocking([TagPathNGD_1385])[0].value
	StringD_1385 = format_value(TagNGD_1385_value)
	
	#3rd Column
	TagPathNGE_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1385_value = system.tag.readBlocking([TagPathNGE_1385])[0].value
	StringE_1385 = format_quantity(TagNGE_1385_value)
	
	TagPathNGF_1385 = "SourceA/Block E/Station 1385/Data/Dashboard/NG Percent 3rd"
	TagNGF_1385_value = system.tag.readBlocking([TagPathNGF_1385])[0].value
	StringF_1385 = format_value(TagNGF_1385_value)
	
	#Adding 1385 To Object Array
	Object_1385 = StationObject("1385", TagNGA_1385_value, TagNGB_1385_value, TagNGC_1385_value, TagNGD_1385_value, TagNGE_1385_value, TagNGF_1385_value)
	StationObjectArray.append(Object_1385)
	#/1385
	
	#1390
	#1st Column
	TagPathNGA_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1390_value = system.tag.readBlocking([TagPathNGA_1390])[0].value
	StringA_1390 = format_quantity(TagNGA_1390_value)
	
	TagPathNGB_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NG Percent 1st"
	TagNGB_1390_value = system.tag.readBlocking([TagPathNGB_1390])[0].value
	StringB_1390 = format_value(TagNGB_1390_value)
	
	#2nd Column
	TagPathNGC_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1390_value = system.tag.readBlocking([TagPathNGC_1390])[0].value
	StringC_1390 = format_quantity(TagNGC_1390_value)
	
	TagPathNGD_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NG Percent 2nd"
	TagNGD_1390_value = system.tag.readBlocking([TagPathNGD_1390])[0].value
	StringD_1390 = format_value(TagNGD_1390_value)
	
	#3rd Column
	TagPathNGE_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1390_value = system.tag.readBlocking([TagPathNGE_1390])[0].value
	StringE_1390 = format_quantity(TagNGE_1390_value)
	
	TagPathNGF_1390 = "SourceA/Block E/Station 1390/Data/Dashboard/NG Percent 3rd"
	TagNGF_1390_value = system.tag.readBlocking([TagPathNGF_1390])[0].value
	StringF_1390 = format_value(TagNGF_1390_value)
	
	#Adding 1390 To Object Array
	Object_1390 = StationObject("1390", TagNGA_1390_value, TagNGB_1390_value, TagNGC_1390_value, TagNGD_1390_value, TagNGE_1390_value, TagNGF_1390_value)
	StationObjectArray.append(Object_1390)
	#/1390
	
	#1398
	#1st Column
	TagPathNGA_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1398_value = system.tag.readBlocking([TagPathNGA_1398])[0].value
	StringA_1398 = format_quantity(TagNGA_1398_value)
	
	TagPathNGB_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NG Percent 1st"
	TagNGB_1398_value = system.tag.readBlocking([TagPathNGB_1398])[0].value
	StringB_1398 = format_value(TagNGB_1398_value)
	
	#2nd Column
	TagPathNGC_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1398_value = system.tag.readBlocking([TagPathNGC_1398])[0].value
	StringC_1398 = format_quantity(TagNGC_1398_value)
	
	TagPathNGD_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NG Percent 2nd"
	TagNGD_1398_value = system.tag.readBlocking([TagPathNGD_1398])[0].value
	StringD_1398 = format_value(TagNGD_1398_value)
	
	#3rd Column
	TagPathNGE_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1398_value = system.tag.readBlocking([TagPathNGE_1398])[0].value
	StringE_1398 = format_quantity(TagNGE_1398_value)
	
	TagPathNGF_1398 = "SourceA/Block E/Station 1398/Data/Dashboard/NG Percent 3rd"
	TagNGF_1398_value = system.tag.readBlocking([TagPathNGF_1398])[0].value
	StringF_1398 = format_value(TagNGF_1398_value)
	
	#Adding 1398 To Object Array
	Object_1398 = StationObject("1398", TagNGA_1398_value, TagNGB_1398_value, TagNGC_1398_value, TagNGD_1398_value, TagNGE_1398_value, TagNGF_1398_value)
	StationObjectArray.append(Object_1398)
	#/1398
	
	#1400
	#1st Column
	TagPathNGA_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1400_value = system.tag.readBlocking([TagPathNGA_1400])[0].value
	StringA_1400 = format_quantity(TagNGA_1400_value)
	
	TagPathNGB_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NG Percent 1st"
	TagNGB_1400_value = system.tag.readBlocking([TagPathNGB_1400])[0].value
	StringB_1400 = format_value(TagNGB_1400_value)
	
	#2nd Column
	TagPathNGC_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1400_value = system.tag.readBlocking([TagPathNGC_1400])[0].value
	StringC_1400 = format_quantity(TagNGC_1400_value)
	
	TagPathNGD_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NG Percent 2nd"
	TagNGD_1400_value = system.tag.readBlocking([TagPathNGD_1400])[0].value
	StringD_1400 = format_value(TagNGD_1400_value)
	
	#3rd Column
	TagPathNGE_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1400_value = system.tag.readBlocking([TagPathNGE_1400])[0].value
	StringE_1400 = format_quantity(TagNGE_1400_value)
	
	TagPathNGF_1400 = "SourceA/Block E/Station 1400/Data/Dashboard/NG Percent 3rd"
	TagNGF_1400_value = system.tag.readBlocking([TagPathNGF_1400])[0].value
	StringF_1400 = format_value(TagNGF_1400_value)
	
	#Adding 1400 To Object Array
	Object_1400 = StationObject("1400", TagNGA_1400_value, TagNGB_1400_value, TagNGC_1400_value, TagNGD_1400_value, TagNGE_1400_value, TagNGF_1400_value)
	StationObjectArray.append(Object_1400)
	#/1400
	
	#1410
	#1st Column
	TagPathNGA_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NGParts/NGPart1st"
	TagNGA_1410_value = system.tag.readBlocking([TagPathNGA_1410])[0].value
	StringA_1410 = format_quantity(TagNGA_1410_value)
	
	TagPathNGB_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NG Percent 1st"
	TagNGB_1410_value = system.tag.readBlocking([TagPathNGB_1410])[0].value
	StringB_1410 = format_value(TagNGB_1410_value)
	
	#2nd Column
	TagPathNGC_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NGParts/NGPart2nd"
	TagNGC_1410_value = system.tag.readBlocking([TagPathNGC_1410])[0].value
	StringC_1410 = format_quantity(TagNGC_1410_value)
	
	TagPathNGD_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NG Percent 2nd"
	TagNGD_1410_value = system.tag.readBlocking([TagPathNGD_1410])[0].value
	StringD_1410 = format_value(TagNGD_1410_value)
	
	#3rd Column
	TagPathNGE_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NGParts/NGPart3rd"
	TagNGE_1410_value = system.tag.readBlocking([TagPathNGE_1410])[0].value
	StringE_1410 = format_quantity(TagNGE_1410_value)
	
	TagPathNGF_1410 = "SourceA/Block E/Station 1410/Data/Dashboard/NG Percent 3rd"
	TagNGF_1410_value = system.tag.readBlocking([TagPathNGF_1410])[0].value
	StringF_1410 = format_value(TagNGF_1410_value)
	
	#Adding 1410 To Object Array
	Object_1410 = StationObject("1410", TagNGA_1410_value, TagNGB_1410_value, TagNGC_1410_value, TagNGD_1410_value, TagNGE_1410_value, TagNGF_1410_value)
	StationObjectArray.append(Object_1410)
	#/1410
	#/Block E
	
	
	
	#General PCU Data
	#Block A
	#1st Column
	TagPathNGA_BlockA = "SourceB/StationStatus/BlockA/Counts/Sta1016TotalParts"
	TagNGA_BlockA_value = system.tag.readBlocking([TagPathNGA_BlockA])[0].value
	StringA_BlockA = format_quantity(TagNGA_BlockA_value)
	
	#2nd Column
	TagPathNGB_BlockA = "SourceB/StationStatus/BlockA/Counts/TotalNoGoodCount"
	TagNGB_BlockA_value = system.tag.readBlocking([TagPathNGB_BlockA])[0].value
	StringB_BlockA = format_quantity(TagNGB_BlockA_value)
	
	#3rd Column
	PercentNGC_BlockA = ((float(TagNGB_BlockA_value) / TagNGA_BlockA_value)*100)
	StringC_BlockA = format_value(PercentNGC_BlockA)
	#/Block A
	
	
	
	#Block B
	#1st Column
	TagPathNGA_BlockB = "SourceB/StationStatus/BlockB/Counts/Sta1100TotalParts"
	TagNGA_BlockB_value = system.tag.readBlocking([TagPathNGA_BlockB])[0].value
	StringA_BlockB = format_quantity(TagNGA_BlockB_value)
	
	#2nd Column
	TagPathNGB_BlockB = "SourceB/StationStatus/BlockB/Counts/TotalNoGoodCount"
	TagNGB_BlockB_value = system.tag.readBlocking([TagPathNGB_BlockB])[0].value
	StringB_BlockB = format_quantity(TagNGB_BlockB_value)
	
	#3rd Column
	PercentNGC_BlockB = ((float(TagNGB_BlockB_value) / TagNGA_BlockB_value)*100)
	StringC_BlockB = format_value(PercentNGC_BlockB)
	#/Block B	
		
	#Block C
	#1st Column
	TagPathNGA_BlockC = "SourceB/StationStatus/BlockC/Counts/Sta1180TotalParts"
	TagNGA_BlockC_value = system.tag.readBlocking([TagPathNGA_BlockC])[0].value
	StringA_BlockC = format_quantity(TagNGA_BlockC_value)
	
	#2nd Column
	TagPathNGB_BlockC = "SourceB/StationStatus/BlockC/Counts/TotalNoGoodCount"
	TagNGB_BlockC_value = system.tag.readBlocking([TagPathNGB_BlockC])[0].value
	StringB_BlockC = format_quantity(TagNGB_BlockC_value)
	
	#3rd Column
	PercentNGC_BlockC = ((float(TagNGB_BlockC_value) / TagNGA_BlockC_value)*100)
	StringC_BlockC = format_value(PercentNGC_BlockC)
	#/Block C	
	
	#Block D
	#1st Column
	TagPathNGA_BlockD = "SourceB/StationStatus/BlockD/Counts/Sta1300TotalParts"
	TagNGA_BlockD_value = system.tag.readBlocking([TagPathNGA_BlockD])[0].value
	StringA_BlockD = format_quantity(TagNGA_BlockD_value)
	
	#2nd Column
	TagPathNGB_BlockD = "SourceB/StationStatus/BlockD/Counts/TotalNoGoodCount"
	TagNGB_BlockD_value = system.tag.readBlocking([TagPathNGB_BlockD])[0].value
	StringB_BlockD = format_quantity(TagNGB_BlockD_value)
	
	#3rd Column
	PercentNGC_BlockD = ((float(TagNGB_BlockD_value) / TagNGA_BlockD_value)*100)
	StringC_BlockD = format_value(PercentNGC_BlockD)
	#/Block D	
	
	#Block E
	#1st Column
	TagPathNGA_BlockE = "SourceB/StationStatus/BlockE/Counts/Sta1360TotalParts"
	TagNGA_BlockE_value = system.tag.readBlocking([TagPathNGA_BlockE])[0].value
	StringA_BlockE = format_quantity(TagNGA_BlockE_value)
	
	#2nd Column
	TagPathNGB_BlockE = "SourceB/StationStatus/BlockE/Counts/TotalNoGoodCount"
	TagNGB_BlockE_value = system.tag.readBlocking([TagPathNGB_BlockE])[0].value
	StringB_BlockE = format_quantity(TagNGB_BlockE_value)
	
	#3rd Column
	PercentNGC_BlockE = ((float(TagNGB_BlockE_value) / TagNGA_BlockE_value) * 100)
	StringC_BlockE = format_value(PercentNGC_BlockE)
	#/Block E	
	
	#All PCU
	#1st Column
	TagPathNGA_ALL_PCU = "SourceB/StationStatus/BlockA/Counts/Sta1016TotalParts"
	TagNGA_ALL_PCU_value = system.tag.readBlocking([TagPathNGA_ALL_PCU])[0].value
	StringA_ALL_PCU = format_quantity(TagNGA_ALL_PCU_value)
	
	#2nd Column
	TagPathNGB_ALL_PCU = "SourceB/StationStatus/TotalNoGoodCount"
	TagNGB_ALL_PCU_value = system.tag.readBlocking([TagPathNGB_ALL_PCU])[0].value
	StringB_ALL_PCU = format_quantity(TagNGB_ALL_PCU_value)
	
	#3rd Column
	PercentNGC_ALL_PCU = ((float(TagNGB_ALL_PCU_value)/ TagNGA_ALL_PCU_value)*100)
	StringC_ALL_PCU = format_value(PercentNGC_ALL_PCU)
	#/All PCU
	        
	valid_station_objects = [obj for obj in StationObjectArray if isinstance(obj, StationObject)]
	        
	#Time Based Top No Good Data
	OrderedObjectArray = sorted(valid_station_objects, key=lambda x:x.NGF, reverse=True)
	First = OrderedObjectArray[0]
	StationFirst_Number = First.Station
	StationFirst_NGPercent = format_value(First.NGF)
	StationFirst_NGCount = format_quantity(First.NGE)
	
	Second = OrderedObjectArray[1]
	StationSecond_Number = Second.Station
	StationSecond_NGPercent = format_value(Second.NGF)
	StationSecond_NGCount = format_quantity(Second.NGE)
	
	Third = OrderedObjectArray[2]
	StationThird_Number = Third.Station
	StationThird_NGPercent = format_value(Third.NGF)
	StationThird_NGCount = format_quantity(Third.NGE)
	
	Fourth = OrderedObjectArray[3]
	StationFourth_Number = Fourth.Station
	StationFourth_NGPercent = format_value(Fourth.NGF)
	StationFourth_NGCount = format_quantity(Fourth.NGE)
	
	Fifth = OrderedObjectArray[4]
	StationFifth_Number = Fifth.Station
	StationFifth_NGPercent = format_value(Fifth.NGF)
	StationFifth_NGCount = format_quantity(Fifth.NGE)
	
	Sixth = OrderedObjectArray[5]
	StationSixth_Number = Sixth.Station
	StationSixth_NGPercent = format_value(Sixth.NGF)
	StationSixth_NGCount = format_quantity(Sixth.NGE)
	#/NoGoodData Sorting	
	
	html_content = """
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <title>Block Layout</title>
	    <style>
	        body {
	            background-color: #D4F1FF;
	            font-family: Arial, sans-serif;
	            margin: 0;
	            padding: 0;
	        }
	
	        .container {
	            display: flex;
	            flex-wrap: wrap;
	            justify-content: space-around;
	            padding: 20px;
	        }
	
	        .block {
	            border: 1px solid #000;
	            margin: 10px;
	            padding: 10px;
	            width: 800px; /* Adjusted width to accommodate layout */
	            background-color: #BFBFBF;
				display: inline-block;
	        }
	
	        .block-title {
	            text-align: center;
	            font-weight: bold;
	            margin-bottom: 10px;
	            background-color: #D4F1FF;
	            padding: 5px;
	            border-bottom: 2px solid #000;
	        }
	
	        .row {
	            display: flex;
	            margin-bottom: 5px;
	        }
	
	        .header-row {
	            background-color: #B0E0E6;
	        }
	
	        .label-row {
	            font-weight: bold;
	            text-align: center;
	            margin-bottom: 5px;
	        }
	
	        .cell {
	            border: 1px solid #000;
	            padding: 5px;
	            text-align: center;
	            flex: 1;
	        }
	
	        .header {
	            font-weight: bold;
	            background-color: #B0E0E6;
	        }
            
            .headerWhite {
                background-color: #DBDBDB;
            }
			
			.WhiteBase {
				font-weight: bold;
				background-color: #DAE7E8;
			}
	
	        .empty-table {
	            background-color: #D4F1FF;
	            border: none;
	        }
	        
	        
	
	        .highlight {
	            background-color: #FFDBDB; /* Light red for %NG cells */
	        }
	
	        .highlight-blue {
	            background-color: #DBDBFF; /* Light blue for Qty cells */
	        }
			
			.highlight-white {
				background-color: #FFFFFF;
			}
	
	        .station {
	            background-color: #D3D3D3; /* Light gray for station numbers */
	        }
	
	        .special-cell {
	            background-color: #f5f2cb; /* Specific numbers background color */
	        }
	
	        .general-cell {
	            background-color: #f5f4f0; /* Rest of the numbers background color */
	        }
            
            .white-cell {
                background-color: #FFFFFF; 
            }
            
            .gray-cell {
                background-color: #DBDBDB;
            }
	
	        .cell[colspan="2"] {
	            flex: 2;
	        }
			
			.table-container {
				display: flex;
				justify-content: space-between;
				width: 50%;
			}
			
	    </style>
	</head>
	<body>
		<div class = "table-container">
			<table class="block" id="blockABC">
				<thead>
					<tr>
						<th class="block-title" colspan="7">BLOCK A</th>
						<th class="block-title" colspan="7">BLOCK B</th>
						<th class="block-title" colspan="7">BLOCK C</th>
					</tr>
					<tr class="header-row">
						<th class="header empty">Shift</th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty">Shift</th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty">Shift</th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
					</tr>
					<tr class="label-row">
						<th class="empty"></th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="empty"></th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="empty"></th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td class="station">1016</td>
						<td class="special-cell">""" + StringA_1016 + """</td>
						<td class="general-cell">""" + StringB_1016 + """</td>
						<td class="special-cell">""" + StringC_1016 + """</td>
						<td class="general-cell">""" + StringD_1016 + """</td>
						<td class="special-cell">""" + StringE_1016 + """</td>
						<td class="general-cell">""" + StringF_1016 + """</td>
						<td class="station">1100</td>
						<td class="special-cell">""" + StringA_1100 + """</td>
						<td class="general-cell">""" + StringB_1100 + """</td>
						<td class="special-cell">""" + StringC_1100 + """</td>
						<td class="general-cell">""" + StringD_1100 + """</td>
						<td class="special-cell">""" + StringE_1100 + """</td>
						<td class="general-cell">""" + StringF_1100 + """</td>
						<td class="station">1180</td>
						<td class="special-cell">""" + StringA_1180 + """</td>
						<td class="general-cell">""" + StringB_1180 + """</td>
						<td class="special-cell">""" + StringC_1180 + """</td>
						<td class="general-cell">""" + StringD_1180 + """</td>
						<td class="special-cell">""" + StringE_1180 + """</td>
						<td class="general-cell">""" + StringF_1180 + """</td>
					</tr>
					<tr>
						<td class="station">1020</td>
						<td class="special-cell">""" + StringA_1020 + """</td>
						<td class="general-cell">""" + StringB_1020 + """</td>
						<td class="special-cell">""" + StringC_1020 + """</td>
						<td class="general-cell">""" + StringD_1020 + """</td>
						<td class="special-cell">""" + StringE_1020 + """</td>
						<td class="general-cell">""" + StringF_1020 + """</td>
						<td class="station">1101</td>						
						<td class="special-cell">""" + StringA_1101 + """</td>
						<td class="general-cell">""" + StringB_1101 + """</td>
						<td class="special-cell">""" + StringC_1101 + """</td>
						<td class="general-cell">""" + StringD_1101 + """</td>
						<td class="special-cell">""" + StringE_1101 + """</td>
						<td class="general-cell">""" + StringF_1101 + """</td>
						<td class="station">1200</td>
						<td class="special-cell">""" + StringA_1200 + """</td>
						<td class="general-cell">""" + StringB_1200 + """</td>
						<td class="special-cell">""" + StringC_1200 + """</td>
						<td class="general-cell">""" + StringD_1200 + """</td>
						<td class="special-cell">""" + StringE_1200 + """</td>
						<td class="general-cell">""" + StringF_1200 + """</td>
					</tr>
					<tr>
						<td class="station">1030</td>
						<td class="special-cell">""" + StringA_1030 + """</td>
						<td class="general-cell">""" + StringB_1030 + """</td>
						<td class="special-cell">""" + StringC_1030 + """</td>
						<td class="general-cell">""" + StringD_1030 + """</td>
						<td class="special-cell">""" + StringF_1030 + """</td>
						<td class="general-cell">""" + StringE_1030 + """</td>
						<td class="station">1110</td>
						<td class="special-cell">""" + StringA_1110 + """</td>
						<td class="general-cell">""" + StringB_1110 + """</td>
						<td class="special-cell">""" + StringC_1110 + """</td>
						<td class="general-cell">""" + StringD_1110 + """</td>
						<td class="special-cell">""" + StringE_1110 + """</td>
						<td class="general-cell">""" + StringF_1110 + """</td>
						<td class="station">1205</td>
						<td class="special-cell">""" + StringA_1205 + """</td>
						<td class="general-cell">""" + StringB_1205 + """</td>
						<td class="special-cell">""" + StringC_1205 + """</td>
						<td class="general-cell">""" + StringD_1205 + """</td>
						<td class="special-cell">""" + StringE_1205 + """</td>
						<td class="general-cell">""" + StringF_1205 + """</td>
					</tr>
					<tr>
						<td class="station">1040</td>
						<td class="special-cell">""" + StringA_1040 + """</td>
						<td class="general-cell">""" + StringB_1040 + """</td>
						<td class="special-cell">""" + StringC_1040 + """</td>
						<td class="general-cell">""" + StringD_1040 + """</td>
						<td class="special-cell">""" + StringF_1040 + """</td>
						<td class="general-cell">""" + StringE_1040 + """</td>
						<td class="station">1120</td>
						<td class="special-cell">""" + StringA_1120 + """</td>
						<td class="general-cell">""" + StringB_1120 + """</td>
						<td class="special-cell">""" + StringC_1120 + """</td>
						<td class="general-cell">""" + StringD_1120 + """</td>
						<td class="special-cell">""" + StringE_1120 + """</td>
						<td class="general-cell">""" + StringF_1120 + """</td>
						<td class="station">1210</td>
						<td class="special-cell">""" + StringA_1210 + """</td>
						<td class="general-cell">""" + StringB_1210 + """</td>
						<td class="special-cell">""" + StringC_1210 + """</td>
						<td class="general-cell">""" + StringD_1210 + """</td>
						<td class="special-cell">""" + StringE_1210 + """</td>
						<td class="general-cell">""" + StringF_1210 + """</td>
					</tr>
					<tr>
						<td class="station">1048</td>
						<td class="special-cell">""" + StringA_1048 + """</td>
						<td class="general-cell">""" + StringB_1048 + """</td>
						<td class="special-cell">""" + StringC_1048 + """</td>
						<td class="general-cell">""" + StringD_1048 + """</td>
						<td class="special-cell">""" + StringF_1048 + """</td>
						<td class="general-cell">""" + StringE_1048 + """</td>
						<td class="station">1500</td>
						<td class="special-cell">""" + StringA_1500 + """</td>
						<td class="general-cell">""" + StringB_1500 + """</td>
						<td class="special-cell">""" + StringC_1500 + """</td>
						<td class="general-cell">""" + StringD_1500 + """</td>
						<td class="special-cell">""" + StringE_1500 + """</td>
						<td class="general-cell">""" + StringF_1500 + """</td>
						<td class="station">1620</td>
						<td class="special-cell">""" + StringA_1620 + """</td>
						<td class="general-cell">""" + StringB_1620 + """</td>
						<td class="special-cell">""" + StringC_1620 + """</td>
						<td class="general-cell">""" + StringD_1620 + """</td>
						<td class="special-cell">""" + StringE_1620 + """</td>
						<td class="general-cell">""" + StringF_1620 + """</td>
					</tr>
					<tr>
						<td class="station">1050</td>
						<td class="special-cell">""" + StringA_1050 + """</td>
						<td class="general-cell">""" + StringB_1050 + """</td>
						<td class="special-cell">""" + StringC_1050 + """</td>
						<td class="general-cell">""" + StringD_1050 + """</td>
						<td class="special-cell">""" + StringF_1050 + """</td>
						<td class="general-cell">""" + StringE_1050 + """</td>
						<td class="station">1510</td>
						<td class="special-cell">""" + StringA_1510 + """</td>
						<td class="general-cell">""" + StringB_1510 + """</td>
						<td class="special-cell">""" + StringC_1510 + """</td>
						<td class="general-cell">""" + StringD_1510 + """</td>
						<td class="special-cell">""" + StringE_1510 + """</td>
						<td class="general-cell">""" + StringF_1510 + """</td>
						<td class="station">1630</td>
						<td class="special-cell">""" + StringA_1630 + """</td>
						<td class="general-cell">""" + StringB_1630 + """</td>
						<td class="special-cell">""" + StringC_1630 + """</td>
						<td class="general-cell">""" + StringD_1630 + """</td>
						<td class="special-cell">""" + StringE_1630 + """</td>
						<td class="general-cell">""" + StringF_1630 + """</td>
					</tr>
					<tr>
						<td class="station">1060</td>
						<td class="special-cell">""" + StringA_1060 + """</td>
						<td class="general-cell">""" + StringB_1060 + """</td>
						<td class="special-cell">""" + StringC_1060 + """</td>
						<td class="general-cell">""" + StringD_1060 + """</td>
						<td class="special-cell">""" + StringF_1060 + """</td>
						<td class="general-cell">""" + StringE_1060 + """</td>
						<td class="station">1530</td>
						<td class="special-cell">""" + StringA_1530 + """</td>
						<td class="general-cell">""" + StringB_1530 + """</td>
						<td class="special-cell">""" + StringC_1530 + """</td>
						<td class="general-cell">""" + StringD_1530 + """</td>
						<td class="special-cell">""" + StringE_1530 + """</td>
						<td class="general-cell">""" + StringF_1530 + """</td>
						<td class="station">1640</td>
						<td class="special-cell">""" + StringA_1640 + """</td>
						<td class="general-cell">""" + StringB_1640 + """</td>
						<td class="special-cell">""" + StringC_1640 + """</td>
						<td class="general-cell">""" + StringD_1640 + """</td>
						<td class="special-cell">""" + StringE_1640 + """</td>
						<td class="general-cell">""" + StringF_1640 + """</td>
					</tr>
					<tr>
						<td class="station">1070</td>
						<td class="special-cell">""" + StringA_1070 + """</td>
						<td class="general-cell">""" + StringB_1070 + """</td>
						<td class="special-cell">""" + StringC_1070 + """</td>
						<td class="general-cell">""" + StringD_1070 + """</td>
						<td class="special-cell">""" + StringF_1070 + """</td>
						<td class="general-cell">""" + StringE_1070 + """</td>
						<td class="station">1140</td>
						<td class="special-cell">""" + StringA_1140 + """</td>
						<td class="general-cell">""" + StringB_1140 + """</td>
						<td class="special-cell">""" + StringC_1140 + """</td>
						<td class="general-cell">""" + StringD_1140 + """</td>
						<td class="special-cell">""" + StringE_1140 + """</td>
						<td class="general-cell">""" + StringF_1140 + """</td>
						<td class="station">1650</td>
						<td class="special-cell">""" + StringA_1650 + """</td>
						<td class="general-cell">""" + StringB_1650 + """</td>
						<td class="special-cell">""" + StringC_1650 + """</td>
						<td class="general-cell">""" + StringD_1650 + """</td>
						<td class="special-cell">""" + StringE_1650 + """</td>
						<td class="general-cell">""" + StringF_1650 + """</td>
					</tr>
					<tr>
						<td class="station">1071</td>
						<td class="special-cell">""" + StringA_1071 + """</td>
						<td class="general-cell">""" + StringB_1071 + """</td>
						<td class="special-cell">""" + StringC_1071 + """</td>
						<td class="general-cell">""" + StringD_1071 + """</td>
						<td class="special-cell">""" + StringF_1071 + """</td>
						<td class="general-cell">""" + StringE_1071 + """</td>
						<td class="station">1142</td>
						<td class="special-cell">""" + StringA_1142 + """</td>
						<td class="general-cell">""" + StringB_1142 + """</td>
						<td class="special-cell">""" + StringC_1142 + """</td>
						<td class="general-cell">""" + StringD_1142 + """</td>
						<td class="special-cell">""" + StringE_1142 + """</td>
						<td class="general-cell">""" + StringF_1142 + """</td>
						<td class="station">1220</td>
						<td class="special-cell">""" + StringA_1220 + """</td>
						<td class="general-cell">""" + StringB_1220 + """</td>
						<td class="special-cell">""" + StringC_1220 + """</td>
						<td class="general-cell">""" + StringD_1220 + """</td>
						<td class="special-cell">""" + StringE_1220 + """</td>
						<td class="general-cell">""" + StringF_1220 + """</td>
					</tr>
					<tr>
						<td class="station">1072</td>
						<td class="special-cell">""" + StringA_1072 + """</td>
						<td class="general-cell">""" + StringB_1072 + """</td>
						<td class="special-cell">""" + StringC_1072 + """</td>
						<td class="general-cell">""" + StringD_1072 + """</td>
						<td class="special-cell">""" + StringF_1072 + """</td>
						<td class="general-cell">""" + StringE_1072 + """</td>
						<td class="station">1150</td>
						<td class="special-cell">""" + StringA_1150 + """</td>
						<td class="general-cell">""" + StringB_1150 + """</td>
						<td class="special-cell">""" + StringC_1150 + """</td>
						<td class="general-cell">""" + StringD_1150 + """</td>
						<td class="special-cell">""" + StringE_1150 + """</td>
						<td class="general-cell">""" + StringF_1150 + """</td>
						<td class="station">1230</td>
						<td class="special-cell">""" + StringA_1230 + """</td>
						<td class="general-cell">""" + StringB_1230 + """</td>
						<td class="special-cell">""" + StringC_1230 + """</td>
						<td class="general-cell">""" + StringD_1230 + """</td>
						<td class="special-cell">""" + StringE_1230 + """</td>
						<td class="general-cell">""" + StringF_1230 + """</td>
					</tr>
					<tr>
						<td class="station">1080</td>
						<td class="special-cell">""" + StringA_1080 + """</td>
						<td class="general-cell">""" + StringB_1080 + """</td>
						<td class="special-cell">""" + StringC_1080 + """</td>
						<td class="general-cell">""" + StringD_1080 + """</td>
						<td class="special-cell">""" + StringF_1080 + """</td>
						<td class="general-cell">""" + StringE_1080 + """</td>
						<td class="station">1160</td>
						<td class="special-cell">""" + StringA_1160 + """</td>
						<td class="general-cell">""" + StringB_1160 + """</td>
						<td class="special-cell">""" + StringC_1160 + """</td>
						<td class="general-cell">""" + StringD_1160 + """</td>
						<td class="special-cell">""" + StringE_1160 + """</td>
						<td class="general-cell">""" + StringF_1160 + """</td>
						<td class="station">1240</td>
						<td class="special-cell">""" + StringA_1240 + """</td>
						<td class="general-cell">""" + StringB_1240 + """</td>
						<td class="special-cell">""" + StringC_1240 + """</td>
						<td class="general-cell">""" + StringD_1240 + """</td>
						<td class="special-cell">""" + StringE_1240 + """</td>
						<td class="general-cell">""" + StringF_1240 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1161</td>
						<td class="special-cell">""" + StringA_1161 + """</td>
						<td class="general-cell">""" + StringB_1161 + """</td>
						<td class="special-cell">""" + StringC_1161 + """</td>
						<td class="general-cell">""" + StringD_1161 + """</td>
						<td class="special-cell">""" + StringE_1161 + """</td>
						<td class="general-cell">""" + StringF_1161 + """</td>
						<td class="station">1241</td>
						<td class="special-cell">""" + StringA_1241 + """</td>
						<td class="general-cell">""" + StringB_1241 + """</td>
						<td class="special-cell">""" + StringC_1241 + """</td>
						<td class="general-cell">""" + StringD_1241 + """</td>
						<td class="special-cell">""" + StringE_1241 + """</td>
						<td class="general-cell">""" + StringF_1241 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1170</td>
						<td class="special-cell">""" + StringA_1170 + """</td>
						<td class="general-cell">""" + StringB_1170 + """</td>
						<td class="special-cell">""" + StringC_1170 + """</td>
						<td class="general-cell">""" + StringD_1170 + """</td>
						<td class="special-cell">""" + StringE_1170 + """</td>
						<td class="general-cell">""" + StringF_1170 + """</td>
						<td class="station">1245</td>
						<td class="special-cell">""" + StringA_1245 + """</td>
						<td class="general-cell">""" + StringB_1245 + """</td>
						<td class="special-cell">""" + StringC_1245 + """</td>
						<td class="general-cell">""" + StringD_1245 + """</td>
						<td class="special-cell">""" + StringE_1245 + """</td>
						<td class="general-cell">""" + StringF_1245 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1260</td>
						<td class="special-cell">""" + StringA_1260 + """</td>
						<td class="general-cell">""" + StringB_1260 + """</td>
						<td class="special-cell">""" + StringC_1260 + """</td>
						<td class="general-cell">""" + StringD_1260 + """</td>
						<td class="special-cell">""" + StringE_1260 + """</td>
						<td class="general-cell">""" + StringF_1260 + """</td>
					</tr>
					<!-- Add more rows here as needed -->
				</tbody>
			</table>
		</div>
		<div class = "table-container">
			<table class="block" id="blockDE">
				<thead>
					<tr>
						<th class="block-title" colspan="7">BLOCK D</th>
						<th class="block-title" colspan="7">BLOCK E</th>
					</tr>
					<tr class="header-row">
						<th class="header empty">Shift</th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty">Shift</th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
					</tr>
					<tr class="label-row">
						<th class="empty"></th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="empty"></th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
						<th class="highlight-blue">Qty</th>
						<th class="highlight">%NG</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td class="station">1300</td>
						<td class="special-cell">""" + StringA_1300 + """</td>
						<td class="general-cell">""" + StringB_1300 + """</td>
						<td class="special-cell">""" + StringC_1300 + """</td>
						<td class="general-cell">""" + StringD_1300 + """</td>
						<td class="special-cell">""" + StringE_1300 + """</td>
						<td class="general-cell">""" + StringF_1300 + """</td>
						<td class="station">1360</td>
						<td class="special-cell">""" + StringA_1360 + """</td>
						<td class="general-cell">""" + StringB_1360 + """</td>
						<td class="special-cell">""" + StringC_1360 + """</td>
						<td class="general-cell">""" + StringD_1360 + """</td>
						<td class="special-cell">""" + StringE_1360 + """</td>
						<td class="general-cell">""" + StringF_1360 + """</td>
					</tr>
					<tr>
						<td class="station">1310</td>
						<td class="special-cell">""" + StringA_1310 + """</td>
						<td class="general-cell">""" + StringB_1310 + """</td>
						<td class="special-cell">""" + StringC_1310 + """</td>
						<td class="general-cell">""" + StringD_1310 + """</td>
						<td class="special-cell">""" + StringE_1310 + """</td>
						<td class="general-cell">""" + StringF_1310 + """</td>
						<td class="station">1370</td>
						<td class="special-cell">""" + StringA_1370 + """</td>
						<td class="general-cell">""" + StringB_1370 + """</td>
						<td class="special-cell">""" + StringC_1370 + """</td>
						<td class="general-cell">""" + StringD_1370 + """</td>
						<td class="special-cell">""" + StringE_1370 + """</td>
						<td class="general-cell">""" + StringF_1370 + """</td>
					</tr>
					<tr>
						<td class="station">1320</td>
						<td class="special-cell">""" + StringA_1320 + """</td>
						<td class="general-cell">""" + StringB_1320 + """</td>
						<td class="special-cell">""" + StringC_1320 + """</td>
						<td class="general-cell">""" + StringD_1320 + """</td>
						<td class="special-cell">""" + StringE_1320 + """</td>
						<td class="general-cell">""" + StringF_1320 + """</td>
						<td class="station">1371</td>
						<td class="special-cell">""" + StringA_1371 + """</td>
						<td class="general-cell">""" + StringB_1371 + """</td>
						<td class="special-cell">""" + StringC_1371 + """</td>
						<td class="general-cell">""" + StringD_1371 + """</td>
						<td class="special-cell">""" + StringE_1371 + """</td>
						<td class="general-cell">""" + StringF_1371 + """</td>
					</tr>
					<tr>
						<td class="station">1720</td>
						<td class="special-cell">""" + StringA_1720 + """</td>
						<td class="general-cell">""" + StringB_1720 + """</td>
						<td class="special-cell">""" + StringC_1720 + """</td>
						<td class="general-cell">""" + StringD_1720 + """</td>
						<td class="special-cell">""" + StringE_1720 + """</td>
						<td class="general-cell">""" + StringF_1720 + """</td>
						<td class="station">1375</td>
						<td class="special-cell">""" + StringA_1375 + """</td>
						<td class="general-cell">""" + StringB_1375 + """</td>
						<td class="special-cell">""" + StringC_1375 + """</td>
						<td class="general-cell">""" + StringD_1375 + """</td>
						<td class="special-cell">""" + StringE_1375 + """</td>
						<td class="general-cell">""" + StringF_1375 + """</td>
					</tr>
					<tr>
						<td class="station">1730</td>
						<td class="special-cell">""" + StringA_1730 + """</td>
						<td class="general-cell">""" + StringB_1730 + """</td>
						<td class="special-cell">""" + StringC_1730 + """</td>
						<td class="general-cell">""" + StringD_1730 + """</td>
						<td class="special-cell">""" + StringE_1730 + """</td>
						<td class="general-cell">""" + StringF_1730 + """</td>
						<td class="station">1380</td>
						<td class="special-cell">""" + StringA_1380 + """</td>
						<td class="general-cell">""" + StringB_1380 + """</td>
						<td class="special-cell">""" + StringC_1380 + """</td>
						<td class="general-cell">""" + StringD_1380 + """</td>
						<td class="special-cell">""" + StringE_1380 + """</td>
						<td class="general-cell">""" + StringF_1380 + """</td>
					</tr>
					<tr>
						<td class="station">1340</td>
						<td class="special-cell">""" + StringA_1340 + """</td>
						<td class="general-cell">""" + StringB_1340 + """</td>
						<td class="special-cell">""" + StringC_1340 + """</td>
						<td class="general-cell">""" + StringD_1340 + """</td>
						<td class="special-cell">""" + StringE_1340 + """</td>
						<td class="general-cell">""" + StringF_1340 + """</td>
						<td class="station">1381</td>
						<td class="special-cell">""" + StringA_1381 + """</td>
						<td class="general-cell">""" + StringB_1381 + """</td>
						<td class="special-cell">""" + StringC_1381 + """</td>
						<td class="general-cell">""" + StringD_1381 + """</td>
						<td class="special-cell">""" + StringE_1381 + """</td>
						<td class="general-cell">""" + StringF_1381 + """</td>
					</tr>
					<tr>
						<td class="station">1341</td>
						<td class="special-cell">""" + StringA_1341 + """</td>
						<td class="general-cell">""" + StringB_1341 + """</td>
						<td class="special-cell">""" + StringC_1341 + """</td>
						<td class="general-cell">""" + StringD_1341 + """</td>
						<td class="special-cell">""" + StringE_1341 + """</td>
						<td class="general-cell">""" + StringF_1341 + """</td>
						<td class="station">1385</td>
						<td class="special-cell">""" + StringA_1385 + """</td>
						<td class="general-cell">""" + StringB_1385 + """</td>
						<td class="special-cell">""" + StringC_1385 + """</td>
						<td class="general-cell">""" + StringD_1385 + """</td>
						<td class="special-cell">""" + StringE_1385 + """</td>
						<td class="general-cell">""" + StringF_1385 + """</td>
					</tr>
					<tr>
						<td class="station">1345</td>
						<td class="special-cell">""" + StringA_1345 + """</td>
						<td class="general-cell">""" + StringB_1345 + """</td>
						<td class="special-cell">""" + StringC_1345 + """</td>
						<td class="general-cell">""" + StringD_1345 + """</td>
						<td class="special-cell">""" + StringE_1345 + """</td>
						<td class="general-cell">""" + StringF_1345 + """</td>
						<td class="station">1390</td>
						<td class="special-cell">""" + StringA_1390 + """</td>
						<td class="general-cell">""" + StringB_1390 + """</td>
						<td class="special-cell">""" + StringC_1390 + """</td>
						<td class="general-cell">""" + StringD_1390 + """</td>
						<td class="special-cell">""" + StringE_1390 + """</td>
						<td class="general-cell">""" + StringF_1390 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1398</td>
						<td class="special-cell">""" + StringA_1398 + """</td>
						<td class="general-cell">""" + StringB_1398 + """</td>
						<td class="special-cell">""" + StringC_1398 + """</td>
						<td class="general-cell">""" + StringD_1398 + """</td>
						<td class="special-cell">""" + StringE_1398 + """</td>
						<td class="general-cell">""" + StringF_1398 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1400</td>
						<td class="special-cell">""" + StringA_1400 + """</td>
						<td class="general-cell">""" + StringB_1400 + """</td>
						<td class="special-cell">""" + StringC_1400 + """</td>
						<td class="general-cell">""" + StringD_1400 + """</td>
						<td class="special-cell">""" + StringE_1400 + """</td>
						<td class="general-cell">""" + StringF_1400 + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1410</td>
						<td class="special-cell">""" + StringA_1410 + """</td>
						<td class="general-cell">""" + StringB_1410 + """</td>
						<td class="special-cell">""" + StringC_1410 + """</td>
						<td class="general-cell">""" + StringD_1410 + """</td>
						<td class="special-cell">""" + StringE_1410 + """</td>
						<td class="general-cell">""" + StringF_1410 + """</td>
					</tr>
					<!-- Add more rows here as needed -->
				</tbody>
			</table>
		</div>
        <div class = "table-container">
			<table class="block" id="blockDE">
				<thead>
					<tr>
						<th class="block-title" colspan="7">3rd Shift PCU Data</th>
						<th class="block-title" colspan="7">3rd Shift Top No Good</th>
					</tr>
					<tr class="header-row">
						<th class="header empty">  </th>
						<th class="headerWhite" colspan="2">Loaded</th>
						<th class="headerWhite" colspan="2">Total NG</th>
						<th class="headerWhite" colspan="2">NG %</th>
						<th class="header empty">  </th>
						<th class="headerWhite" colspan="2">Station</th>
						<th class="headerWhite" colspan="2">NG %</th>
						<th class="headerWhite" colspan="2">NG Count</th>
					</tr>
				</thead>
				<tbody>
					<tr>
	                    <td class="station">ALL PCU</td>
	                    <td class="white-cell" colspan="2">""" + StringA_ALL_PCU + """</td>
	                    <td class="white-cell" colspan="2">""" + StringB_ALL_PCU + """</td>
	                    <td class="white-cell" colspan="2">""" + StringC_ALL_PCU + """</td>
	                    <td class="station">1st</td>
	                    <td class="white-cell" colspan="2">""" + StationFirst_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFirst_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFirst_NGCount + """</td>
					</tr>
					<tr>
                        <td class="station">Block A</td>
                        <td class="gray-cell" colspan="2">""" + StringA_BlockA + """</td>
                        <td class="gray-cell" colspan="2">""" + StringB_BlockA + """</td>
                        <td class="gray-cell" colspan="2">""" + StringC_BlockA + """</td>
                        <td class="station">2nd</td>
	                    <td class="white-cell" colspan="2">""" + StationSecond_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationSecond_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationSecond_NGCount + """</td>
					</tr>
					<tr>
                        <td class="station">Block B</td>
                        <td class="white-cell" colspan="2">""" + StringA_BlockB + """</td>
                        <td class="white-cell" colspan="2">""" + StringB_BlockB + """</td>
                        <td class="white-cell" colspan="2">""" + StringC_BlockB + """</td>
                        <td class="station">3rd</td>
	                    <td class="white-cell" colspan="2">""" + StationThird_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationThird_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationThird_NGCount + """</td>
					</tr>
					<tr>
                        <td class="station">Block C</td>
                        <td class="gray-cell" colspan="2">""" + StringA_BlockC + """</td>
                        <td class="gray-cell" colspan="2">""" + StringB_BlockC + """</td>
                        <td class="gray-cell" colspan="2">""" + StringC_BlockC + """</td>
                        <td class="station">4th</td>
	                    <td class="white-cell" colspan="2">""" + StationFourth_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFourth_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFourth_NGCount + """</td>
					</tr>
					<tr>
                        <td class="station">Block D</td>
                        <td class="white-cell" colspan="2">""" + StringA_BlockD + """</td>
                        <td class="white-cell" colspan="2">""" + StringB_BlockD + """</td>
                        <td class="white-cell" colspan="2">""" + StringC_BlockD + """</td>
                        <td class="station">5th</td>
	                    <td class="white-cell" colspan="2">""" + StationFifth_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFifth_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationFifth_NGCount + """</td>
					</tr>
					<tr>
	                    <td class="station">Block E</td>
	                    <td class="gray-cell" colspan="2">""" + StringA_BlockE + """</td>
	                    <td class="gray-cell" colspan="2">""" + StringB_BlockE + """</td>
	                    <td class="gray-cell" colspan="2">""" + StringC_BlockE + """</td>
	                    <td class="station">6th</td>
	                    <td class="white-cell" colspan="2">""" + StationSixth_Number + """</td>
	                    <td class="white-cell" colspan="2">""" + StationSixth_NGPercent + """</td>
	                    <td class="white-cell" colspan="2">""" + StationSixth_NGCount + """</td>
					</tr>
					<!-- Add more rows here as needed -->
				</tbody>
			</table>
		</div>
	<body>
	</html>
	"""
	
	
	
	smtp = "sever"
	username = ""  # not required as smtpProfile is used
	sender = "email"
	password = "password"
	subject = "PCU Automated Email"
	body = "PCU Reject Data From Date: " + todays_date + " Time: " + current_time + "\n\n" + html_content.strip()
	
	
	#recipients = []
	
	recipients = []
	system.net.sendEmail(smtp=smtp, fromAddr=sender, subject=subject, body=body,html=1, to=recipients, password=password)	
