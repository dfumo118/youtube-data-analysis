from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from dotenv import dotenv_values
import emoji

def get_videos_info(youtube, videoIds):
    for i in range(4):
        query = ""
        for j in range(i*50, (i+1)*50):
            if j >= len(videoIds):
                break
            query = query + videoIds[j] + ","

        response = youtube.videos().list(part='statistics, snippet', id=query[:-1]).execute()

        result = []
        for item in response['items']:
            result.append({
                'channelId': item['snippet']['channelId'],
                'id': item['id'],
                'title': item['snippet']['title'],
                'date': item['snippet']['publishedAt'],
                'views': item['statistics']['viewCount'],
                'likes': item['statistics'].get('likeCount',0),
                'comments': item['statistics'].get('commentCount',0)
            })

    return pd.DataFrame(result)



def get_channel_videos(youtube, channelId):
    videos = []
    uploadId = youtube.channels().list(part='contentDetails', id=channelId).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    pageToken = ""

    for i in range(4):
        response = youtube.playlistItems().list(part='snippet', playlistId= uploadId, maxResults= 50).execute()
        if i > 0:
            response = youtube.playlistItems().list(part='snippet', playlistId= uploadId, maxResults= 50, pageToken= pageToken).execute()
        
        for item in response['items']:
            videos.append(item['snippet']['resourceId']['videoId'])
        
        try:
            pageToken = response['nextPageToken']
        except:
            break

    return videos

def remove_emoji(string):
    return emoji.replace_emoji(string, replace="")

def clean_video_info(df):
    df['title'] = df['title'].apply(remove_emoji)
    df['views'] = pd.to_numeric(df['views'])
    df['likes'] = pd.to_numeric(df['likes'])
    df['comments'] = pd.to_numeric(df['comments'])
    df['date'] = pd.to_datetime(df['date']).dt.date.astype('datetime64')


def get_video_data():
    config = dotenv_values(".env")
    apiKey = config['API_KEY']
    channelIds = [
        "UC-lHJZR3Gqxm24_Vd_AJ5Yw", # PewDiePie
        "UCX6OQ3DkcsbYNE6H8uQQuVA", # MrBeast
        "UCRijo3ddMTht_IHyNSNXpNQ", # Dude Perfect
        "UC7_YxT-KID8kRbqZo7MyscQ", # Markiplier
        "UCpB959t8iPrxQWj7G6n0ctQ", # SSSniperWolf
        "UCTkXRDQl0luXxVQrRQvWS6w", # Dream
        "UCYzPXprvl5Y-Sf0g4vX-m6g", # jacksepticeye
        "UCKqH_9mk1waLgBiL2vT5b9g", # VanossGaming
        "UCwD4x63A9KC7Si2RuSfg-SA", # Dobre Twins
        "UClQubH2NeMmGLTLgNdLBwXg" # ZHC
    ]

    youtube = build('youtube', 'v3', developerKey = apiKey)
    
    df = pd.DataFrame([], columns=['id', 'title', 'views', 'likes', 'comments', 'channelId', 'date'])
    for id in channelIds:
        df = pd.concat([df,get_videos_info(youtube, get_channel_videos(youtube, id))], ignore_index=True)

    clean_video_info(df)
    
    df.to_csv("data/video_info.csv")

def get_channel_info(youtube, channelId):
    response = youtube.channels().list(part='snippet, statistics', id= channelId).execute()
    return pd.DataFrame([{
        'id': response['items'][0]['id'],
        'name': response['items'][0]['snippet']['title'],
        'totalViews': response['items'][0]['statistics']['viewCount'],
        'totalSubscribers': response['items'][0]['statistics']['subscriberCount'],
        'totalVideos': response['items'][0]['statistics']['videoCount'],
    }])

def clean_channel_info(df):
    df['totalViews'] = pd.to_numeric(df['totalViews'])
    df['totalSubscribers'] = pd.to_numeric(df['totalSubscribers'])
    df['totalVideos'] = pd.to_numeric(df['totalVideos'])

def get_channel_data():
    config = dotenv_values(".env")
    apiKey = config['API_KEY']
    channelIds = [
        "UC-lHJZR3Gqxm24_Vd_AJ5Yw", # PewDiePie
        "UCX6OQ3DkcsbYNE6H8uQQuVA", # MrBeast
        "UCRijo3ddMTht_IHyNSNXpNQ", # Dude Perfect
        "UC7_YxT-KID8kRbqZo7MyscQ", # Markiplier
        "UCpB959t8iPrxQWj7G6n0ctQ", # SSSniperWolf
        "UCTkXRDQl0luXxVQrRQvWS6w", # Dream
        "UCYzPXprvl5Y-Sf0g4vX-m6g", # jacksepticeye
        "UCKqH_9mk1waLgBiL2vT5b9g", # VanossGaming
        "UCwD4x63A9KC7Si2RuSfg-SA", # Dobre Twins
        "UClQubH2NeMmGLTLgNdLBwXg" # ZHC
    ]

    youtube = build('youtube', 'v3', developerKey = apiKey)
    df = pd.DataFrame([], columns=['id', 'name', 'totalViews', 'totalSubscribers', 'totalVideos'])
    for id in channelIds:
        df = pd.concat([df,get_channel_info(youtube, id)], ignore_index=True)
    clean_channel_info(df)
    
    df.to_csv("data/channel_info.csv")

if __name__ == "__main__":
    get_channel_data()
