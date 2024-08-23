import sys

import numpy as np
import pandas as pd
import praw
from praw import Reddit

from utils.constants import POST_FIELDS

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("connected to reddit!")
        return reddit
    except Exception as ex:
        print(ex)
        sys.exit(1)

def extract_posts(reddit_instance: Reddit, subreddit:str, time_filter:str, limit:None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter = time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        print(f'POST111: {post_dict}')
        post = {key: post_dict[key] for key in POST_FIELDS}

