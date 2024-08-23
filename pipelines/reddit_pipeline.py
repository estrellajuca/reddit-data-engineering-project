from utils.constants import CLIENT_ID, SECRET, USER_AGENT
from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)
    #extraction
    post = extract_posts(instance, subreddit, time_filter, limit)