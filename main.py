# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os


if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\photos")

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    # 'Mercedes-Benz A-Class 2004', 'Mercedes-Benz A-Class 2012', 'Mercedes-Benz A-Class 2018' done
    # 'Mercedes-Benz B-Class 2005', 'Mercedes-Benz B-Class 2011', 'Mercedes-Benz B-Class 2019' done
    # 'Mercedes-Benz C-Class 2007', 'Mercedes-Benz C-Class 2014', 'Mercedes-Benz C-Class 2021' done
    # 'Mercedes-Benz CLA-Class 2013', 'Mercedes-Benz CLA-Class 2019' done but less data
    # 'Mercedes-Benz CLS-Class 2004', 'Mercedes-Benz CLS-Class 2011', 'Mercedes-Benz CLS-Class 2018'  
    # 'Mercedes-Benz E-Class 2002', 'Mercedes-Benz E-Class 2009', 'Mercedes-Benz E-Class 2016' 
    # 'Mercedes-Benz G-Class 1990', 'Mercedes-Benz G-Class 2017' 
    # 'Mercedes-Benz S-Class 2005', 'Mercedes-Benz S-Class 2013', 'Mercedes-Benz S-Class 2020' 
    # 'Mercedes-Benz Sprinter 2006', 'Mercedes-Benz A-Class 2018'
    # 'Mercedes-Benz V-Class 2003', 'Mercedes-Benz A-Class 2014' 
    # 'Mercedes-Benz GLS-Class 2006', 'Mercedes-Benz GLS-Class 2012', 'Mercedes-Benz GLS-Class 2019' 
    # 'Mercedes-Benz GLE-Class 2005', 'Mercedes-Benz GLE-Class 2011', 'Mercedes-Benz GLE-Class 2019' 
    search_keys= ['Mercedes-Benz CLA-Class 2013', 'Mercedes-Benz CLA-Class 2019']

    #Parameters
    number_of_images = 100
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
    
    #Release resources    
    del image_scrapper