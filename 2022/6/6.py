#test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
#test2 = 'nppdvjthqldpwncqszvftbrmjlhg'
#test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

def buffer_scan(buffer):
    count = 0
    SOP_address = 0
    for index, char in enumerate(buffer):
        if count == 4:
            break
        slice = buffer[index : index + 4]
        for c in slice:
            if slice.count(c) > 1:
                count = 0
                break
            else : count += 1
            if count == 4:
                SOP_address = buffer.find(slice) + 4
                break
    return (SOP_address)

def buffer_scan_message(buffer):
    count = 0
    SOM_address = 0
    for index, char in enumerate(buffer):
        if count == 14:
            break
        slice = buffer[index : index + 14]
        for c in slice:
            if slice.count(c) > 1:
                count = 0
                break
            else : count += 1
            if count == 14:
                SOM_address = buffer.find(slice) + 14
                break
    return (SOM_address)

file = open('input.txt')
buffer = file.read()
print(buffer_scan(buffer))
print(buffer_scan_message(buffer))