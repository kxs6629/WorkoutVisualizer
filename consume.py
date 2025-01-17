def consume(filename):
    dataFile= open(filename, "r")
    
    day = 0
    activityMap = []
    for line in dataFile:
        if line == "\n":
            day+=1
        else:
            cleanCut = line.rstrip()
            curLine = cleanCut.split(',')
            dataLen = len(curLine)
            if dataLen == 1:
                activityMap.append([day,curLine[0]])
                print("generic activity")
            elif dataLen == 2:
                activityMap.append([day,curLine[0],int(curLine[1])])
                print("")
            elif dataLen == 3:
                activityMap.append([day,curLine[0],curLine[1],curLine[2]])
                print()
            else:
                print("not sure how you got here man")

    dataFile.close()
    return activityMap