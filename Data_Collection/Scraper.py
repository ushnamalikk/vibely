from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#faceless undetected chrome
print("Starting the driver")
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument(f"--user-data-dir=user_data")
# options.add_argument("--headless")
waitTime = 4

artistList = {}

def save_progress():
     with open("arhamList.json", "w") as file:
            json.dump(artistList, file)
            

#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
actions = ActionChains(driver)

print("Driver started")

driver.get("https://www.spotify.com/")

sleep(8)

ArtistName = "(//div[@class = 'Ih5mmxAJFDIBYVcQQrrN']/div)"
ArtistInfo = "(//div[@class='RP2rRchy4i8TIp1CTmb7'])"

for i in range(1, 1000):
    for j in range(1, i):
        if j%10 == 0:
            actions.send_keys(Keys.PAGE_DOWN).perform()
            sleep(1)

    artist = wait.until(EC.presence_of_element_located((By.XPATH, ArtistName+"["+str(i)+"]")))
    artist.click()

    info = wait.until(EC.presence_of_element_located((By.XPATH, ArtistInfo))).text
    # print(info)
    final_info = info.split("\n")
    if "Verified" in final_info[0]:
        artistList[final_info[1]] = [final_info[0], final_info[2]]
        print(final_info[1], [final_info[0], final_info[2]])
    else:
        artistList[final_info[0]] = final_info[1:]
        print(final_info[0], final_info[1:])

    # go to previous page
    driver.back() 
    if i%10 == 0:
        save_progress()

    
    
        


print("Work done.\nQuiting driver")
sleep(60)
driver.quit()
