import matplotlib.pyplot as plt
plt.clf()

# Data from "The dynamics of Cenozoic and Mesozoic plate motions" (100-74 mya)
# doi=10.1029/97RG02282 
# using Rice University Plate Motion Calculator
# http://tectonics.rice.edu/calculators/hs3.html
# and "Young tracks of hotspots and current plate velocities" (current speed)
# doi=10.1046/j.1365-246X.2002.01627.x
# Speeds are in mm/yr relative to hotspots

Mya = [1, 2, 3, 4, 5, 6]
Xlabels = ["100-119", "94-100", "84-94", "74-84", "64-74", "0"]

AfSpeeds = [20.1, 20.04, 20.04, 21.13, 21.13, 16]
AnSpeeds = [22.43, 22.43, 22.43, 16.36, 7.03, 15]
NoSpeeds = [33.38, 33.26, 30.72, 36.75, 33.39, 41]
SoSpeeds = [43.69, 43.29, 43.29, 38.78, 40.72, 45]
PaSpeeds = [74.99, 42.72, 42.72, 42.72, 76.48, 81]
InSpeeds = [15.5, 16.67, 16.67, 26.63, 37.95, 50]

# Layer plots for each continent
plt.plot(Mya, AfSpeeds, color = "purple", marker = "|", label="African Plate")
plt.plot(Mya, AnSpeeds, color = "blue", marker = "|", label="Antartic Plate")
plt.plot(Mya, NoSpeeds, color = "deepskyblue", marker = "|", label="North America Plate")
plt.plot(Mya, SoSpeeds, color = "green", marker = "|", label="South America Plate")
plt.plot(Mya, PaSpeeds, color = "orange", marker = "|", label="Pacific Plate")
plt.plot(Mya, InSpeeds, color = "red", marker = "|", label="India Plate")

# Add axis and tick labels
plt.xticks(Mya, Xlabels)
plt.ylabel("Speed (km/myr)")
plt.xlabel("Time (mya)")

# Add a title
plt.suptitle("Change in tectonic plate speed over time", x = .39)

# This is the easy way to make a legend
# plt.legend()

# This is the way to adjust where the legend appears
plt.legend(bbox_to_anchor=(1.05, 1.05), loc = 2, borderaxespad=0)

# Adjust the margins to add space for the legend
plt.subplots_adjust(left=0.15, right=0.65, top=.9, bottom=0.15)

plt.show()