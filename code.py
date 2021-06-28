!pip install kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d tmbd/tmbd-movie-metadata

!ls

!unzip tmbd-movie-metadata.zip

!ls

import pandas as pd
import numpy as np

df1 = pd.read_csv('users_interactions.csv')
df2 = pd.read_csv('shared_articles.csv')

df1.head()
df2.head()

df1.columns = ['timestamp', 'eventType', 'contentId', 'authorPersonId', 'contentType', 'title', 'lang', 'url']
df2 = df2.merge(df1, on='id')

df2.head(5)

q_movies = df2.copy().loc[df2['vote_count'] >= m]
print(q_movies.shape)

def weighted_rating(x, m=m, C=C):
  v = x['userCountry']
  R = x['userRegion']
  return(v/(v+m)*R) + (v/(v+m)*C)

q_timestamp['score'] = q_timestamp.apply(weighted_rating, axis = 1)

import plotly.express as px

fig = px.bar((q_timestamp.head(10).sort_values('score', ascending=True)), x="score", y="title", orientation='h')
fig.show()
