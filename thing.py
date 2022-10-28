RESOLUTION = 50
samples = []

import csv
import math
with open('in.csv') as file:
	reader = csv.reader(file)
	coords = [(float(row[0]), float(row[1])) for row in reader]
	for (i, coord) in enumerate(coords):
		lastCoord = coords[(i - 1) % len(coords)]

		dx = coord[0] - lastCoord[0]
		dy = coord[1] - lastCoord[1]
		dist = math.sqrt(dx ** 2 + dy ** 2)
		sampleCount = math.ceil(dist * RESOLUTION)

		for step in range(sampleCount):
			dxStep = dx / sampleCount * step
			dyStep = dy / sampleCount * step
			stepx = (lastCoord[0] + dxStep)
			stepy = (lastCoord[1] + dyStep)

			samples.append(int(stepy * 255))
			samples.append(int(stepx * 255))


import wave
with wave.open('out.wav', 'wb') as file:
	file.setnchannels(2)
	file.setsampwidth(1)
	file.setframerate(44100)
	file.writeframes(bytes(samples))
