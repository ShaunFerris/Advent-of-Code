with open('input.txt', 'r') as f:
    measurements = []
    for line in f:
        measurements.append(line.strip())

print(measurements)