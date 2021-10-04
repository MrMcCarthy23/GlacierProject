from selenium import webdriver as wb
from selenium.webdriver import FirefoxOptions
import time
#def get_shot(filename,url):


url = 'https://www.nps.gov/webcams-glac/ApgarLookout-01.jpg?1633201317362'
	
path = '/home/mrmark23/Pictures/Glacier_test/'

#open browser in headless mode
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = wb.Firefox(firefox_options = opts)
    
#create timestamp
tmp = time.strftime("%Y%m%d-%H%M")

#create file path w/ tmp
filename2 = path+tmp+'.png'

driver.get(url)

#take screenshot as file at filename
driver.get_screenshot_as_file(filename2)

driver.close()
#return 
###############MAIN FUNCTION###################  


#get screenshot from web, save localy, and flickr pro account auto uploads
#get_shot(path,url)

