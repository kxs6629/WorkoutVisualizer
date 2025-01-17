##Overview
* Transferred the txt file I've had on my phone for a year at this point
    - Clean up the data to be in a parseable format
    - Determine ways to read in and visualize all the data
* Consume the data in python
* Visualize it


## Data Sanitzation Process
```
Workout type:
    generic weight: [`dayAppended`,activity,weight]
    reps : [`dayAppended`,activity,weight,repsXset]
    generic cardio: [`dayAppended`,activity,time]
    cardio : [`dayAppended`,activity,incline,time]
    unspecified : [`dayAppended`,activity]

Data layout:
    
    (day 0)
    blahblah
    blahblah

    (day 1)
    blahblah

    * in the future I'd like to work with actual dates, but I forgor to put it in my notepad x.x*
```
* Had a lot of special characters to indicate uncertainty or side notes
    - Rather than complicate things more, I trimmed a lot of these values to follow the 3 format categories above
    - Still not sure what to do with the abs 




## Going Forward...
* How can I get this to update with new data as I continue to work out?
    - Use actual timestamps with this implementation