from time import sleep
import json
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#global variables
#load artist names
artists = []
with open("ArtistList.txt", "r") as file:
    artists = file.readlines()
    artists = [artist.strip() for artist in artists]


artistDict = {}
with open("ArtistStatus.json", "r") as file:
    try:
       artistDict = json.load(file)
    except:
        pass

   
#load the dataset dictionary
dataset = {}
with open("SongInfo.json", "r") as file:
    try:
       dataset = json.load(file)
    except:
        print("Running for the first time.")



#helper functions 
def add_music_entry(dataset, music_id, title, artist, album_name, duration, view_count): 
    if music_id in dataset:
        print(f"Music ID '{music_id}' already exists. Entry not added.")
    else:
        # Add new entry to the dataset
        dataset[music_id] = {
            "Title": title,
            "Artist": artist,
            "Album Name": album_name,
            "View Count": view_count,
            "Duration": duration,
            "url": f"https://youtube.com/watch?v={music_id}"
        }

        #save the updated dataset
        with open('SongInfo.json', 'w', encoding='utf-8') as fp:
            json.dump(dataset, fp, ensure_ascii=False, indent=4)


        print(f"Music entry '{music_id}' added successfully.")



#XPATHs
SearchBar = "//input[contains(@id,'input')]"
ArtisitCard = "//div[contains(@class,'card-container style-scope ytmusic-card-shelf-renderer')]"
GoToArtist = "(//div[contains(@class,'card-container style-scope ytmusic-card-shelf-renderer')]//button[contains(@class,'yt-spec-button-shape-next')])[3]"
ArtistCheck = "//ytmusic-shelf-renderer[contains(@class,'ytmusic-section-list-renderer')]//h2//a[contains(@class,'yt-formatted-string')]"
# GoToSongs = "//ytmusic-shelf-renderer[contains(@class,'ytmusic-section-list-renderer')]//button[contains(@class, 'yt-spec-button-shape-next')]//span[contains(text(),'Show all')]"
GoToSongs = "(//ytmusic-shelf-renderer[contains(@class,'ytmusic-section-list-renderer')]//button[contains(@class, 'yt-spec-button-shape-next')]//span[contains(text(),'Show all')]/../../..//div[contains(@class,'yt-spec-touch-feedback-shape__fill')])[1]"
SongsCheck = "//div[contains(@id,'header')]//h2//*[contains(text(),'Songs')]"
PrimaryCol = "(//div[contains(@class,'style-scope ytmusic-playlist-shelf-renderer') and contains(@id,'contents')]//ytmusic-responsive-list-item-renderer//div[contains(@class,'title')]"
SecondaryCol = "(//div[contains(@class,'style-scope ytmusic-playlist-shelf-renderer') and contains(@id,'contents')]//ytmusic-responsive-list-item-renderer//div[contains(@class,'secondary-flex-columns')]"
SongTitle = "//a)"
ArtistName = "//yt-formatted-string[1])"
ViewCount = "//yt-formatted-string[2])"
AlbumName = "//yt-formatted-string[3])"
Duration = "(//yt-formatted-string[contains(@class,'fixed-column MUSIC_RESPONSIVE_LIST_ITEM_COLUMN_DISPLAY_PRIORITY_HIGH style-scope ytmusic-responsive-list-item-renderer style-scope ytmusic-responsive-list-item-renderer')])"

# FirstResult = "(//ytd-video-renderer[contains(@class,'style-scope ytd-item-section-renderer')]//ytd-thumbnail[contains(@size,'large')])"
# CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]"
# CommentN = "//ytd-comment-thread-renderer[contains(@class,'style-scope ytd-item-section-renderer')]//span[contains(@class,'yt-core-attributed-string--white-space-pre-wrap' )]"


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
waitTime = 5




#main code 
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, waitTime)
print("Driver started")

#open website 
driver.get('https://music.youtube.com/')
# sleep(200)

for artist in artists:
    if artist in dataset:
        print(f"Skipping {artist}")
        continue

    if artist in artistDict:
            continue
   
    print(f"Searching for {artist}")
    search = wait.until(EC.presence_of_element_located((By.XPATH, SearchBar)))
    search.clear()
    search.send_keys(artist)
    search.send_keys(Keys.RETURN)
    
    try:
        arrtistCard = wait.until(EC.presence_of_element_located((By.XPATH, ArtisitCard)))
    except:
        print(f"Artist not found for {artist}")
        artistDict[artist] = None
        continue

    #if the artist card is present goto the artist page
    try:
        goToArtist = wait.until(EC.element_to_be_clickable((By.XPATH, GoToArtist)))
    except:
        print(f"No artist page for {artist}")
        artistDict[artist] = None
        continue
    goToArtist.click()

    #check for songs section
    try:
        artistCheck = wait.until(EC.element_to_be_clickable((By.XPATH, ArtistCheck)))
    except:
        print(f"Songs not found on Artist page for {artist}")
        artistDict[artist] = None
        continue

    # #go to songs section 
    # goToSongs = wait.until(EC.element_to_be_clickable((By.XPATH, GoToSongs)))
    # goToSongs.click()
    artistCheck.click()


    #check for songs section
    try:
        songsCheck = wait.until(EC.presence_of_element_located((By.XPATH, SongsCheck)))
    except:
        print(f"Songs not found in default location for {artist}")
        artistDict[artist] = None
        continue

    #traverse over the songs and fetch stats

    SongsCount = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, PrimaryCol+")"))))
    

    for i in range(SongsCount):
        try:
            title = wait.until(EC.presence_of_element_located((By.XPATH, PrimaryCol + SongTitle + "[" + str(i+1) + "]"))).text
            artistName = wait.until(EC.presence_of_element_located((By.XPATH, SecondaryCol + ArtistName + "[" + str(i+1) + "]"))).text
            album_name = wait.until(EC.presence_of_element_located((By.XPATH, SecondaryCol + AlbumName + "[" + str(i+1) + "]"))).text
            view_count = wait.until(EC.presence_of_element_located((By.XPATH, SecondaryCol + ViewCount + "[" + str(i+1) + "]"))).text
            duration = wait.until(EC.presence_of_element_located((By.XPATH, Duration + "[" + str(i+1) + "]"))).text
            url = wait.until(EC.presence_of_element_located((By.XPATH, PrimaryCol + SongTitle + "[" + str(i+1) + "]"))).get_attribute("href")
            music_id = url.split("&")[0].split("=")[1]
            # print(music_id+":"+title + "|"+artistName+ "|"+ album_name, duration, view_count)
        except:
            print(f"Error in fetching song {title}")
            continue

        add_music_entry(dataset, music_id, title, artistName, album_name, duration, view_count)

    artistDict[artist] = True
    with open('ArtistStatus.json', 'w', encoding='utf-8') as fp:
        json.dump(artistDict, fp, ensure_ascii=False, indent=4)

    print(f"Done with {artist}")



        
 

    

        
print("Work done.\nQuiting driver")
driver.quit()
