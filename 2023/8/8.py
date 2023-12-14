with open("input.txt") as f:
    lines = [f.strip() for f in f.readlines()]

with open("subset.txt") as f:
    test_lines = [f.strip() for f in f.readlines()]


class navigation_loop:
    def __init__(self, navigation_instructions: str):
        self.instructions = navigation_instructions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current_instruction = self.instructions[self.index]

        if self.index + 1 > len(self.instructions) - 1:
            self.index = 0
        else:
            self.index += 1
        return current_instruction


test_instructions = test_lines[0]
for i in navigation_loop(test_instructions):
    print(i)
