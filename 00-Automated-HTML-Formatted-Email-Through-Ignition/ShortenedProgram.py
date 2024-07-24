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

#formatting block values
def format_value(value):
	if value == 0:
		return "0"
	elif isinstance(value, int):
		return "{:.0f}".format(value)
	else:
		return"{:.2f}".format(value)
		
#formatting counts for top no good and General PCU Data   
def format_quantity(value):
	return "0" if value == 0 else "{:.0f}".format(value)
	
#removing the A from A1030 for station number in Top No Good	
def format_station(station):
	return station[1:]
	
def create_station_object(block, station_number):
	base_path = "Block {}/Station {}/Data/Dashboard/"
	tag_paths = {
		"NGPart1st": base_path.format(block, station_number) + "NGParts/NGPart1st",
		"NGPercent1st": base_path.format(block, station_number) + "NG Percent 1st",
		"NGPart2nd": base_path.format(block, station_number) + "NGParts/NGPart2nd",
		"NGPercent2nd": base_path.format(block, station_number) + "NG Percent 2nd",
		"NGPart3rd": base_path.format(block, station_number) + "NGParts/NGPart3rd",
		"NGPercent3rd": base_path.format(block, station_number) + "NG Percent 3rd"
	}
	
	tag_values = {key: system.tag.readBlocking([tag_paths[key]])[0].value for key in tag_paths}

	station_object = StationObject(
		"{}{}".format(block, station_number),
		tag_values["NGPart1st"],
		tag_values["NGPercent1st"],
		tag_values["NGPart2nd"],
		tag_values["NGPercent2nd"],
		tag_values["NGPart3rd"],
		tag_values["NGPercent3rd"]
	)

	return station_object
	
	
def Main():
	
	#Getting Times & Dates
	todays_date = datetime.date.today().strftime('_%m_%d_%y')
	current_time = datetime.datetime.now().strftime('_%H_%M')
    
	#Station Object Array
	block_station_mapping = {
	# 		  0		1	  2		3	  4		5	  6		7	  8 	9	  10  
    	"A": [1016, 1020, 1030, 1040, 1048, 1050, 1060, 1070, 1071, 1072, 1080],
    # 		  11	12	  13	14	  15	16	  17	18	  19 	20	  21    22	  23 	24
    	"B": [1100, 1101, 1110, 1120, 1500, 1510, 1515, 1530, 1140, 1142, 1150, 1160, 1161, 1170],
    # 		  25	26	  27	28	  29	30	  31	32 	  33	34    35	36	  37    38
    	"C": [1180, 1200, 1205, 1210, 1620, 1630, 1640, 1650, 1220, 1230, 1240, 1241, 1245, 1260],
    # 		  39	40	  41	42	  43	44	  45	46
    	"D": [1300, 1310, 1320, 1720, 1730, 1340, 1341, 1345],
    # 		  47	48	  49	50	  51	52	  53	54 	  55	56    57    58
    	"E": [1360, 1365, 1370, 1371, 1375, 1380, 1381, 1385, 1390, 1398, 1400, 1410]
	}
	
	StationObjectArray = []
    
	# Populate StationObjectArray with StationObject instances
	for block, stations in block_station_mapping.items():
		for station_number in stations:
			StationObjectArray.append(create_station_object(block, station_number))

	#excluding stations from the TOP NO GOOD
	excluded_stations = {"B1101", "A1016"}
	valid_station_objects = [obj for obj in StationObjectArray if isinstance(obj, StationObject) and str(obj.Station).strip() not in excluded_stations]
		
	#Time Based Top No Good Data
	OrderedObjectArray = sorted(valid_station_objects, key=lambda x:x.NGF, reverse=True)
	
	
