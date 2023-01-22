with open('input.txt', 'r') as f:
    data = f.readlines()

def calorie_counter(lines, number_of_elves=1):
    elves = []
    curr_elf = 0
    for cal in lines:
        if cal != '\n':
            curr_elf +=int(cal)
        elif cal == '\n':
            elves.append(curr_elf)
            curr_elf = 0
    elves = sorted(elves, reverse=True)
    output_elves = []
    for i in range(0, number_of_elves):
        output_elves.append(elves[i])
    if number_of_elves == 1:
         return output_elves
    else:
        return sum(output_elves)
print(calorie_counter(data, number_of_elves=3))