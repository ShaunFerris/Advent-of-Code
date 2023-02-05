from copy import deepcopy

#Test data
with open('test.txt', 'r') as f:
    test_bit_strings = [f.strip() for f in f.readlines()]

#Actual data
with open('input.txt', 'r') as f:
    bit_strings = [f.strip() for f in f.readlines()]

def most_common(lst):
    return max(lst, key=lst.count)

def gamma_rate(data):
    '''Gets the most common bit in each string index for any number
    bit strings of any length'''
    bit_map = {indx: [] for indx, b in enumerate(data[0])}
    for bit_string in data:
        for indx, bit in enumerate(bit_string):
            bit_map[indx].append(bit)
    gamma_string = ''
    for i in bit_map.values():
        gamma_string += most_common(i)
    gamma_number = int(gamma_string, base=2)
    return gamma_string, gamma_number

def epsilon_rate(data):
    '''Opposite of gamma rate, least common bit at each index for a
    number of bit strings'''
    mirror = gamma_rate(data)[0]
    epsilon_string = ''
    for i in mirror:
        if i == '1':
            epsilon_string += '0'
        elif i == '0':
            epsilon_string += '1'
    epsilon_number = int(epsilon_string, base=2)
    return epsilon_string, epsilon_number

gam = gamma_rate(test_bit_strings)
ep = epsilon_rate(test_bit_strings)
print(gam, ep, gam[1] * ep[1])

def oxygen_rating(data):
    oxygen_data = deepcopy(data)
    count = 0
    while len(oxygen_data) > 1:
        zeros, ones = 0, 0
        for bit_string in oxygen_data:
            if bit_string[count] == '0':
                zeros += 1
            elif bit_string[count] == '1':
                ones += 1
        if zeros > ones:
            oxygen_data = [bit_string for bit_string in oxygen_data if bit_string[count] == '0']
        elif ones > zeros or ones == zeros:
            oxygen_data = [bit_string for bit_string in oxygen_data if bit_string[count] == '1']
        count += 1
        oxygen_number = int(oxygen_data[0], base=2)
    return oxygen_data, oxygen_number

def co2_rating(data):
    co2_data = deepcopy(data)
    count = 0
    while len(co2_data) > 1:
        zeros, ones = 0, 0
        for bit_string in co2_data:
            if bit_string[count] == '0':
                zeros += 1
            elif bit_string[count] == '1':
                ones += 1
        if zeros > ones:
            co2_data = [bit_string for bit_string in co2_data if bit_string[count] == '1']
        elif ones > zeros or ones == zeros:
            co2_data = [bit_string for bit_string in co2_data if bit_string[count] == '0']
        count += 1
        co2_number = int(co2_data[0], base=2)
    return co2_data, co2_number

o = oxygen_rating(bit_strings)[1]
c = co2_rating(bit_strings)[1]
print(o * c)