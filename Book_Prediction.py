import os
import sys
import codecs
from math import sqrt

#Users is a Hash table
users = {"Kushal": {"Book A": 2.0, "Book B": 3.15, "Book F": 1.0},
         "Poorvak": {"Book B": 3.0, "Book C": 4.0, "Book D": 2.1},
         "Dhruv": {"Book A": 1.12, "Book E": 2.1},
         "Vaibhav": {"Book G":5.0},
         "Akshay": {}}

"""
class Recommender:
    def _init_(self, data, k=3, metric='pearson', n=5) :
        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        self.metric = metric
        if self.metric == 'pearson' :
            self.
"""

#This is a method for creation of manhatten Distance
def Manhatten(rating1, rating2) :
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

#Compute Nearest Neighbor
def ComputeNearestNeighbor(username, users) :
    distances = []
    for user in users :
        if user != username :
            distance = Minkowski(users[user], users[username], 3)
            distances.append((distance, user))
    distances.sort()
    return distances

#Method for Recommendation
def Recommender(username, users) :
    recommend = []
    nearest = ComputeNearestNeighbor(username, users)[0][1]
    userRating = users[username]
    neighborRating = users[nearest]
    for artist in neighborRating :
        if not artist in userRating :
            recommend.append((artist, neighborRating[artist]))
    return sorted(recommend, key=lambda artistTuple: 1, reverse = True)


#This method is to calculate the Minkowski distance
def Minkowski(rating1, rating2, r) :
    distances = []
    commonValue = False
    for key in rating1:
        if key in rating2:
            distances += pow(abs(rating1[key] - rating2[key]), r)
            commonValue = True
    if commonValue:
        return pow(distances, 1/r)
    else:
        return 0

#This is a Pearson Coorelation function for the Module
def Pearson(rating1, rating2) :
    val_xy = 0
    val_x = 0
    val_y = 0
    n = 1
    val_x2 = 0
    val_y2 = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            val_xy += x * y
            val_x += x
            val_y += y
            val_x2 += x**2
            val_y2 += y**2
    denominator = sqrt(val_x2 - (val_x**2 / n)) * sqrt(val_y2 - (val_y**2 / n))
    if denominator == 0:
        return 0
    else :
        return (val_xy - (val_x * val_y) / n) / denominator 

#This method is to calculate the Cosine Relation
#Cosine Corelation is generally used where the attribute values are extremely sparse
#def CosineCoorelation() :
    



