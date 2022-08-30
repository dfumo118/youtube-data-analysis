from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from dotenv import dotenv_values

def get_data():
    config = dotenv_values(".env")
    api_key = config['API_KEY']
    print(api_key)


if __name__ == "__main__":
    get_data()
