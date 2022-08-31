import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def cloud_by_channel(channelId):
    channels = pd.read_csv("data/channel_info.csv")
    channels = channels.loc[channels['id'] == channelId]
    names = (' '.join(channels['name'].to_list())).split(' ')

    stopwords = set(STOPWORDS)
    stopwords.update(names)

    df = pd.read_csv("data/video_info.csv")
    df = df.loc[df['channelId'] == channelId]
    generate_cloud(df['title'].to_list(), stopwords)

def overall_cloud():
    channels = pd.read_csv("data/channel_info.csv")
    names = (' '.join(channels['name'].to_list())).split(' ')

    stopwords = set(STOPWORDS)
    stopwords.update(names)

    df = pd.read_csv("data/video_info.csv")
    generate_cloud(df['title'].to_list(), stopwords)

def generate_cloud(titles, stopwords):
    words = ' '.join(titles)

    wordcloud = WordCloud(stopwords= stopwords, background_color= "white").generate(words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    cloud_by_channel("UCRijo3ddMTht_IHyNSNXpNQ")