#PRINT STATEMENT FOR TESTING VALUE OUTPUTS - just delete the """ at the front and start of comment to test
	"""for station_obj in StationObjectArray:
		# Extract the block and station_number from the Station attribute
		block = station_obj.Station[0]  # Extracts the first character (block letter)
		station_number = station_obj.Station[1:]  # Extracts all characters after the first (station number)
	
		# Print block and station_number along with NG values
		print("Block: {}, Station: {}, NGA: {}, NGB: {}, NGC: {}, NGD: {}, NGE: {}, NGF: {}".format(
			block, station_number,
			station_obj.NGA, station_obj.NGB,
			station_obj.NGC, station_obj.NGD,
			station_obj.NGE, station_obj.NGF))"""

		
	#PARTS
	#Block {2}/Station {1}/Data/Dashboard/NGParts/NGPart1st.value
	
	#PERCENTS
	#Block {1}/Station {2}/Data/Dashboard/NG Percent 1st
	
	#General PCU Data
	#Block A
	#1st Column
	TagPathNGA_BlockA = "StationStatus/BlockA/Counts/Sta1016TotalParts"
	TagNGA_BlockA_value = system.tag.readBlocking([TagPathNGA_BlockA])[0].value
	StringA_BlockA = format_quantity(TagNGA_BlockA_value)
	
	#2nd Column
	TagPathNGB_BlockA = "StationStatus/BlockA/Counts/TotalNoGoodCount"
	TagNGB_BlockA_value = system.tag.readBlocking([TagPathNGB_BlockA])[0].value
	StringB_BlockA = format_quantity(TagNGB_BlockA_value)
	
	#3rd Column
	if (TagNGA_BlockA_value != 0):
		PercentNGC_BlockA = ((float(TagNGB_BlockA_value) / TagNGA_BlockA_value)*100)
		StringC_BlockA = format_value(PercentNGC_BlockA)
	else:
		StringC_BlockA = "0"
	#/Block A
	
	
	
	#Block B
	#1st Column
	TagPathNGA_BlockB = "StationStatus/BlockB/Counts/Sta1100TotalParts"
	TagNGA_BlockB_value = system.tag.readBlocking([TagPathNGA_BlockB])[0].value
	StringA_BlockB = format_quantity(TagNGA_BlockB_value)
	
	#2nd Column
	TagPathNGB_BlockB = "StationStatus/BlockB/Counts/TotalNoGoodCount"
	TagNGB_BlockB_value = system.tag.readBlocking([TagPathNGB_BlockB])[0].value
	StringB_BlockB = format_quantity(TagNGB_BlockB_value)
	
	#3rd Column
	if (TagNGA_BlockB_value != 0):
		PercentNGC_BlockB = ((float(TagNGB_BlockB_value) / TagNGA_BlockB_value)*100)
		StringC_BlockB = format_value(PercentNGC_BlockB)
	else:
		StringC_BlockB = "0"
	#/Block B	
		
	#Block C
	#1st Column
	TagPathNGA_BlockC = "StationStatus/BlockC/Counts/Sta1180TotalParts"
	TagNGA_BlockC_value = system.tag.readBlocking([TagPathNGA_BlockC])[0].value
	StringA_BlockC = format_quantity(TagNGA_BlockC_value)
	
	#2nd Column
	TagPathNGB_BlockC = "StationStatus/BlockC/Counts/TotalNoGoodCount"
	TagNGB_BlockC_value = system.tag.readBlocking([TagPathNGB_BlockC])[0].value
	StringB_BlockC = format_quantity(TagNGB_BlockC_value)
	
	#3rd Column
	if (TagNGA_BlockC_value != 0):
		PercentNGC_BlockC = ((float(TagNGB_BlockC_value) / TagNGA_BlockC_value)*100)
		StringC_BlockC = format_value(PercentNGC_BlockC)
	else:
		StringC_BlockC = "0"
	#/Block C	
	
	#Block D
	#1st Column
	TagPathNGA_BlockD = "StationStatus/BlockD/Counts/Sta1300TotalParts"
	TagNGA_BlockD_value = system.tag.readBlocking([TagPathNGA_BlockD])[0].value
	StringA_BlockD = format_quantity(TagNGA_BlockD_value)
	
	#2nd Column
	TagPathNGB_BlockD = "StationStatus/BlockD/Counts/TotalNoGoodCount"
	TagNGB_BlockD_value = system.tag.readBlocking([TagPathNGB_BlockD])[0].value
	StringB_BlockD = format_quantity(TagNGB_BlockD_value)
	
	#3rd Column
	if (TagNGA_BlockD_value != 0):
		PercentNGC_BlockD = ((float(TagNGB_BlockD_value) / TagNGA_BlockD_value)*100)
		StringC_BlockD = format_value(PercentNGC_BlockD)
	else:
		StringC_BlockD = "0"
	#/Block D	
	
	#Block E
	#1st Column
	TagPathNGA_BlockE = "StationStatus/BlockE/Counts/Sta1360TotalParts"
	TagNGA_BlockE_value = system.tag.readBlocking([TagPathNGA_BlockE])[0].value
	StringA_BlockE = format_quantity(TagNGA_BlockE_value)
	
	#2nd Column
	TagPathNGB_BlockE = "StationStatus/BlockE/Counts/TotalNoGoodCount"
	TagNGB_BlockE_value = system.tag.readBlocking([TagPathNGB_BlockE])[0].value
	StringB_BlockE = format_quantity(TagNGB_BlockE_value)
	
	#3rd Column
	if (TagNGA_BlockE_value != 0):
		PercentNGC_BlockE = ((float(TagNGB_BlockE_value) / TagNGA_BlockE_value) * 100)
		StringC_BlockE = format_value(PercentNGC_BlockE)
	else:
		StringC_BlockE = "0"
	#/Block E	
	
	#All PCU
	#1st Column
	TagPathNGA_ALL_PCU = "stuffStationStatus/BlockA/Counts/Sta1016TotalParts"
	TagNGA_ALL_PCU_value = system.tag.readBlocking([TagPathNGA_ALL_PCU])[0].value
	StringA_ALL_PCU = format_quantity(TagNGA_ALL_PCU_value)
	
	#2nd Column
	TagPathNGB_ALL_PCU = "stuffStationStatus/TotalNoGoodCount"
	TagNGB_ALL_PCU_value = system.tag.readBlocking([TagPathNGB_ALL_PCU])[0].value
	StringB_ALL_PCU = format_quantity(TagNGB_ALL_PCU_value)
	
	#3rd Column
	if (TagNGA_ALL_PCU_value != 0):
		PercentNGC_ALL_PCU = ((float(TagNGB_ALL_PCU_value)/ TagNGA_ALL_PCU_value)*100)
		StringC_ALL_PCU = format_value(PercentNGC_ALL_PCU)
	else:
		StringC_ALL_PCU = "0"
	#/All PCU
	
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
						<th class="header empty"></th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty"></th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty"></th>
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
						<td class="special-cell">""" + format_value(StationObjectArray[0].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[0].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[0].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[0].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[0].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[0].NGF) + """</td>
						<td class="station">1100</td>
						<td class="special-cell">""" + format_value(StationObjectArray[11].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[11].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[11].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[11].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[11].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[11].NGF) + """</td>
						<td class="station">1180</td>
						<td class="special-cell">""" + format_value(StationObjectArray[25].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[25].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[25].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[25].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[25].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[25].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1020</td>
						<td class="special-cell">""" + format_value(StationObjectArray[1].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[1].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[1].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[1].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[1].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[1].NGF) + """</td>
						<td class="station">1101</td>						
						<td class="special-cell">""" + format_value(StationObjectArray[12].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[12].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[12].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[12].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[12].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[12].NGF) + """</td>
						<td class="station">1200</td>
						<td class="special-cell">""" + format_value(StationObjectArray[26].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[26].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[26].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[26].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[26].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[26].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1030</td>
						<td class="special-cell">""" + format_value(StationObjectArray[2].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[2].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[2].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[2].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[2].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[2].NGF) + """</td>
						<td class="station">1110</td>
						<td class="special-cell">""" + format_value(StationObjectArray[13].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[13].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[13].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[13].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[13].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[13].NGF) + """</td>
						<td class="station">1205</td>
						<td class="special-cell">""" + format_value(StationObjectArray[27].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[27].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[27].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[27].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[27].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[27].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1040</td>
						<td class="special-cell">""" + format_value(StationObjectArray[3].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[3].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[3].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[3].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[3].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[3].NGF) + """</td>
						<td class="station">1120</td>
						<td class="special-cell">""" + format_value(StationObjectArray[14].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[14].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[14].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[14].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[14].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[14].NGF) + """</td>
						<td class="station">1210</td>
						<td class="special-cell">""" + format_value(StationObjectArray[28].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[28].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[28].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[28].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[28].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[28].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1048</td>
						<td class="special-cell">""" + format_value(StationObjectArray[4].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[4].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[4].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[4].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[4].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[4].NGF) + """</td>
						<td class="station">1500</td>
						<td class="special-cell">""" + format_value(StationObjectArray[15].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[15].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[15].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[15].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[15].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[15].NGF) + """</td>
						<td class="station">1230</td>
						<td class="special-cell">""" + format_value(StationObjectArray[29].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[29].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[29].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[29].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[29].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[29].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1050</td>
						<td class="special-cell">""" + format_value(StationObjectArray[5].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[5].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[5].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[5].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[5].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[5].NGF) + """</td>
						<td class="station">1510</td>
						<td class="special-cell">""" + format_value(StationObjectArray[16].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[16].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[16].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[16].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[16].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[16].NGF) + """</td>
						<td class="station">1630</td>
						<td class="special-cell">""" + format_value(StationObjectArray[30].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[30].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[30].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[30].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[30].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[30].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1060</td>
						<td class="special-cell">""" + format_value(StationObjectArray[6].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[6].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[6].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[6].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[6].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[6].NGF) + """</td>
						<td class="station">1515</td>
						<td class="special-cell">""" + format_value(StationObjectArray[17].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[17].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[17].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[17].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[17].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[17].NGF) + """</td>
						<td class="station">1640</td>
						<td class="special-cell">""" + format_value(StationObjectArray[31].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[31].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[31].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[31].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[31].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[31].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1070</td>
						<td class="special-cell">""" + format_value(StationObjectArray[7].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[7].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[7].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[7].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[7].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[7].NGF) + """</td>
						<td class="station">1530</td>
						<td class="special-cell">""" + format_value(StationObjectArray[18].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[18].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[18].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[18].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[18].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[18].NGF) + """</td>
						<td class="station">1650</td>
						<td class="special-cell">""" + format_value(StationObjectArray[32].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[32].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[32].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[32].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[32].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[32].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1071</td>
						<td class="special-cell">""" + format_value(StationObjectArray[8].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[8].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[8].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[8].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[8].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[8].NGF) + """</td>
						<td class="station">1140</td>
						<td class="special-cell">""" + format_value(StationObjectArray[19].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[19].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[19].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[19].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[19].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[19].NGF) + """</td>
						<td class="station">1220</td>
						<td class="special-cell">""" + format_value(StationObjectArray[33].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[33].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[33].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[33].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[33].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[33].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1072</td>
						<td class="special-cell">""" + format_value(StationObjectArray[9].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[9].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[9].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[9].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[9].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[9].NGF) + """</td>
						<td class="station">1142</td>
						<td class="special-cell">""" + format_value(StationObjectArray[20].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[20].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[20].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[20].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[20].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[20].NGF) + """</td>
						<td class="station">1230</td>
						<td class="special-cell">""" + format_value(StationObjectArray[34].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[34].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[34].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[34].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[34].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[34].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1080</td>
						<td class="special-cell">""" + format_value(StationObjectArray[10].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[10].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[10].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[10].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[10].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[10].NGF) + """</td>
						<td class="station">1150</td>
						<td class="special-cell">""" + format_value(StationObjectArray[21].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[21].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[21].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[21].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[21].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[21].NGF) + """</td>
						<td class="station">1240</td>
						<td class="special-cell">""" + format_value(StationObjectArray[35].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[35].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[35].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[35].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[35].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[35].NGF) + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1160</td>
						<td class="special-cell">""" + format_value(StationObjectArray[22].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[22].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[22].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[22].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[22].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[22].NGF) + """</td>
						<td class="station">1241</td>
						<td class="special-cell">""" + format_value(StationObjectArray[36].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[36].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[36].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[36].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[36].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[36].NGF) + """</td>
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
						<td class="special-cell">""" + format_value(StationObjectArray[23].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[23].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[23].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[23].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[23].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[23].NGF) + """</td>
						<td class="station">1245</td>
						<td class="special-cell">""" + format_value(StationObjectArray[37].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[37].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[37].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[37].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[37].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[37].NGF) + """</td>
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
						<td class="special-cell">""" + format_value(StationObjectArray[24].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[24].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[24].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[24].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[24].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[24].NGF) + """</td>
						<td class="station">1260</td>
						<td class="special-cell">""" + format_value(StationObjectArray[38].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[38].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[38].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[38].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[38].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[38].NGF) + """</td>
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
						<th class="header empty"></th>
						<th class="header" colspan="2">1st</th>
						<th class="header" colspan="2">2nd</th>
						<th class="header" colspan="2">3rd</th>
						<th class="header empty"></th>
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
						<td class="special-cell">""" + format_value(StationObjectArray[39].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[39].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[39].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[39].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[39].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[39].NGF) + """</td>
						<td class="station">1360</td>
						<td class="special-cell">""" + format_value(StationObjectArray[47].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[47].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[47].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[47].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[47].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[47].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1310</td>
						<td class="special-cell">""" + format_value(StationObjectArray[40].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[40].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[40].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[40].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[40].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[40].NGF) + """</td>
						<td class="station">1365</td>
						<td class="special-cell">""" + format_value(StationObjectArray[48].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[48].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[48].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[48].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[48].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[48].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1320</td>
						<td class="special-cell">""" + format_value(StationObjectArray[41].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[41].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[41].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[41].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[41].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[41].NGF) + """</td>
						<td class="station">1370</td>
						<td class="special-cell">""" + format_value(StationObjectArray[49].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[49].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[49].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[49].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[49].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[49].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1720</td>
						<td class="special-cell">""" + format_value(StationObjectArray[42].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[42].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[42].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[42].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[42].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[42].NGF) + """</td>
						<td class="station">1371</td>
						<td class="special-cell">""" + format_value(StationObjectArray[50].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[50].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[50].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[50].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[50].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[50].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1730</td>
						<td class="special-cell">""" + format_value(StationObjectArray[43].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[43].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[43].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[43].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[43].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[43].NGF) + """</td>
						<td class="station">1375</td>
						<td class="special-cell">""" + format_value(StationObjectArray[51].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[51].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[51].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[51].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[51].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[51].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1340</td>
						<td class="special-cell">""" + format_value(StationObjectArray[44].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[44].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[44].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[44].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[44].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[44].NGF) + """</td>
						<td class="station">1380</td>
						<td class="special-cell">""" + format_value(StationObjectArray[52].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[52].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[52].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[52].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[52].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[52].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1341</td>
						<td class="special-cell">""" + format_value(StationObjectArray[45].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[45].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[45].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[45].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[45].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[45].NGF) + """</td>
						<td class="station">1381</td>
						<td class="special-cell">""" + format_value(StationObjectArray[53].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[53].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[53].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[53].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[53].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[53].NGF) + """</td>
					</tr>
					<tr>
						<td class="station">1345</td>
						<td class="special-cell">""" + format_value(StationObjectArray[46].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[46].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[46].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[46].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[46].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[46].NGF) + """</td>
						<td class="station">1385</td>
						<td class="special-cell">""" + format_value(StationObjectArray[54].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[54].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[54].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[54].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[54].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[54].NGF) + """</td>
					</tr>
					<tr>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="empty"></td>
						<td class="station">1390</td>
						<td class="special-cell">""" + format_value(StationObjectArray[55].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[55].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[55].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[55].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[55].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[55].NGF) + """</td>
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
						<td class="special-cell">""" + format_value(StationObjectArray[56].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[56].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[56].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[56].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[56].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[56].NGF) + """</td>
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
						<td class="special-cell">""" + format_value(StationObjectArray[57].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[57].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[57].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[57].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[57].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[57].NGF) + """</td>
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
						<td class="special-cell">""" + format_value(StationObjectArray[58].NGA) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[58].NGB) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[58].NGC) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[58].NGD) + """</td>
						<td class="special-cell">""" + format_value(StationObjectArray[58].NGE) + """</td>
						<td class="general-cell">""" + format_value(StationObjectArray[58].NGF) + """</td>
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
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[0].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[0].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[0].NGE) + """</td>
					</tr>
					<tr>
                        <td class="station">Block A</td>
                        <td class="gray-cell" colspan="2">""" + StringA_BlockA + """</td>
                        <td class="gray-cell" colspan="2">""" + StringB_BlockA + """</td>
                        <td class="gray-cell" colspan="2">""" + StringC_BlockA + """</td>
                        <td class="station">2nd</td>
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[1].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[1].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[1].NGE) + """</td>
					</tr>
					<tr>
                        <td class="station">Block B</td>
                        <td class="white-cell" colspan="2">""" + StringA_BlockB + """</td>
                        <td class="white-cell" colspan="2">""" + StringB_BlockB + """</td>
                        <td class="white-cell" colspan="2">""" + StringC_BlockB + """</td>
                        <td class="station">3rd</td>
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[2].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[2].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[2].NGE) + """</td>
					</tr>
					<tr>
                        <td class="station">Block C</td>
                        <td class="gray-cell" colspan="2">""" + StringA_BlockC + """</td>
                        <td class="gray-cell" colspan="2">""" + StringB_BlockC + """</td>
                        <td class="gray-cell" colspan="2">""" + StringC_BlockC + """</td>
                        <td class="station">4th</td>
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[3].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[3].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[3].NGE) + """</td>
					</tr>
					<tr>
                        <td class="station">Block D</td>
                        <td class="white-cell" colspan="2">""" + StringA_BlockD + """</td>
                        <td class="white-cell" colspan="2">""" + StringB_BlockD + """</td>
                        <td class="white-cell" colspan="2">""" + StringC_BlockD + """</td>
                        <td class="station">5th</td>
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[4].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[4].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[4].NGE) + """</td>
					</tr>
					<tr>
	                    <td class="station">Block E</td>
	                    <td class="gray-cell" colspan="2">""" + StringA_BlockE + """</td>
	                    <td class="gray-cell" colspan="2">""" + StringB_BlockE + """</td>
	                    <td class="gray-cell" colspan="2">""" + StringC_BlockE + """</td>
	                    <td class="station">6th</td>
	                    <td class="white-cell" colspan="2">""" + format_station(OrderedObjectArray[5].Station) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_value(OrderedObjectArray[5].NGF) + """</td>
	                    <td class="white-cell" colspan="2">""" + format_quantity(OrderedObjectArray[5].NGE) + """</td>
					</tr>
					<!-- Add more rows here as needed -->
				</tbody>
			</table>
		</div>
	<body>
	</html>
	"""
	
	
	
	smtp = ""
	username = ""  # not required as smtpProfile is used
	sender = "aom"
	password = "password"
	subject = "PCU Automated Email"
	body = "PCU Reject Data From Date: " + todays_date + " Time: " + current_time + "\n\n" + html_content.strip()
	
	
	#recipients = [""]
	
	recipients = [""]
	
	system.net.sendEmail(smtp=smtp, fromAddr=sender, subject=subject, body=body,html=1, to=recipients, password=password)	
