import pandas as pd
import numpy as np
import openpyxl
import csv

def savecosines(username):
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 300)

    df = pd.read_csv('datafile/winemag-data-130k-v2.csv', usecols=[
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
    
    user_index_list = user_based_collab[username].sort_values(ascending=False)[:10].index.tolist()
    print(user_index_list)
    return user_index_list[1]

def editexcel(new_data):

    with open("datafile/winemag-data-130k-v2.csv", 'a', newline='', encoding='latin1') as file:
        fieldnames = ['id','country','description','designation','points','price','province','region_1','region_2','taster_name','taster_twitter_handle','title','variety','winery']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_data)

def searchwine(tag):
    redwine = ['Red', 'Früburgunder', 'Shiraz', 'Zinfandel', 'Tinta', 'Cabernet', 'Syrah-Grenache', 'Roditis', 'Merlot', 'Traminer', 'Nero', 'Shiraz-Viognier', 'Syrah', 'Frappato', 'Nebbiolo', 'Petite', 'Duras', 'Cinsault', 'Zweigelt', 'Bordeaux-style', 'Barbera', 'Sagrantino', 'Malbec', 'Garnacha', 'Tannat-Cabernet', 'Nerello', 'Meritage', 'Primitivo', 'Mencía', 'Blaufränkisch', 'G-S-M', 'Pinot', 'Cannonau', 'Tempranillo', 'Graciano', 'Monica' , 'Merlot-Malbec', 'Bonarda', 'Carmenère', 'Monastrell', 'Gamay', 'Sangiovese', 'Montepulciano', 'Tempranillo-Merlot', 'Carignan-Grenache', 'Prugnolo', 'Port', 'Rhône-style', 'Pinotage', 'Touriga', 'Aglianico', 'Dolcetto' ,'Petite', 'Grenache', 'Shiraz-Cabernet', 'Syrah-Viognier', 'Portuguese', 'Corvina', 'Sousão']

    whitewine = ["Riesling",'Verdelho', 'Zierfandler', 'Grillo', 'Chenin', 'Ugni', 'Cortese', 'White', 'Sémillon', 'Furmint', 'Melon', 'Ribolla', 'Vignoles', 'Verdicchio', 'Inzolia', 'Garganega', 'Vilana', 'Antão', 'Viura', 'Friulano', 'Greco', 'Torrontés', 'Vidal', 'Alsace', 'Marsanne', 'Moscato', 'Vernaccia', 'Glera', 'Muscat', 'Silvaner', 'Savagnin', 'Fiano', 'Vermentino', 'Insolia', 'Catarratto', 'Grüner', 'Viognier-Chardonnay', 'Muscadelle', 'Albariño', 'Kerner', 'Carricante', 'Trebbiano', 'Scheurebe', 'Verdejo', 'Colombard', 'Assyrtico', 'Chinuri', 'Sylvaner', 'Fumé', 'Viognier', 'Verdejo-Viura' ,'Weissburgunder', 'Avesso', 'Gewürztraminer', 'Verduzzo', 'Roussanne', 'Xarel-lo', 'Sauvignon', 'Chardonnay']

    rosewine = ['Rosé', 'Roter', 'Rosato']

    spacling = ['Champagne', 'Prosecco', 'Sparkling']

    if tag in redwine:
        return '레드와인'
    elif tag in whitewine:
        return '화이트와인'
    elif tag in rosewine:
        return '로제와인'
    elif tag in spacling:
        return '스파클링와인'
    else : 
        return f'미분류{tag}'




