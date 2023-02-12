import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import the csv files into the dataframe
dfGB = pd.read_csv('GBvideos.csv')
dfUS = pd.read_csv('USvideos.csv')

#create a new column to see the dislike ratio
dfGB['dislike_ratio'] = dfGB.likes/dfGB.dislikes
dfUS['dislike_ratio'] = dfUS.likes/dfUS.dislikes

#Clean Data remove all NaN and inf
dfGB.replace([np.inf, -np.inf], np.nan, inplace=True)
dfGB.dropna()
dfUS.replace([np.inf, -np.inf], np.nan, inplace=True)
dfUS.dropna()

#Calculate the average dislike ratio in each country
avg_dislike_ratioGB = dfGB["dislike_ratio"].mean()
avg_dislike_ratioUS = dfUS["dislike_ratio"].mean()
print(avg_dislike_ratioGB)
print(avg_dislike_ratioUS)

#Change data column to datetime format in pandas
dfGB['trending_date'] = pd.to_datetime(dfGB['trending_date'], format='%y.%d.%m')
dfUS['trending_date'] = pd.to_datetime(dfUS['trending_date'], format='%y.%d.%m')
#Create year column and seperate data for just 2018
dfGB['year'] = dfGB['trending_date'].dt.year
dfGB_2018 = dfGB[dfGB['year'] == 2018]
dfUS['year'] = dfUS['trending_date'].dt.year
dfUS_2018 = dfUS[dfUS['year'] == 2018]
#find the mean of the likes in 2018
GB_mean_likes_2018 = dfGB_2018['likes'].mean()
print(GB_mean_likes_2018)
US_mean_likes_2018 = dfUS_2018['likes'].mean()
print(US_mean_likes_2018)

#Analyze data to find out if the most polarizing Videos get watched the most
plt.scatter(dfGB['views'], dfGB['dislike_ratio'], label = 'GB Data')
plt.scatter(dfUS['views'], dfUS['dislike_ratio'], label = 'US Data')
plt.legend(loc='upper left')
plt.xlabel('Views')
plt.ylabel('Ratio of Likes to Dislikes')
plt.show()

'''
from the image we can see that the relationship of views and dislike ratio was negative
this implies that the most polarizing videos do in fact get the most views
'''

