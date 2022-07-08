
# import libraries
from GoogleImage import GoogleImage
import os


if __name__ == "__main__":
    # paths for driver
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\mercedes-benz-okt")

    #Add new search key into array 
    search_keys= [
                'Mercedes-Benz A-Class 2004', 'Mercedes-Benz A-Class 2012', 'Mercedes-Benz A-Class 2018',
                 'Mercedes-Benz B-Class 2005', 'Mercedes-Benz B-Class 2011', 'Mercedes-Benz B-Class 2019',
                   'Mercedes-Benz C-Class 2007', 'Mercedes-Benz C-Class 2014', 'Mercedes-Benz C-Class 2021',
                   'Mercedes-Benz CLA-Class 2013', 'Mercedes-Benz CLA-Class 2019',
                   'Mercedes-Benz CLS-Class 2004', 'Mercedes-Benz CLS-Class 2011', 'Mercedes-Benz CLS-Class 2018' , 
                   'Mercedes-Benz E-Class 2002', 'Mercedes-Benz E-Class 2009', 'Mercedes-Benz E-Class 2016', 
                   'Mercedes-Benz G-Class 1990', 'Mercedes-Benz G-Class 2017', 
                   'Mercedes-Benz S-Class 2005', 'Mercedes-Benz S-Class 2013', 'Mercedes-Benz S-Class 2020' ,
                   'Mercedes-Benz Sprinter 2006', 'Mercedes-Benz Sprinter-Class 2018',
                   'Mercedes-Benz V-Class 2003', 'Mercedes-Benz V-Class 2014', 
                   'Mercedes-Benz GLS-Class 2006', 'Mercedes-Benz GLS-Class 2012', 'Mercedes-Benz GLS-Class 2019', 
                   'Mercedes-Benz GLE-Class 2005', 'Mercedes-Benz GLE-Class 2011', 'Mercedes-Benz GLE-Class 2019 
                'Mercedes-Benz C-Class 2007', 'Mercedes-Benz C-Class 2021', 'Mercedes-Benz CLA-Class 2013', 'Mercedes-Benz E-Class 2009']

    # parameters
    number = 300
    headless = False
    min_res=(0,0)
    max_res=(9999,9999)

    # main program
    for search_key in search_keys:
        image_scrapper = GoogleImage(webdriver_path,image_path,search_key,number,headless,min_res,max_res)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
    
    # release resources    
    del image_scrapper