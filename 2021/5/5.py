#This could probably be done better using numpy but I'm going to try not using it.

#Process testing data
with open('testinput.txt', 'r') as f:
    test_lines = [line.strip() for line in f.readlines()]

#Process actual data
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def grid_builder(x=10, y=10):
    '''Builds the 0,0 to 9,9 grid to count line intersections at those 
    coordinates. '.' will mark empty, ints will mark number of lines in 
    the coordinate list that pass through a given point. The grid is
    initialized with every point empty.'''

    return [['.' for i in range(x)] for j in range(y)]

def expand_line(line):
    '''Creates a list representing each point along a line from the 
    point representation of a line (eg: 9,7 -> 7,7) as point a to 
    point b. Determines the lines orientation so that future functions
    can ignore diagonal lines, as this is part of the problem parameters.'''

    x1, x2 = int(line.split()[0].split(',')[0]), int(line.split()[2].split(',')[0])
    y1, y2 = int(line.split()[0].split(',')[1]), int(line.split()[2].split(',')[1])
    if x1 == x2:
        orientation = 'vertical'
    elif y1 == y2:
        orientation = 'horizontal'
    else:
        orientation = 'diagonal'
    x_range = list(range(x1, x2 + 1)) if x1 < x2 else list(range(x2, x1 + 1))
    y_range = list(range(y1, y2 + 1)) if y1 < y2 else list(range(y2, y1 + 1))
    if x1 > x2:
        x_range.reverse()
    if y1 > y2:
        y_range.reverse()
    while len(x_range) < len(y_range):
        x_range.append(x_range[0])
    while len(y_range) < len(x_range):
        y_range.append(y_range[0])
    points_list = []
    for i, j in enumerate(y_range):
        points_list.append((x_range[i], j))
    return points_list, orientation

def plot_points(expanded_line, tracking_grid):
    '''Takes a points list for a given line and a matrix that tracks the 
    lines, and adds this line to the tracking grid.'''

    for point in expanded_line:
        if tracking_grid[point[1]][point[0]] == '.':
            tracking_grid[point[1]][point[0]] = 1
        else:
            tracking_grid[point[1]][point[0]] += 1
    return tracking_grid

def map_lines(lines_data, grid_size=10, mode=0):
    '''Takes the processed input data, a list of strings in format 9,7 -> 7,7
    representing lines to be mapped. Creates a grid matrix to map these lines
    by point, and plots each line. Returns a matrix representing the mapped lines.
    Mode determines wether or not it will ignore diagonal lines. Default 0 will
    ignore diags and only process horizontal or vertical lines.'''

    grid = grid_builder(x=grid_size, y=grid_size)
    for line in lines_data:
        if mode == 0:
            if expand_line(line)[1] == 'vertical' or expand_line(line)[1] == 'horizontal':
                points = expand_line(line)[0]
                grid = plot_points(points, grid)
        elif mode == 1:
            points = expand_line(line)[0]
            grid = plot_points(points, grid)
    return grid

def readable_diagram(lines_data, grid_size=10, mode=0):
    '''Takes the input data, runs the map lines function on it, then tranforms the
    output into a diagram that is easier to compare directly to the example diagram
    for the problem.
    NOTE: Only useful for small subsets like the example used for the testing data,
    where grid size is 10. Not readable on real data where grid size is 1000.'''

    grid_matrix = map_lines(lines_data, grid_size, mode)
    for i in grid_matrix:
        print(''.join([str(j) for j in i]))
    return

def count_hotspots(diagram, threshold=2):
    '''Counts the number of points on a given map of lines x or more lines have
    crossed, where x is the threshold arg. Retuns the count as an int.'''

    count = 0
    for line in diagram:
        for point in line:
            if point != '.' and point >= threshold:
                count +=1
    return count


diagram = map_lines(lines, grid_size=1000, mode=1)
print(count_hotspots(diagram))
#readable_diagram(test_lines, grid_size=10, mode=1)
