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
    post_df['selftext'] = post_df['selftext'].astype(str)
    post_df['title'] = post_df['title'].astype(str)
    post_df['score'] = post_df['score'].astype(int)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['author'] = post_df['author'].astype(str)
    post_df['created_utc'] = post_df['created_utc'].fillna(0)  # Example: Fill with 0
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['url'] = post_df['url'].astype(str)
    post_df['subreddit_subscribers'] = post_df['subreddit_subscribers'].astype(int)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    over_18_mode = post_df['over_18'].mode()
    post_df['over_18'] = np.where(post_df['over_18'].isin([True, False]),
                                post_df['over_18'], over_18_mode).astype(bool)
    spoiler_mode = post_df['spoiler'].mode()
    post_df['spoiler'] = np.where(post_df['spoiler'].isin([True, False]),
                                post_df['spoiler'], spoiler_mode).astype(bool)
    stickied_mode = post_df['stickied'].mode()
    post_df['stickied'] = np.where(post_df['stickied'].isin([True, False]),
                                    post_df['stickied'], stickied_mode).astype(bool)

    return post_df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index= False)


