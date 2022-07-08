# import librarys 
import zipfile
import stat
from sys import pform
import sys
import os
import urllib.request
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def download_lastest_cdriver(present_chrome_version=""):
'''Find the latest chromedriver, download, (un)zip, set permissions to executable.'''
    def get_pform_fname():
        fname = ''
        is_64bits = sys.maxsize > 2**32
    
        if pform == "linux" or pform == "linux2":
            # linux
            fname += 'linux'
            fname += '64' if is_64bits else '32'
        elif pform == "win32":
             # windows...
            fname += 'win32'
        elif pform == "darwin":
            # os x
            fname += 'mac64'
        fname += '.zip'
        return fname
    
    res = False

    try:
        url = 'https://chromedriver.chromium.org/downloads'
        base_driver_url = 'https://chromedriver.storage.googleapis.com/'
        file_name = 'chromedriver_' + get_pform_fname()
        pattern = 'https://.*?path=(\d+\.\d+\.\d+\.\d+)'
    
        # latest cdriver
        stream = urllib.request.urlopen(url)
        cont = stream.read().decode('utf8')
    
        # parse the latest vers.
        every_match = re.findall(pattern, cont)
        
        if every_match:
            if(present_chrome_version!=""):
                print("information! cdriver update")
                every_match = list(set(re.findall(pattern, cont)))
                present_chrome_version = ".".join(present_chrome_version.split(".")[:-1])
                version_match = [i for i in every_match if re.search("^%s"%present_chrome_version,i)]
                version = version_match[0]
            else:
                print("information! installing newest cdriver")
                version = every_match[1]
            driver_url = base_driver_url + version + '/' + file_name
    
            # download file
            print('information - this can take a minute! downloading chromedriver ver: %s: %s'% (version, driver_url))
            application_path = os.path.dirname(os.path.realpath(__file__))
            cdriver_path = os.path.normpath(application_path+"\\webdriver\\chromedriver.exe")
            f_path = os.path.normpath(application_path + '\\webdriver\\' + file_name)
            urllib.request.urlretrieve(driver_url, f_path)
    
            # folder unzip
            with zipfile.ZipFile(f_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.normpath(application_path + '\\webdriver\\'))
    
            st = os.stat(cdriver_path)
            os.chmod(cdriver_path, st.st_mode | stat.S_IEXEC)
            print('information! lastest cdriver downloaded')
            # tidy up
            os.remove(f_path)
            res = True
    except Exception:
        print("[WARN] unable to download cdriver. the system use local vers.")
    
    return res

