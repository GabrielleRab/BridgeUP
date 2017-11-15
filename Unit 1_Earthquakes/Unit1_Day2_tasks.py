AfSpeeds = [20.1, 20.04, 20.04, 21.13, 21.13]
AnSpeeds = [22.43, 22.43, 22.43, 16.36, 7.03]
NoSpeeds = [33.38, 33.26, 30.72, 36.75, 33.39]
SoSpeeds = [43.69, 43.29, 43.29, 38.78, 40.72]
PaSpeeds = [74.99, 42.72, 42.72, 42.72, 76.48]
InSpeeds = [15.5, 16.67, 16.67, 26.63, 37.95]

print("#1.", len(AfSpeeds))

# print("#2.", 42.72-16.67)
print("#2.", PaSpeeds[2] - InSpeeds[2])

print("#3.", sum(AnSpeeds) / (len(AnSpeeds)))

AfSpeeds.append(16)
AnSpeeds.append(15)
NoSpeeds.append(41)
SoSpeeds.append(45)
PaSpeeds.append(81)
InSpeeds.append(50)

print("#4.", AfSpeeds)
