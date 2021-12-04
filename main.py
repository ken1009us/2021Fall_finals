from scipy import stats

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# import cartopy

def loadFile():
	areaName = input('Which area? (Montreal, Toronto, Washington): ')

	# nrows=10000000
	trips_df = pd.read_csv(f'data/{areaName}/trips.csv', delimiter=',', nrows=1000)
	# print(trips_df.head())
	# print(trips_df.dtypes)

	stations_df = pd.read_csv(f'data/{areaName}/stations.csv', delimiter=',')
	# print(stations_df.head())
	# print(stations_df.dtypes)

	weather_df = pd.read_csv(f'data/{areaName}/weather.csv', delimiter=',')
	# print(weather_df.head())
	# print(weather_df.dtypes)

	return trips_df, stations_df, weather_df


def dataPreprocessing(trips_df, weather_df):
	trips_df = trips_df
	# convert date to datetime
	trips_df['start_date']= pd.to_datetime(trips_df['start_date'])
	trips_df['end_date']= pd.to_datetime(trips_df['end_date'])
	# print(trips_df['start_date'])
	# print(trips_df['end_date'])

	# filter the dataframe, remove the rows that the duration is smaller than zero.
	trips_df = trips_df[trips_df['duration_sec'] > 0]
	# print(trips_df)

	# convert date to datetime
	weather_df['date']= pd.to_datetime(weather_df['date'])

	return trips_df, weather_df


def dataAnalysis(new_trips_df, new_weather_df):
	new_trips_df = new_trips_df
	new_weather_df = new_weather_df

	# Hypothesis #1: Total daily trips duration depends on weather conditions.
	# print(new_weather_df.describe())
	# print(new_trips_df['start_date'].dtype)

	# convert to pandas series date type, remove the time, and add the new column called start_date_day
	new_trips_df['start_date_day'] = new_trips_df['start_date'].dt.date
	# group by the start_date_day, and summarize the duration.
	daily_trips = new_trips_df.groupby(['start_date_day'])['duration_sec'].sum()
	# print(daily_trips)

	# set index to the date.
	new_weather_df = new_weather_df.set_index('date')
	# print(new_weather_df.head())

	# Merge the dataframe new_weather_df and daily_trip, and drop the rows which values are N/A.
	weather_duration_relation_df = pd.concat([new_weather_df, daily_trips], axis=1)
	weather_duration_relation_df = weather_duration_relation_df.dropna()
	# print(weather_duration_relation_df)

	# generate discriptive statistic
	dis_stat = round(weather_duration_relation_df.describe(), 2)
	# print(dis_stat)

	# preprocessing the column of yearid.
	column_name_list = weather_duration_relation_df.columns.values.tolist()
	if 'yearid' in column_name_list:
		column_name_list.remove('yearid')

	# skip the final column (duration_sec).
	column_name_list = column_name_list[0:-1]

	for i in range(len(column_name_list)):
		print(stats.pearsonr(weather_duration_relation_df[column_name_list[i]],
                         	 weather_duration_relation_df['duration_sec']))

	stat = round(weather_duration_relation_df.corr(), 2)
	# round(stat,2)
	print(stat)

	return column_name_list, weather_duration_relation_df, stat


def plotScatter(column_name_list, weather_duration_relation_df, stat):
	column_name_list = column_name_list
	weather_duration_relation_df = weather_duration_relation_df

	fig, ax = plt.subplots(4, 5, figsize=(30,25))
	j, k = 0, 0
	for i in range(len(column_name_list)):
	    ax[j, k].scatter(weather_duration_relation_df[column_name_list[i]],
						 weather_duration_relation_df['duration_sec'],
						 alpha=0.7)

	    ax[j, k].set_title(column_name_list[i])

	    k += 1
	    if k > 4:
	        j += 1
	        k = 0

	fig.tight_layout()
	ax[3,4].set_axis_off()
	plt.show()


def plotHeatMap(stat):
	stat = stat
	plt.figure(figsize = (12,8))
	sns.heatmap(stat, linewidths=.7, cmap="YlGnBu")
	plt.show()


if __name__ == '__main__':
	trips_df, stations_df, weather_df = loadFile()
	new_trips_df, new_weather_df = dataPreprocessing(trips_df, weather_df)
	column_name_list, weather_duration_relation_df, stat = dataAnalysis(new_trips_df, new_weather_df)
	plotScatter(column_name_list, weather_duration_relation_df)
	plotHeatMap(stat)
