# This version of the activity introduces dictionaries and for loops

import matplotlib.pyplot as plt
plt.clf()

# Data from "The dynamics of Cenozoic and Mesozoic plate motions" (100-74 mya)
# doi=10.1029/97RG02282 
# using Rice University Plate Motion Calculator
# http://tectonics.rice.edu/calculators/hs3.html
# and "Young tracks of hotspots and current plate velocities" (current speed)
# doi=10.1046/j.1365-246X.2002.01627.x
# Speeds are in mm/yr relative to hotspots

# Create a dictionary with the plate names as the keys and a list of speeds as the values
Speeds = {
    "African Plate": [20.1, 20.04, 20.04, 21.13, 21.13, 16],
    "Antarctic Plate": [22.43, 22.43, 22.43, 16.36, 7.03, 15],
    "North American Plate": [33.38, 33.26, 30.72, 36.75, 33.39, 41],
    "South American Plate": [43.69, 43.29, 43.29, 38.78, 40.72, 45],
    "Pacific Plate": [74.99, 42.72, 42.72, 42.72, 76.48, 81],
    "Indian Plate": [15.5, 16.67, 16.67, 26.63, 37.95, 50] 
    }

# Create a dictionary
Colors = {
    "African Plate": "purple",
    "Antarctic Plate": "blue",
    "North American Plate": "deepskyblue",
    "South American Plate": "green",
    "Pacific Plate": "orange",
    "Indian Plate": "red"
    }

# Add information about the x axis
Xaxis = [1, 2, 3, 4, 5, 6]
Xlabels = ["100-119", "94-100", "84-94", "74-84", "64-74", "0"]

# Use a for loop to create plots for each plate
for plate in Speeds:
    plt.plot(Xaxis, Speeds[plate], color = Colors[plate], marker = "|", label=plate)
    
# Add axis and tick labels
plt.xticks(Xaxis, Xlabels)
plt.ylabel("Speed (km/myr)")
plt.xlabel("Time (mya)")

# Add a title
plt.suptitle("Change in tectonic plate speed over time", x = .39)

# Create a legend and sdjust where it appears
plt.legend(bbox_to_anchor=(1.05, 1.05), loc = 2, borderaxespad=0)

# Adjust the margins to add space for the legend
plt.subplots_adjust(left=0.15, right=0.65, top=.9, bottom=0.15)

plt.show()