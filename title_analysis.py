from itertools import count
import pandas as pd
import numpy as np
import string
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def get_words():
    stop = set(stopwords.words('english'))
    videos_df = pd.read_csv("data/video_info.csv", index_col= 0)
    channels_df = pd.read_csv("data/channel_info.csv", index_col= 0)
    names = [name for name in channels_df['name']]
    split_names = (' '.join(names).lower()).split(' ')

    words = ' '.join([title for title in videos_df['title']])
    words = words.translate(str.maketrans('', '', string.punctuation)).lower()
    words = re.sub(r'[0-9]+', '', words)
    words = words.split(' ')
    words = [word for word in words if word not in stop and word != '' and word not in split_names]

    return words

def count_instances(words):
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
            continue
        
        result[word] = 1

    return pd.DataFrame(list(result.items()), columns= ['word', 'count'])

def count_total_views_of_word(word):
    videos_df = pd.read_csv("data/video_info.csv", index_col= 0)
    videos_df['title'] = videos_df['title'].str.lower()
    videos_df = videos_df[videos_df['title'].str.contains(f" {word} ")]

    return videos_df['views'].sum()

def count_total_views(words):
    result = {word:count_total_views_of_word(word) for word in words}
    return pd.DataFrame(list(result.items()), columns= ['word', 'views'])
    