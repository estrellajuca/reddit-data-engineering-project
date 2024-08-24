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
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)

    return post_lists

def transform_data(post_df: pd.DataFrame):
    post_df['id'] = post_df['id'].astype(str)
    post_df['title'] = post_df['title'].astype(str)
    post_df['score'] = post_df['score'].astype(int)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['author'] = post_df['author'].astype(str)
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], units='s')
    post_df['url'] = post_df['url'].astype(str)
    post_df['over_18'] = post_df['over_18'].astype(bool)
    post_df['edited'] = post_df['edited'].astype(str)
    post_df['spoiler'] = post_df['spoiler'].astype(str)
    post_df['stickied'] = post_df['stickied'].astype(str)
    post_df['subreddit_subscribers'] = post_df['subreddit_subscribers'].astype(int)

    return post_df

def data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index= False)


