from utils.constants import CLIENT_ID, SECRET, USER_AGENT, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, transform_data, extract_posts, data_to_csv
import pandas as pd

def reddit_pipeline(file_name:str, subreddit:str, time_filter='day', limit=None):
    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)
    #extraction
    post = extract_posts(instance, subreddit, time_filter, limit)
    #transformation
    df_post = pd.DataFrame(post)
    df_transformed = transform_data(df_post)
    #load
    data_to_csv(df_transformed, )
