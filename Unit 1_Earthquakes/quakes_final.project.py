import matplotlib.pyplot as plt
image = plt.imread("earth.jpg")
image = plt.imread("plates.png")
fig, ax = plt.subplots()

ax.imshow(image, extent = [-180,180,-90,90])

quakes = open("currentQuakes.txt", 'r')
quakes.readline()

lats = []
lons = []
cols = []


### ADD IN conditionals for colors based on mags
for quake in quakes:
	quake_data = quake.split(',')
	lat = float(quake_data[1])
	lon = float(quake_data[2])
	lats.append(lat)
	lons.append(lon)
	if float(quake_data[4]) < 3.5:
		cols.append([25/255,25/255,75/255])
	elif float(quake_data[4]) < 5.0:
		cols.append([0/255,0/255,250/255])
	else:
		cols.append([150/255,150/255,250/255])

#volcanoes = open("volcanoes.txt", 'r')
#volcanoes.readline()

# #for eruption in volcanoes:
# 	eruption_data = eruption.split(',')
# 	lat = float(eruption_data[8])
# 	lon = float(eruption_data[9])
# 	lats.append(lat)
# 	lons.append(lon)
# 	if eruption_data[14] != " ":
# 		if float(eruption_data[14]) < 3:
# 			cols.append([75/255,25/255,25/255])
# 		elif float(eruption_data[14]) < 5:
# 			cols.append([255/255,0/255,0/255])
# 		else:
# 			cols.append([250/255,150/255,150/255])
# 	else:
# 		cols.append([255/255,0/255,0/255])

plt.scatter(x=lons,y=lats, c= cols)
plt.show()