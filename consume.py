import numpy as np

def consume(filename):
    dataFile= open(filename, "r")
    
    day = 0
    dataList = []
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
            # if dataLen == 1:
            #     dataList.append([int(day),curLine[0]])
            if dataLen == 2:
                dataList.append([int(day),curLine[0].strip().upper(),formatY(curLine[1])])
            elif dataLen == 3:
                dataList.append([int(day),curLine[0].strip().upper(),formatY(curLine[2])])

    dataFile.close()
    return np.array(dataList) 

# So this is the dirty part
# Down the line I wanna come back here and tidy things up some more
def formatY(val):
    if ':' in val:
        timeVal = val.split(':')
        timeInSec = (int(timeVal[0]) * 60) + int(timeVal[1])
        return timeInSec
    elif 'x' in val:
        repVal = val.split('x')
        return int(repVal[0])*int(repVal[1])
    elif '.' in val:
        return int(float(val))
    else:
        return int(val)