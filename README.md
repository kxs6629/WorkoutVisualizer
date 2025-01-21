# Workout Visualizer
Homebrew data visualizer for my workouts over the last year. Ideally I want to build this out to continue to take in future data and display fresh graphs.

## UPDATE
This is serving as just a proof of concept / dusting off python project. I'm starting to work on converting this into a react app that I can use on the go.

## Core Functions
* Consume data and visualize workout progress


## Tech Stack
* Python
    - Plotly
    - Pandas


    ## Overview
* Transferred the txt file I've had on my phone for a year at this point
    - Clean up the data to be in a parseable format
    - Determine ways to read in and visualize all the data
* Conver the txt file to csv
* Consume the data in python
* Visualize it


## Dev Process 

### Data Sanitzation Process
```
Workout type: (scrapped for now, but keeping this for future me)
    generic weight: [`dayAppended`,activity,weight]
    reps : [`dayAppended`,activity,weight,repsXset]
    generic cardio: [`dayAppended`,activity,time]
    cardio : [`dayAppended`,activity,incline,time]
    unspecified : [`dayAppended`,activity]

Data layout:
    
    (day 0)
    blahblah.10
    blahblah.5

    (day 1)
    blahblah,15

    * in the future I'd like to work with actual dates, but I forgor to put it in my notepad x.x*
```
* Had a lot of special characters to indicate uncertainty or side notes
    - Rather than complicate things more, I trimmed a lot of these values to follow the format: [day,activity,quantity/time]
    - Still not sure what to do with the abs 
* Matplotlib and numpy are proving to be a pain with consuming this data...
    - Looking into pandas and other plotting libraries
    - Plotly?
* Wow, plotly made this super easy. Marking this project as done and moving on to version 2.


### Going Forward...
* How can I get this to update with new data as I continue to work out?
    - Use actual timestamps with this implementation?
* I decided to have this serve as a proof of concept. Next project will be reworking this into a web app I can use on the go and at home