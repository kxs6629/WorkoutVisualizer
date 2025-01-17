def consume(filename):
    dataFile= open(filename, "r")
    
    day = 0
    activityMap = []
    # parse data file
    for line in dataFile:
        # if line is just a new line, that means new day
        if line == "\n":
            day+=1
        else:
            cleanCut = line.rstrip()
            curLine = cleanCut.split(',')
            dataLen = len(curLine)
            # gets a little ugly here, but I need to sanitize it 
            # To future me, we're working on sorting out how to store weight, time, etc. for the y value
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