from datetime import date as Date
from flask import jsonify

#dateToDay converts a date into the day-number of the year
def dateToDay(date):
    date = date.split()
    monthDict = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
    }
    day = int(date[0])
    month = monthDict[date[1]]
    year = Date.today().year
    dayNumber = Date(year, month, day).timetuple()[7]
    return dayNumber


#Calculates the maximum profit and filters out the movies the actor should work on.
def maximizeProfit(movies):
    moviesList = list()

    #Coverting the movies list into an array
    for movie in movies:
        moviesList.append([dateToDay(movies[movie]['endtime']), dateToDay(movies[movie]['starttime']), movie ])

    moviesList.sort() #Sorts the array based on the end date of movie

    moviesShouldDo = dict()
    res = [moviesList[0][::-1]]
    moviesShouldDo[res[-1][0]] = movies[res[-1][0]]

    #Filters the movie list
    for i in range(1, len(moviesList)):
        if res[-1][2] < moviesList[i][1]:
            res.append(moviesList[i][::-1])
            moviesShouldDo[res[-1][0]] = movies[res[-1][0]]

    amount = len(moviesShouldDo)

    return {"movies":moviesShouldDo, "amount":"Rs."+str(amount) + " Crore"}