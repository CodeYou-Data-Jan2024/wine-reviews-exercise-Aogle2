import pandas as pd

datasource = r"data/winemag-data-130k-v2.csv.zip"

main_df = pd.read_csv(datasource,index_col=0)

#print(main_df.columns())

#print(new_df.columns)

#print(main_df.country.value_counts())

#print(main_df["points"] )

country_values = main_df.country.iloc[6:].value_counts()
country_points = main_df.points.iloc[6:].round(2).idxmax()

new_df = pd.DataFrame(data={'country':[main_df.country],
			'counts':[country_values],
			'points':[country_points] })
#print(country_values)
#print(f"{country_points}")
#new_df['country'] = main_df.country.iloc[6:]
#new_df['counts'] = main_df.country.iloc[6:].value_counts()
#new_df['points'] = main_df.points.iloc[6:].round(1).idxmax()


print(new_df.columns)
print(new_df.head())
print(new_df)
