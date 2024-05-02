import pandas as pd

datasource = r"data/winemag-data-130k-v2.csv.zip"

main_df = pd.read_csv(datasource,index_col=0)

agg_df = main_df[['country','points']].groupby('country').count().reset_index() #Creates a new DF of country and points, then isolates the unigue rows in country and then counti it.

points_df = main_df[['country','points']].groupby('country').agg('mean').round(1).reset_index() #Does the same as above but gets the mean and also rounds it by one decimal

final_df = agg_df.rename(columns={'points':"count"}) #renames counts to points

final_df['points'] = points_df['points']

print(final_df.to_csv("data/reviews-per-country.csv"))
