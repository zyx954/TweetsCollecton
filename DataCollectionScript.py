#import tweepy
import time
import twitter
import json
import pickle,pprint
from itertools import cycle

import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine


#usign tweepy
def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information
    # on Twitter's OAuth implementation.

    # use your own key
    CONSUMER_KEY = 'XXX'
    CONSUMER_SECRET = 'XXX'
    OAUTH_TOKEN = 'XXX'
    OAUTH_TOKEN_SECRET = 'XXX'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth,retry=True)
    return twitter_api


# Sample usage
twitter_api = oauth_login()


fileNames = ['xaa', 'xab', 'xac']
for filename in fileNames:
    # the filename formate is  'xba'  'xbb'
    #======get data from file to ListDict

    #manipulate  filename into  the formate as "./SplitAs90000/xbe"
    fileName4Read = './SplitAs90000/' + filename
    file = open(fileName4Read,"r")
    try:
        lines = file.readlines()
        # print lines[0]
        # print lines[1]N
        # print lines[2]

        ListItems = []

        for s in lines:
            # print lines[s]
            items = s.split(",")
            # ListItems[3]=4
            ListItems.append({'tweetsID':items[0],'maliciousResult':items[1],'annotationMethod':items[2]})
    finally:
        file.close()



    print "get " +str(len(ListItems)) + "  lines data list[ dict {} ]"
    # print  ListItems[1999]["tweetsID"]
    #



    # #==========
    List4TweetsResponse = []
    running = True
    ListDicts = cycle(ListItems)
    stopIterationCounter = len(ListItems)
    counter = 0
    errorCounter=0
    #     # print tweetsID

    while running:
        if(counter ==stopIterationCounter):
            break
        DataDict = ListDicts.next()
        try:
            tweetsResonse = twitter_api.statuses.show(_id=DataDict["tweetsID"])
            tweetsResonse.maliciousResult = DataDict["maliciousResult"]
            tweetsResonse.annotationMethod = DataDict["annotationMethod"]
            List4TweetsResponse.append(tweetsResonse)
        except:
            print "catch error for " + DataDict["tweetsID"]
            errorCounter= errorCounter+1
        counter=counter+1
        # print DataDict
    try:
        print "the number of data withinfile " + str(len(List4TweetsResponse))
        print "the number of invalid data  " + str(errorCounter)
        print "total number of data" + str(len(List4TweetsResponse)+errorCounter)
    except:
        pass



    try:
        # manipulate  filename  into  the formate as "'xbeData.pkl'"
        fileName4Load = filename + 'Data.pkl'
        output = open(fileName4Load, 'w')

        # Pickle dictionary using protocol 0.
        print List4TweetsResponse[0].annotationMethod
        pickle.dump(List4TweetsResponse, output)
    finally:
        output.close()

#==============finish writing data to file======
