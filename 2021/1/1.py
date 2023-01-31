with open('input.txt', 'r') as f:
    measurements = []
    for line in f:
        measurements.append(int(line.strip()))

depth_delta = {'increase': 0, 'decrease': 0}
current_depth = 0
for measurement in measurements:
    if current_depth == 0:
        current_depth = measurement
        continue
    elif measurement > current_depth:
        depth_delta['increase'] += 1
        current_depth = measurement
    elif measurement < current_depth:
        depth_delta['decrease'] += 1
        current_depth = measurement
print(depth_delta)