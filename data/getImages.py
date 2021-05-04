"""
Download hero and item images to be used in the UI
"""
import requests
import pandas as pd
import os

heroes_df = pd.read_csv('output/heroesData.csv')
items_df = pd.read_csv('output/itemsData.csv')

# heroes - download small size images
for i in heroes_df.img_sb:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_sb.png')[0] + '.png'
    with open(os.path.join('assets', 'heroes', 'sb', hero_name), 'wb') as f:
        f.write(r.content)

# heroes - download full size images
for i in heroes_df.img_full:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_full.png')[0] + '.png'
    with open(os.path.join('assets', 'heroes', 'full', hero_name), 'wb') as f:
        f.write(r.content)

# heroes - download vertical images
for i in heroes_df.img_vert:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_vert.jpg')[0] + '.jpg'
    with open(os.path.join('assets', 'heroes', 'vert', hero_name), 'wb') as f:
        f.write(r.content)

# items - download images
for i in items_df.img:
    r = requests.get(i)
    item_name = i.split('/images/items/')[1]
    with open(os.path.join('assets', 'items', item_name), 'wb') as f:
        f.write(r.content)
