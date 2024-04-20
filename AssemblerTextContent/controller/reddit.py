


import json

import requests
from scraper.model.reddit.model import RedditListing


def getSingleReddit():
    url = "https://www.reddit.com/r/AITAH/comments/1c86ne7/aitah_for_cancelling_my_sister_in_laws_engagement/.json"
    # url = "https://www.reddit.com/r/AITAH/.json"
    response = requests.get(url)

    reddit_listings = []
    if response.status_code == 200:
        reddit_data = json.loads(response.text)
        if isinstance(reddit_data, list):
            for reddit_item in reddit_data: 
                reddit_listing = RedditListing(**reddit_item)
                reddit_listings.append(reddit_listing)
        else:
            print('//TODO')
            # for reddit_item in reddit_data: 
            #     reddit_listing = RedditListing(**reddit_item)
            #     reddit_listings.append(reddit_listing)
    else:
        print("error occurred \n ++ Reason:"+response.reason)
    return reddit_listings[0].data.children[0].data.selftext
