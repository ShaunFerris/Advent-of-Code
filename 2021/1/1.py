#Testing data
with open('test.txt', 'r') as f:
    test_measurements = []
    for line in f:
        test_measurements.append(int(line.strip()))

#Actual data
with open('input.txt', 'r') as f:
    measurements = []
    for line in f:
        measurements.append(int(line.strip()))

def one_data_point_delta(measurements):
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
    return depth_delta

def tres_data_point_delta(measurements):
    window_sums = [sum(measurements[i - 2: i + 1]) for i in range(2, len(measurements))]
    return one_data_point_delta(window_sums)

print(tres_data_point_delta(measurements))