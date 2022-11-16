
# import libraries
from GoogleImage import GoogleImageScraper
import os


if __name__ == "__main__":
    # paths for driver
    webdriver_path = os.path.normpath(os.getcwd()+"\\webdriver\\chromedriver.exe")
    image_path = os.path.normpath(os.getcwd()+"\\mercedes-benz-15112022-2")

    #Add new search key into array 
    search_keys= [
                # "A-Class",
                # "B-Class",
                # "C-Class",
                # "CLA",
                # "CLS",
                # #"E-Class",
                # "G-Class",
                # "GLA",
                # "GLB",
                # "GLC",
                # "GLE",
                # "GLS",
                # "S-Class",
                # "SL",
                # "V-Class",
                # "EQA",
                # "EQB",
                # "EQC",
                # "EQE",
                # "EQS SUV",
                # "EQS",
                # "EQV",
                #"T-Class",
                #"smart",
                #"AMG GT",
                #"Sprinter",
                #"Citan",
                #"Vito",
                "Marco Polo Mercedes-Benz"]

    # parameters
    number = 300
    headless = False
    min_res=(0,0)
    max_res=(9999,9999)

    # main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number,headless,min_res,max_res)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls, keep_filenames=False)
    
    # release resources    
    del image_scrapper
