import matplotlib.pyplot as plt
plt.clf()

years = [1,2,3,4,5]

speed1 = [1.5, 3, 2.5, 4, 5]
speed2 = [8, 6.5, 7, 7.5, 9]
speed3 = [16,	15,	16.5,	17,	16.5]
speed4 = [11,	10,	11.5,	9,	9.5]
speed5 = [13, 16, 15.5, 17, 18]

plt.plot(years, speed1, color = [255/255, 0/255, 0/255], label="African Plate")
plt.plot(years, speed2, color = [250/255,200/255,0/255], label="Antartic Plate")
plt.plot(years, speed3, color = [255/255, 0/255, 0/255], label="Nazca Plate")
plt.plot(years, speed4, color = [250/255,200/255,255/255], label="South America Plate")
plt.plot(years, speed5, color = [255/255, 0/255, 255/255], label="Pacific Plate")
#Add this to adjust the margins
plt.subplots_adjust(left=0.15, right=0.65, top=.9, bottom=0.15)

plt.ylabel("Speed")
plt.xlabel("Years")
#This is the easy way to make a legend
#plt.legend()
#This is the way to adjust where the legend appears
plt.legend(bbox_to_anchor=(1.05, 1.05), loc=2, borderaxespad=0)

plt.show()