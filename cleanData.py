# rather than painstakingly going through the data again, I'm making this script
def formatFile(filename):
    dataFile= open(filename, "r")
    newFile  = open('data/formattedData.csv',"w")
    newFile.write("day,activity,weight/time\n")
    day = 0
    for line in dataFile:
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
                newFile.write(str(day)+","+curLine[0].strip().upper()+","+str(formatY(curLine[1]))+"\n")
            elif dataLen == 3:
                newFile.write(str(day)+","+curLine[0].strip().upper()+","+str(formatY(curLine[2]))+"\n")

    dataFile.close()
    newFile.close()


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