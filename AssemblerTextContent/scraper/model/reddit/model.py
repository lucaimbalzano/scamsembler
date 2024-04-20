import json


class RedditListing:
    def __init__(self, kind, **data):
        self.kind = kind
        self.data = RedditData(**data)

class RedditData:
    def __init__(self, **kwargs):
        self.after = kwargs.get('after')
        self.dist = kwargs.get('dist')
        self.modhash = kwargs.get('modhash')
        self.geo_filter = kwargs.get('geo_filter')
        self.children = [RedditChild(**child) for child in kwargs.get('children')]

class RedditChild:
    def __init__(self, kind, data):
        self.kind = kind
        self.data = RedditPost(**data)

class RedditPost:
    def __init__(self, **kwargs):
        self.approved_at_utc = kwargs.get('approved_at_utc')
        self.subreddit = kwargs.get('subreddit')
        self.selftext = kwargs.get('selftext')
        self.author_fullname = kwargs.get('author_fullname')
        self.title = kwargs.get('title')
        self.ups = kwargs.get('ups')
        self.score = kwargs.get('score')
        self.created = kwargs.get('created')
        self.url = kwargs.get('url')
        self.subreddit_subscribers = kwargs.get('subreddit_subscribers')
        self.num_crossposts = kwargs.get('num_crossposts')


def print_object(reddit_listings):
    for reddit_listing in reddit_listings:
        print("Reddit Listing:")
        print("Kind:", reddit_listing.kind)
        print("Data:")
        print("  After:", reddit_listing.data.after)
        print("  Dist:", reddit_listing.data.dist)
        print("  Modhash:", reddit_listing.data.modhash)
        print("  Geo Filter:", reddit_listing.data.geo_filter)
        print("  Children:")
        for child in reddit_listing.data.children:
            print("    Kind:", child.kind)
            print("    Data:")
            print("      Approved At UTC:", child.data.approved_at_utc)
            print("      Subreddit:", child.data.subreddit)
            print("      Selftext:", child.data.selftext)
            print("      Author Fullname:", child.data.author_fullname)

# Assuming `json_data` contains the JSON data you provided
json_data = '''
{
  "kind": "Listing",
  "data": {
    "after": "t3_1c85vr2",
    "dist": 26,
    "modhash": "",
    "geo_filter": null,
    "children": [
      {
        "kind": "t3",
        "data": {
          "approved_at_utc": null,
          "subreddit": "AITAH",
          "selftext": "A place for members of r/AITAH to chat with each other",
          "author_fullname": "t2_5i11el5c",
          "saved": false,
          "mod_reason_title": null,
          "gilded": 0,
          "clicked": false,
          "title": "r/AITAH Lounge",
          "link_flair_richtext": [],
          "subreddit_name_prefixed": "r/AITAH",
          "hidden": false,
          "pwls": 6,
          "link_flair_css_class": null,
          "downs": 0,
          "thumbnail_height": null,
          "top_awarded_type": null,
          "hide_score": false,
          "name": "t3_m6n71o",
          "quarantine": false,
          "link_flair_text_color": "dark",
          "upvote_ratio": 0.98,
          "author_flair_background_color": null,
          "subreddit_type": "public",
          "ups": 700,
          "total_awards_received": 0,
          "media_embed": {},
          "thumbnail_width": null,
          "author_flair_template_id": null,
          "is_original_content": false,
          "user_reports": [],
          "secure_media": null,
          "is_reddit_media_domain": false,
          "is_meta": false,
          "category": null,
          "secure_media_embed": {},
          "link_flair_text": null,
          "can_mod_post": false,
          "score": 700,
          "approved_by": null,
          "is_created_from_ads_ui": false,
          "author_premium": false,
          "thumbnail": "self",
          "edited": false,
          "author_flair_css_class": null,
          "author_flair_richtext": [],
          "gildings": {},
          "content_categories": null,
          "is_self": true,
          "mod_note": null,
          "created": 1615939521,
          "link_flair_type": "text",
          "wls": 6,
          "removed_by_category": null,
          "banned_by": null,
          "author_flair_type": "text",
          "domain": "self.AITAH",
          "allow_live_comments": true,
          "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;A place for members of &lt;a href=\"/r/AITAH\"&gt;r/AITAH&lt;/a&gt; to chat with each other&lt;/p&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;",
          "likes": null,
          "suggested_sort": "new",
          "banned_at_utc": null,
          "view_count": null,
          "archived": false,
          "no_follow": false,
          "is_crosspostable": false,
          "pinned": false,
          "over_18": false,
          "all_awardings": [],
          "awarders": [],
          "media_only": false,
          "can_gild": false,
          "spoiler": false,
          "locked": false,
          "author_flair_text": null,
          "treatment_tags": [],
          "visited": false,
          "removed_by": null,
          "num_reports": null,
          "distinguished": null,
          "subreddit_id": "t5_446kys",
          "author_is_blocked": false,
          "mod_reason_by": null,
          "removal_reason": null,
          "link_flair_background_color": "",
          "id": "m6n71o",
          "is_robot_indexable": true,
          "report_reasons": null,
          "author": "DepressedTrashKitty",
          "discussion_type": "CHAT",
          "num_comments": 2273,
          "send_replies": true,
          "whitelist_status": "all_ads",
          "contest_mode": false,
          "mod_reports": [],
          "author_patreon_flair": false,
          "author_flair_text_color": null,
          "permalink": "/r/AITAH/comments/m6n71o/raitah_lounge/",
          "parent_whitelist_status": "all_ads",
          "stickied": true,
          "url": "https://www.reddit.com/r/AITAH/comments/m6n71o/raitah_lounge/",
          "subreddit_subscribers": 1491863,
          "created_utc": 1615939521,
          "num_crossposts": 2,
          "media": null,
          "is_video": false
        }
      }
    ]
  }
}
'''



