# rather than painstakingly going through the data again, I'm making this script
def formatFile(filename):
    dataFile = open(filename, "r",newline="\n")
    newFile  = open("data/formattedData.csv","w",newline="\n")

    newFile.write("Day,Activity,Weight(lbs)/Time(seconds)\n")
    day = 0
    
    for line in dataFile:
        if line == "\n":
            day+=1
        else:
            cleanCut = line.rstrip()
            curLine = cleanCut.split(',')
            dataLen = len(curLine)
            if dataLen == 2:
                newFile.write(str(day)+","+curLine[0].strip().upper()+","+str(formatY(curLine[1]))+"\n")
            elif dataLen == 3:
                newFile.write(str(day)+","+curLine[0].strip().upper()+","+str(formatY(curLine[2]))+"\n")

    dataFile.close()
    newFile.close()


# Converts the quantity/time column values in a easier to display format
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