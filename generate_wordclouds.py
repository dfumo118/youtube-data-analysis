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

    label = channels.iloc[0]['name']
    generate_cloud(df['title'].to_list(), stopwords, label)

def overall_cloud():
    channels = pd.read_csv("data/channel_info.csv")
    names = (' '.join(channels['name'].to_list())).split(' ')

    stopwords = set(STOPWORDS)
    stopwords.update(names)

    df = pd.read_csv("data/video_info.csv")
    generate_cloud(df['title'].to_list(), stopwords, "Overall")

def generate_cloud(titles, stopwords, label):
    words = ' '.join(titles)

    wordcloud = WordCloud(stopwords= stopwords, background_color= "white").generate(words)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(label, fontdict={'fontsize': 30}, pad= 20)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    overall_cloud()