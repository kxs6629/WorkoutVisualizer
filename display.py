import consume as c
import matplotlib as plt

# Right now I just want to take in the data from consume.py and display line graphs
# in a window where you can change the data set on the fly (various activities)

data = c.consume('data/work.txt')
print(data)
# Now that I have all of this data, I need to find a way to get it mapped in graph friendly format


# In the future, this should have a prettier interface
# lowkey if I get this far I'm starting from scratch and making a react app
# Once I'm satisfeid with the desktop version, I can worry about making this mobile