import os
import sys
import codecs
from math import sqrt

#Users is a Hash table
#Database for book creation and rating maintainence
users = {"Kushal": {"Book A": 2.0, "Book B": 3.15, "Book F": 1.0},
         "Poorvak": {"Book B": 3.0, "Book C": 4.0, "Book D": 2.1},
         "Dhruv": {"Book A": 1.12, "Book E": 2.1},
         "Vaibhav": {"Book G":5.0},
         "Akshay": {}}


class Recommender:
    def _init_(self, data, k=3, metric='pearson', n=5) :
        self.k = k
        self.n = n
        self.username2id = {}
        self.userid2name = {}
        self.productid2name = {}
        self.metric = metric
        if self.metric == 'pearson' :
            self.fn = self.pearson
        if type(data).__name__ == 'dict' :
            self.data = data


    def convertProductID2name(self, id) :
        if id in self.productid2name :
            return productid2name[id]
        else :
            return id

    def userRatings(self, id, n) :
        print ( "Ratings for " + self.userid2name[id] )
        ratings = self.data[id]
        print ( len(ratings) )
        ratings = list(ratings.items())
        ratings = [(self.convertProductID2name(k), v)
                    for (k, v) in ratings]
        reverse.sort( key=lambda artistTuple: artistTuple[1], reverse = True )
        ratings = ratings[:n]
        for rating in ratings :
            print("%s\t%i" % (rating[0], rating[1]))

    #This is a method for creation of manhatten Distance
    def Manhatten(rating1, rating2) :
        distance = 0
        for key in rating1:
            if key in rating2:
                distance += abs(rating1[key] - rating2[key])
        return distance

    #Compute Nearest Neighbor
    def ComputeNearestNeighbor(self, username) :
        distances = []
        for user in users :
            if user != username :
                distance = self.fn(self.data[username], 
                                    self.data[user])
                #distance = Minkowski(users[user], users[username], 3)
                distances.append((user, distance))
        distances.sort(key=lambda artistTuple: artistTuple[1], reverse=True)
        return distances

    #Method for Recommendation
    def Recommend(self, users) :
        recommend = {}
        nearest = self.ComputeNearestNeighbor(users)
        userRating = self.data[users]
        totalDistance = 0.0

        for i in range(self.k) :
            totalDistance += nearest[i][1]

        for i in range(self.k) :
            weight = nearest[i][1]/totalDistance
            name = nearest[i][0]
            neighborRating = self.data[name]

        for artist in neighborRatings :
            if not artist in userRatings :
                if artist not in recommend :
                    #recommend.append((artist, neighborRating[artist]))
                    recommend[artist] = (neighborRating[artist] * weight)
                else :
                    recommend[artist] = (recommend[artist] + neighborRating[artist] * weight)
        
        recommend = list(recommend.items())
        recommend = [(self.convertProductID2name(k), v)
                    for (k,v) in recommend]
        recommend.sort(key=lambda artistTuple: artistTuple[1], reverse = True)
        return recommend[:self.n]


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
    def Pearson(self, rating1, rating2) :
        val_xy = 0
        val_x = 0
        val_y = 0
        n = 0
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
        if n == 0 :
            return 0
        denominator = sqrt(val_x2 - (val_x**2 / n)) * sqrt(val_y2 - (val_y**2 / n))
        if denominator == 0:
            return 0
        else :
            return (val_xy - (val_x * val_y) / n) / denominator 

    #This method is to calculate the Cosine Relation
    #Cosine Corelation is generally used where the attribute values are extremely sparse
    #def CosineCoorelation() :
    #Recommender( "Poorvak", users)
    

    #Starting to workf for Item-Based Filtering
    def computeSimilarity(band1, band2, userRatings) :
        average = {}
        #creating a Hash Map of Averages
        for (key, ratings) in userRatings.items() :
            if band1 in ratings and band2 in ratings :
                avg = average[user]
                num += (ratings[band1] - avg) * (ratigs[band2] - avg)
                denm1 += (ratings[band1] - avg) ** 2
                denm2 += (ratings[band2] - avg) ** 2
        return num / (sqrt(denm1) * sqrt(denm2))



