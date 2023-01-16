from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://career.infosys.com/joblist?countrycode=IN&companyhiringtype=IL"


web = webdriver.Chrome()

web.get(url)
sec = 5 # increase if internet speed is not good !!!!!!!!!!
print(f"Sleep Seconds {sec}")
time.sleep(sec)

jobs = web.find_elements(By.CSS_SELECTOR, "#filterTabbed > div > div.col-md-8 > div")

for job in jobs:
    data = job.find_elements(By.TAG_NAME, "div")
    try:
        title = data[2].text
        skill = data[5].text.replace("Skills:\n", "")
        location = job.find_element(By.CSS_SELECTOR, "#filterTabbed > div > div.col-md-8 > div > div.bgclass > div:nth-child(2)").text.replace("\n", "")
        print(f"Title: {title}, Skill : {skill}, Location: {location}")
    except:
        pass

print("Sleeping section")
time.sleep(1000)