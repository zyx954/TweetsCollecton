
import pickle

fileNames = ['xbf', 'xbg', 'xbh', 'xbi', 'xbj']
for fileName in fileNames:
    try:
        #manipulate  filename into  the formate as "./SplitAs90000/xbe"
        fileName4Read='./SplitAs90000/'+fileName
        # print fileName
        print fileName
        file = open(fileName4Read,"r")
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
        pass
        file.close()

    try:
        # manipulate  filename  into  the formate as "'xbeData.pkl'"
        fileName4Load =fileName+ 'Data.pkl'
        output = open(fileName4Load, 'w')

        # Pickle dictionary using protocol 0.
        # print List4TweetsResponse[0].annotationMethod
        pickle.dump('test', output)
    finally:
        output.close()