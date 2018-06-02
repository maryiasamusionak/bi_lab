import csv
import numpy as np
import pandas as pd

data = pd.read_csv('IMDB-Movie-Data.csv')
year_rating = data.groupby('Year')
csv.writer(open('Rating.csv', 'w'))\
    .writerow([year_rating['Year'], year_rating['Rating'].agg(np.mean)])

data_top = data.nlargest(250, 'Rating')
data_top.to_csv('Top.csv', columns=['Title', 'Rating'])
