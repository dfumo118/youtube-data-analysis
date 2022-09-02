import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def most_views_in_set():
    videos_df = pd.read_csv("data/video_info.csv", index_col= 0)
    channels_df = pd.read_csv("data/channel_info.csv", index_col= 0)

    totals_df = videos_df.groupby(videos_df['channelId'], as_index= False).sum()
    totals_df = totals_df.sort_values('views')

    ids = [id for id in totals_df['channelId']]
    labels = [channels_df.loc[channels_df['id'] == id, 'name'].values[0] for id in ids]
    views = [totals_df.loc[totals_df['channelId'] == id, 'views'].values[0] for id in ids]
    
    fig = plt.figure(figsize =(12, 7))
    plt.barh(labels, views)
    plt.show()

def divide_by_views_in_set(totals_row, channels_df, n):
    videos = channels_df.loc[channels_df['id'] == totals_row['channelId'], 'totalVideos'].values[0]
    totals_row['views'] = float(totals_row['views']) / float(videos)
    return totals_row
    

def most_views_per_video_in_set():
    videos_df = pd.read_csv("data/video_info.csv", index_col= 0)
    channels_df = pd.read_csv("data/channel_info.csv", index_col= 0)

    totals_df = videos_df.groupby(videos_df['channelId'], as_index= False).sum()
    totals_df = totals_df.apply(divide_by_views_in_set, axis= 1, args= (channels_df, 0))
    totals_df = totals_df.sort_values('views')

    ids = [id for id in totals_df['channelId']]
    labels = [channels_df.loc[channels_df['id'] == id, 'name'].values[0] for id in ids]
    views = [totals_df.loc[totals_df['channelId'] == id, 'views'].values[0] for id in ids]
    
    fig = plt.figure(figsize =(12, 7))
    plt.barh(labels, views)
    plt.show()

def most_total_views():
    channels_df = pd.read_csv("data/channel_info.csv", index_col= 0)
    channels_df = channels_df.sort_values('totalViews')

    labels = [name for name in channels_df['name']]
    views = [count for count in channels_df['totalViews']]
    
    fig = plt.figure(figsize =(12, 7))
    plt.barh(labels, views)
    plt.show()

def divide_by_views(row):
    row['totalViews'] = float(row['totalViews']) / float(row['totalVideos'])
    return row

def most_total_views_per_video():
    channels_df = pd.read_csv("data/channel_info.csv", index_col= 0)
    channels_df = channels_df.apply(divide_by_views, axis= 1)
    channels_df = channels_df.sort_values('totalViews')

    labels = [name for name in channels_df['name']]
    views = [count for count in channels_df['totalViews']]
    
    fig = plt.figure(figsize =(12, 7))
    plt.barh(labels, views)
    plt.show()

if __name__ == "__main__":
    most_total_views_per_video()

