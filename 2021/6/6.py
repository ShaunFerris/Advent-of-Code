test = [3, 4, 3, 1, 2]

with open('input.txt', 'r') as f:
    fish = [int(fish) for fish in f.read().split(',')]

def organise_school(school):
    '''Creates a dictionary of the number of fish that are each a 
    given number of days from spawning.'''

    return {clock: school.count(clock) for clock in range(0, 9)}

def increment_day(organised_school, no_of_days):
    '''Takes an orgainised school of fish and then calculates how it
    would look after a given number of days.'''
    
    while no_of_days > 0:
        for clock, count in organised_school.items():
            if clock == 0:
                new_borns = count
                just_bred = count
            else:
                organised_school[clock - 1] = count
            if clock == 8:
                organised_school[8] = new_borns
                organised_school[6] += just_bred
                no_of_days -= 1
    return organised_school

school = organise_school(fish)
after = increment_day(school, 80)
print(sum(after.values()))