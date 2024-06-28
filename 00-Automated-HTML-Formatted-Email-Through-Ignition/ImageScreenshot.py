
from java.io import File
from javax.imageio import ImageIO


#importing the Time library for the date and the time.
from time import sleep 
import datetime

# Importing the necessary modules for email sending
from java.nio.file import Files
from java.nio.file import Paths
def Main():

	system.nav.openWindow('Popups/DashboardRejects')
	print('opened')
	window = system.gui.getWindow("Popups/DashboardRejects")
	#component = window.rootContainer.getComponent("Button 4")
	#component = event.source.parent
	bufferedImage = system.print.createImage(window)
	
	#Getting the correct file name
	todays_date = datetime.date.today().strftime('_%y_%m_%d__')
	current_time = datetime.datetime.now().strftime('%H_%M')
	new_filename = "Third_Rejects_Date" + todays_date + "Time_" + current_time + ".jpg" 
	   
	rawPath = "\\\path\\path\\path\\02 Dashboard Outputs\\03 Third Shift Rejects\\" + new_filename 
	
	FormattedPath = File(rawPath) 
	 
	ImageIO.write(bufferedImage , "jpg", FormattedPath)
	
	print('closing')
	system.nav.closeWindow('Popups/DashboardRejects')
	
	
	
