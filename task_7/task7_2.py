import argparse
import os.path
import pandas as pd

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--year', help='Shows top 250 films and their years',
                        action='store_true')
arg_parser.add_argument('--rate', help='Shows top 250 films and their rates',
                        action='store_true')
arg_parser.add_argument('--all', help='Shows film and its rate and year',
                        action='store_true')
arg_parser.add_argument('--histogram', help='Shows change of rates by years ')
arg_parser.add_argument('--output', help='Saves data')
args = arg_parser.parse_args()
filename = 'IMDB-Movie-Data.csv'

if os.path.exists(filename):
    data_frame = pd.read_csv(filename)
    if args.year:
        sorted_df = data_frame.sort_values(by=['Year', 'Title'],
                                           ascending=[False, True])[:250]
        result_df = sorted_df[['Title', 'Year']]
    if args.rate:
        sorted_df = data_frame.sort_values(by=['Rating', 'Title'],
                                           ascending=[False, True])[:250]
        result_df = sorted_df[['Title', 'Rating']]
    if args.all:
        result_df = data_frame[['Title', 'Rating', 'Year']]
    if args.histogram == 'rating':
        grouped_df = data_frame.groupby('Rating')['Rating'].count()
        result_df = grouped_df.sort_index(ascending=False)
    if args.histogram == 'year':
        grouped_df = data_frame.groupby('Year')['Year'].count()
        result_df = grouped_df.sort_index(ascending=False)
    if args.output:
        result_df.to_csv(args.output)
    else:
        print(result_df.to_string())
else:
    print("Requested file doesn't exist")
