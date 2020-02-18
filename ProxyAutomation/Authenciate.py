import os
import time as T
import logging
import schedule 
from decouple import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


log_filename = lambda filename: filename if filename else "message.log"

def SetUpLogger(filename):
    LOG_FILENAME = log_filename(filename)
    logging.basicConfig(filename=LOG_FILENAME,          
                        level=logging.INFO,
                        format="%(asctime)s - Authenciation - %(levelname)s - %(message)s"
                        )

def SetUpDriver(path):
    try:
        option =Options()
        option.add_argument("--headless")
        wd = webdriver.Chrome(executable_path=path,options=option)
        return wd
    except:
        logging.error("Path not correcet")
        exit(0)
    

def Authenciate(wd,username,password):
    try:
        url = f"http://{username}:{password}@proxy1.iitj.ac.in/B0001D0000N0000N0000F0000S0000R0004/10.24.1.97/http://math.com/"
        url2= f"http://{username}:{password}@proxy2.iitj.ac.in/B0001D0000N0000N0000F0000S0000R0004/10.24.1.97/http://math.com/"
        wd.get(url)
        if "Math" in wd.title:
            logging.info("SUCESS")
        else:
            logging.error("FAIL")
        wd.close()
    except:
        log_filename.error("Authenciation fail..")

def job():
    USERNAME = config('username',default="")
    PASSWORD = config('password', default="")
    LOG_FILENAME = config('LOG_FILENAME',default="")
    PATH=config('DRIVER_PATH',default="")
    SetUpLogger(LOG_FILENAME)
    wd = SetUpDriver(PATH)
    Authenciate(wd,USERNAME,PASSWORD)

if __name__=="__main__":
    while True:
        time = 60*5  # 5 min
        job()
        T.sleep(time)