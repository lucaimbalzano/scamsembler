from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from scraper.model.reddit.model import RedditListing, print_object
from scraper.core import Scraper
from scraper.settings import settings
from scraper.settings.browser import Browser
import requests
import json


app = FastAPI()


app.add_middleware(CORSMiddleware,
                   allow_methods=["*"],
                   allow_credentials=True,
                   allow_origins=["http://localhost:5173/"])

# url = settings.BASE_LINK_REDDIT_AITAH
# scraper_browser = Scraper(Browser.get_browser()).browser
# xpath = "/html/body/shreddit-app/dsa-transparency-modal-provider/div/div[1]/div/main/shreddit-post/div[2]/div"
# scraper_browser.get(url)
# firstQuestion = scraper_browser.find_element("xpath",xpath).text
# print(firstQuestion)
# scraper_browser.close()

# url = "https://www.reddit.com/r/AITAH/comments/1c86ne7/aitah_for_cancelling_my_sister_in_laws_engagement/.json"
url = "https://www.reddit.com/r/AITAH/.json"
response = requests.get(url)
reddit_listings = []
if response.status_code == 200:
    list_reddit_data = json.loads(response.text)
    for reddit_item in list_reddit_data: 
        reddit_listing = RedditListing(**reddit_item)
        reddit_listings.append(reddit_listing)
else:
    print("error occurred ["+str(response.status_code)+"] \n ++ Reason:"+response.reason)
print_object(reddit_listings)


@app.get('/')
def run_check():
    return JSONResponse(content={"status": "Running!"})