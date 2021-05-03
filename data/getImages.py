"""
Download hero images to be used in the UI
"""
import requests
import pandas as pd
import os

heroes_df = pd.read_csv('output/heroesData.csv')

# download small size images
for i in heroes_df.img_sb:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_sb.png')[0] + '.png'
    with open(os.path.join('assets', 'sb', hero_name), 'wb') as f:
        f.write(r.content)

# download full size images
for i in heroes_df.img_full:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_full.png')[0] + '.png'
    with open(os.path.join('assets', 'full', hero_name), 'wb') as f:
        f.write(r.content)

# download vertical images
for i in heroes_df.img_vert:
    r = requests.get(i)
    hero_name = i.split('/images/heroes/')[1].split('_vert.jpg')[0] + '.jpg'
    with open(os.path.join('assets', 'vert', hero_name), 'wb') as f:
        f.write(r.content)
