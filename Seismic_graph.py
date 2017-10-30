import matplotlib.pyplot as plt

plt.clf()
DataFile = open("seismic_data.txt")

column_names = dataFile.readline()
print(column_names)

times = []
s_wave = []
p_wave = []


for line in DataFile:
	line = line.split(',')
	times.append(float(line[0]))
	s_wave.append(float(line[1]))
	p_wave.append(float(line[2]))


plt.plot(times,s_wave, label = "s_wave")
plt.plot(times,p_wave, label = "p_wave")

plt.xlabel("Time (min)")
plt.ylabel("Distance from Focus (km)")
plt.legend()
plt.show()