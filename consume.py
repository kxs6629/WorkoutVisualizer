def consume(filename):
    dataFile= open(filename, "r")
    
    day = 0
    activityMap = {}
    for line in dataFile:
        if line == "\n":
            day+=1
        else:
            curLine = line.split(',')
            dataLen = len(curLine)
            if dataLen == 1:
                print("generic activity")
            elif dataLen == 2:
                print("")
            elif dataLen == 3:
                print()
            else:
                print("not sure how you got here man")
            day+=1

    dataFile.close()
    return activityMap