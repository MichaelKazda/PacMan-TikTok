import pymongo
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12, 8] #Set the plot size
uri = 'mongodb+srv://packman:MIB123456@packman-mib-wil2x.azure.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient(uri)
db = client.userData
collection = db.userData

europeanUnionCountries= ['Spain','Germany','France']
numUserStats = "1"
def autolabel(rects):
    #Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{:,}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

for country in europeanUnionCountries:
	usersTags = []
	followers = []
	#Top 10 most followed TikTok users by country in the database.
	for user in list(collection.find({'userRegion': country}, {'_id': False,'userTag':1,'userStats':1}).sort("userStats."+numUserStats+".userFollowers",pymongo.DESCENDING).limit(10)):
		usersTags.append(user['userTag'])
		followers.append(user['userStats'][int(numUserStats)]['userFollowers'])
	#bar graph for each country	
	bar = plt.bar(usersTags,followers,color='purple')
	autolabel(bar)
	plt.title("Top 10 most followed from "+country)
	plt.xlabel("Users")
	plt.ylabel("Followers")
	plt.xticks(rotation=30)
	plt.ylim(0, 20000000) 
	plt.show()