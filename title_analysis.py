import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def get_words():
    stop = set(stopwords.words('english'))
    videos_df = pd.read_csv("data/video_info.csv", index_col= 0)
    words = ' '.join([title for title in videos_df['title']])
    words = words.translate(str.maketrans('', '', string.punctuation)).lower()
    words = words.split(' ')
    words = [word for word in words if word not in stop and word != '']
    return words

def count_instances(words):
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
            continue
        
        result[word] = 1

    return pd.DataFrame(list(result.items()), columns= ['word', 'count'])