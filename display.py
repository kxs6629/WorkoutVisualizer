import consume as c
import matplotlib as plt
import numpy as np

# Right now I just want to take in the data from consume.py and display line graphs
# in a window where you can change the data set on the fly (various activities)

data = c.consume('data/work.txt')

# Now that I have all of this data, I need to find a way to get it mapped in graph friendly format
workoutTypes = set()
for i in data:
    curActivity = i[1]
    if curActivity not in workoutTypes:
        workoutTypes.add(curActivity)
print(workoutTypes)
print(data[0])
print(data[0][1])
# print(data['BENCH'])
# np.select((data[0][1] == "BENCH"),data)


# for type in workoutTypes:
#     np.where(data[1] == type)
# data[0]
# data[1 == 'BENCH']
# Time to figure out how to:
# Display a single data set
# Switch data set, refresh graph (preferably in the UI)
# Display a l l 

# In the future, this should have a prettier interface
# - lowkey if I get this far I'm starting from scratch and making a react app