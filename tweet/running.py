import pandas as pd
import numpy as np
import openpyxl
import csv

def savecosines():
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 300)

    df = pd.read_csv('tweet/winemag-data-130k-v2.csv', usecols=[
        'id',
        'country',
        'points',
        'taster_name',
        'title'
    ],encoding='latin1')
    # winemag-data-130k-v2.csv

    title_user = df.pivot_table('points', index='taster_name', columns='title')

    # 평점을 부여안한 영화는 그냥 0이라고 부여

    title_user = title_user.fillna(0)

    from sklearn.metrics.pairwise import cosine_similarity

    # 유저 1~610 번과 유저 1~610 번 간의 코사인 유사도를 구함
    user_based_collab = cosine_similarity(title_user, title_user)

    user_based_collab = pd.DataFrame(user_based_collab, index=title_user.index, columns=title_user.index)

    user_index_list = user_based_collab['add name'].sort_values(ascending=False)[:10].index.tolist()

    return user_index_list[1]

def Editexcel(new_data):

    # df = pd.read_csv('tweet/winemag-data-130k-v2.csv', usecols = ['description','points','taster_name','title'], encoding='latin_1')
    # print(df)

    # df = df.append(new_data, ignore_index=True)
    # print(df)
    # df.to_csv('tweet/winemag-data-130k-v2.csv')

    with open("tweet/winemag-data-130k-v2.csv", 'a', newline='') as file:
        fieldnames = ['id','country','description','designation','points','price','province','region_1','region_2','taster_name','taster_twitter_handle','title','variety','winery']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_data)




