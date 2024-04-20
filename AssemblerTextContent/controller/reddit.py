import json
import time
import requests
from scraper.model.reddit.model import RedditData, RedditListing



def getRandom():
    url = "https://www.reddit.com/r/AITAH/.json"
    response = requests.get(url)
    reddit_data = json.loads(response.text)
    print(reddit_data)


def getRedditsByCycle(cycle):
    # url = "https://www.reddit.com/r/AITAH/top/.json?t=year"
    # url = "https://www.reddit.com/r/AITAH/top/.json?t=week"
    # url = "https://www.reddit.com/r/AITAH/top/.json?t=day"
    url = "https://www.reddit.com/r/AITAH/top/.json?t=month"
    time.sleep(2)
    response = requests.get(url)
    reddit_listings = []
    if response.status_code == 200:
        reddit_data = json.loads(response.text)
        redditListing = RedditListing(reddit_data.get('kind'),**reddit_data.get('data'))
        sorted_posts = sorted(redditListing.data.children, key=lambda x: x.data.score, reverse=True)

        for post in sorted_posts[:cycle]:
            print("Title:", post.data.title)
            print("Score:", post.data.score)
            print("Subreddit:", post.data.subreddit)
            print(cycle)
            reddit_listings.append(post.data.selftext)

    else:
        return "Error occurred "+"\n ++ Reason:"+response.reason
    if reddit_listings.index != 0:
        return reddit_listings
    else:
        return "Reddit Listings post not found"
    
        
