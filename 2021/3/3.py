from copy import deepcopy
import re

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
    most_common_bits = gamma_rate(data)[0]
    considering = deepcopy(data)
    for b in most_common_bits:
        r = re.compile('^' + most_common_bits[:most_common_bits.index(b)])
        considering = list(filter(r.match, considering))
    return considering

print(oxygen_rating(test_bit_strings))