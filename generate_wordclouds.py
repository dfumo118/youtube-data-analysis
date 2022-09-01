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
    filename = '_'.join(label.split(' '))
    generate_cloud(df['title'].to_list(), stopwords, label, filename)

def overall_cloud():
    channels = pd.read_csv("data/channel_info.csv")
    names = (' '.join(channels['name'].to_list())).split(' ')

    stopwords = set(STOPWORDS)
    stopwords.update(names)

    df = pd.read_csv("data/video_info.csv")
    generate_cloud(df['title'].to_list(), stopwords, "Overall", "overall")

def generate_cloud(titles, stopwords, label, filename):
    words = ' '.join(titles)

    wordcloud = WordCloud(stopwords= stopwords, background_color= "white").generate(words)
    wordcloud.to_file("img/" + filename + ".png")
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(label, fontdict={'fontsize': 30}, pad= 20)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
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
    for id in channelIds:
        cloud_by_channel(id)