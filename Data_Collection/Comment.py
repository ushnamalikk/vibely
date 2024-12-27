from time import sleep
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#global variables
# load songs name from the txt file
Songs = {}
with open("SongInfo.json", "r") as file:
    Songs = json.load(file)



#load the song dictionary
songDict = {}
with open("SongCollection.json", "r") as file:
    try:
       songDict = json.load(file)
    except:
        print("Running for the first time.")
   

#XPATHs
CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]//span[contains(@class,'yt-core-attributed-string--white-space-pre-wrap')]"


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




#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
actions = ActionChains(driver)


print("Driver started")
# Run on the last half of the songs
print(f"Total songs: {len(Songs)}")
print("Running on the last half of the songs: " + str(len(Songs)//2))

# Convert the dictionary to a list of keys
song_keys = list(Songs.keys())
# song_keys = song_keys[len(Songs)//2:]

for song in song_keys:
    if song in songDict:
        print(f"Skipping {song}")
        continue
    
    print(f"Searching for {song}")

    songUrl = Songs[song]["url"]
    print(f"Opening {songUrl}")

    driver.get(songUrl)

    # scroll down until the comments are loaded
    for _ in range(5):
        actions.send_keys(Keys.PAGE_DOWN).perform()
        sleep(0.5)


    #get first count comments
    count = 100
    comments = []

    for i in range(count):
        try:
            comment = wait.until(EC.presence_of_all_elements_located((By.XPATH, "("+CommentN+")["+str(i+1)+"]")))
            comments.append(comment[0].text)
            
            if i % 4 == 0:
               actions.send_keys(Keys.PAGE_DOWN).perform()

               element = wait.until(EC.presence_of_element_located((By.XPATH, "("+CommentN+")["+str(i+1)+"]")))
               actions.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
            
        except:
            break
            

    #save the comments in the dictionary 
    songDict[song] = comments
    with open('SongCollection.json', 'w', encoding='utf-8') as fp:
            json.dump(songDict, fp, ensure_ascii=False, indent=4)

 

    
print("Work done.\nQuiting driver")
driver.quit()
