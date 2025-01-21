import pandas as pd

import consume as c
import cleanData as cd

# Right now I just want to take in the data from consume.py and display line graphs
pd.options.plotting.backend = "plotly"

cd.formatFile('data/work.txt')
data = c.consume('data/formattedData.csv')

# Now that I have all of this data, I need to find a way to plot it
# Time to figure out how to:
# Display a single data set
# Switch data set, refresh graph (preferably in the UI)
# Display a l l 

# lmao nevermind plotly and panda made so easy???
fig = data.plot(title="Workout Visualizer",x="Day",y="Weight(lbs)/Time(seconds)",color="Activity")
fig.show()


# In the future, this should have a prettier interface
# - lowkey if I get this far I'm starting from scratch and making a react app
# time to start working on version 2!