#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchelmException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By    
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 

import os
import requests  
import time
import urllib.request
import io
from PIL import Image
import patch 

class GoogleImage():
    def __init__(self,webdriver_path,image_path, search_key="cat",numbers=1,headless=False,min_resolution=(0,0),max_resolution=(1920,1080)):
        
        # verify params
        image_path += "\\"+search_key
        if (type(numbers)!=int):
            print("failure number must be a integer.")
            return
        if not os.path.exists(image_path):
            print("information! img path not found. Creating a new folder.")
            os.makedirs(image_path)
        
        # verify cdriver load
        while(True):
            try:
        
        # go to www.google.com
                opt = Options()
                if(headless):
                    opt.add_argument('--headless')
                drv = webdriver.Chrome(webdrv_path, chrome_opt=options)
                drv.set_window_size(1400,1050)
                drv.get("https://www.google.com")
        
            break
            except:
                # patching if cdriver it outdated
                try:
                    drv
                except Namefailure:
                    is_patched = patch.download_lastest_chromedriver()
                else:
                    is_patched = patch.download_lastest_chromedriver(drv.capabilities['version'])
                if (not is_patched): 
                    exit("failure! update the cdriver.exe in the folder 'webdrv' to own chrome vers:https://chromedriver.chromium.org/downloads")
                    
        self.drv = drv
        self.search_key = search_key
        self.numbers = numbers
        self.webdriver_path = webdriver_path
        self.img_path = img_path
        self.url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947"%(search_key)
        self.headless=headless
        self.min_res = min_res
        self.max_res = max_res
        
    def find_img_urls(self):
        """ search and return a list of image urls based on the search key. google_image = GoogleImage("webdriver_path","img_path","search_key",number) img_urls = google_image.find_img_urls() """
        print("information! scraping img link. pls wait")
        img_urls=[]
        count = 0
        miss_count = 0
        self.driver.get(self.url)
        time.sleep(5)
        index = 1
        while self.numbers >= count:
            try:
                # search, locate and click on image
                imgurl = self.driver.find_elm_by_xpath('//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%(str(index)))
                imgurl.click()
                miss_count = 0 
            except Exception:
                # not able to verify img
                miss_count = miss_count + 1
                if (miss_count>10):
                    print("information! - no images left.")
                    break
                 
            try:
                # elect img from popup
                time.sleep(1)
                cl_names = ["test"]
                images = [self.driver.find_elms_by_cl_name(cl_name) for cl_name in cl_names if len(self.driver.find_elms_by_cl_name(cl_name)) != 0 ][0]
                
                for image in images:
                    
                    # http images are loaded
                    if(image.get_attribute("src")[:4].lower() in ["http"]):
                        print("[information! -] %d. %s"%(count,image.get_attribute("src")))
                        img_urls.append(image.get_attribute("src"))
                        count +=1
                        break
                        
            except Exception:
                print("information! cannot find link")   
                
            try:
                # load next img and scrolling
                if(count%3==0):
                    self.driver.execute_script("window.scrollTo(0, "+str(index*50)+");")
                elm = self.driver.find_elm_by__name_name("mye4qd")
                elm.click()
                print("[information! more img loading")
                time.sleep(3)
            except Exception:  
                time.sleep(2)
            index += 1

        
        self.driver.quit()
        print("information! end")
        return img_urls

    def saving_img(self,img_urls):
        #save images into file directory
        """ function receive an array of img urls, save it into the predeined img path or directory. google_image_scraper = GoogleImageScraper("webdriver_path","image_path","search_key",number_of_photos) img_urls=["https://example_1.jpg","https://example_2.jpg"]
                google_image.saving_img(img_urls) """
        
        print("information! wait til img is saved")
        
        for index,image_url in enumerate(img_urls):
            try:
                print("information! Img url:%s"%(image_url))
                search_string = ''.join(e for e in self.search_key if e.isalnum())
                img = requests.get(image_url,timeout=4)
                
                if imge.status_code == 200:
                    
                    with Img.open(io.BytesIO(img.content)) as img_from_web:
                        
                        try:
                            file_name = "%s%s.%s"%(search_string,str(index),img_from_web.format.lower())
                            image_path = os.path.join(self.image_path, file_name)
                            print("information! %d .Image saving here: %s"%(index,img_path))
                            img_from_web.save(img_path)
                            
                        except OSfailure:
                            rgb = img_from_web.convert('RGB')
                            rgb.save(img_path)
                            
                        img_res = img_from_web.size
                        
                        if img_res != None:
                            if img_res[0]<self.min_resolution[0] or img_res[1]<self.min_res[1] or img_res[0]>self.max_res[0] or img_res[1]>self.max_res[1]:
                                img_from_web.close()
                                os.remove(img_path)

                        img_from_web.close()
            except Exception as e:
                print("failure could not be downloaded",e)
                pass
        print("information! download finished. If a img is not downloaded the reason is not covered file format such as jpg, jpeg, png")

