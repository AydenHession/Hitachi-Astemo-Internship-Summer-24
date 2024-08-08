from java.io import File
from javax.imageio import ImageIO

#importing the Time library for the date and the time. 
from time import sleep
import datetime

# Importing the necessary modules for email sending
from java.nio.file import Files
from java.nio.file import Paths

def Main():

	send_text = False
	
	tags = [
		#Regular Help Call Buttons
		("Source/Block A/Station 1010/Mode/Station 1010/CallPB", "Regular", "1010"),
		("Source/Block A/Station 1040/Mode/Station 1040/CallPB", "Regular", "1040"),
		("Source/Block B/Station 1100/Mode/Station 1100/CallPB", "Regular", "1100"),
		("Source/Block B/Station 1530/Mode/Station 1530/CallPB", "Regular", "1530"),
		("Source/Block B/Station 1160/Mode/Station 1160/CallPB", "Regular", "1160"),
		("Source/Block C/Station 1640/Mode/Station 1640/CallPB", "Regular", "1640"),
		("Source/Block D/Station 1310/Mode/Station 1310/CallPB", "Regular", "1310"),
		("Souce/Block E/Station 1398/Mode/Station 1398/CallPB", "Regular", "1398"),
		#Quality Help Call Buttons
		("Source/Block A/Station 1010/Mode/BlockA_Front_Help_CallPB_Quality", "Quality", "1010"),
		("Source/Block A/Station 1040/Mode/BlockA_Middle_Help_CallPB_Quality", "Quality", "1040"),
		("Source/Block B/Station 1100/Mode/BlockB_Beginning_Help_CallPB_Quality", "Quality", "1100"),
		("Source/Block B/Station 1530/Mode/BlockB_Middle_Help_CallPB_Quality", "Quality", "1530"),
		("Source/Block B/Station 1160/Mode/BlockB_Back_Help_CallPB_Quality", "Quality", "1160"),
		("Source/Block C/Station 1640/Mode/BlockC_Help_CallPB_Quality", "Quality", "1640"),
		("Source/Block D/Station 1310/Mode/BlockD_Help_CallPB_Quality", "Quality", "1310"),
		("Source/Block E/Station 1398/Mode/BlockE_Help_CallPB_Quality", "Quality", "1398")
	]

	
	#Getting Times & Dates
	todays_date = datetime.date.today().strftime('_%m_%d_%y')
	current_time = datetime.datetime.now().strftime('_%H_%M')
	current_hour = datetime.datetime.now().hour
	
	
	#First shift if 6 <= current_hour < 14:
	#Second shift if 14 <= current_hour < 22:
	#Third shift if current_hour >= 22 or current_hour < 6:
	if 14 <= current_hour < 22:
		send_text = True
	
	#Can Format Like This For Multiple People For Differing Time Frames	
	#if 6 <= current_hour < 14:
	#		send_text = True
	#		recipients = ["phone@txt.att.net", "phone@tmomail.net", "phone@vtext.net"]
	
	
	#print (current_hour)
	#if the time is correct, then check the stations
	if send_text:
		smtp = "_____.com"
		username = ""  # not required as smtpProfile is used
		sender = "____________@hitachiastemo.com"
		password = "password"
		subject = ""
		body = " "
		
		for tagPath, helpType, station in tags:
			if system.tag.read(tagPath).value:  # Assuming you're reading the tag like this
				body += "Station " +station + " " + helpType +  " Help Call At " + current_time + "\n"
		
		
		recipients = ["__________@tmomail.net"]
		
		if "Help Call" in body:
			system.net.sendEmail(smtp=smtp, fromAddr=sender, subject=subject, body=body,html=0, to=recipients, password=password)	
