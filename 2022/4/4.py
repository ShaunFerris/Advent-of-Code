with open('input.txt') as f:
    data = f.readlines()

def get_sequence(elf):
    sections = list(map(int, elf.split('-')))
    return list(range(sections[0], sections[1] + 1))

def is_subsequence(seqA, seqB):
    if len(seqA) < len(seqB):
        seqA, seqB = seqB, seqA
    seqA, seqB = set(seqA), set(seqB)
    if seqA.intersection(seqB) == seqB:
        return True
    else:
        return False

def count_full_overlaps(elf_assignments):
    count = 0
    for pair in elf_assignments:
        elf1, elf2 = pair.split(',')[0], pair.split(',')[1]
        seq1, seq2, = get_sequence(elf1), get_sequence(elf2)
        if is_subsequence(seq1, seq2):
            count += 1
    return count

print(count_full_overlaps(data))

#Problem part 2

def count_inclusions(elf_assignments):
    count = 0
    for pair in elf_assignments:
        elf1, elf2 = pair.split(',')[0], pair.split(',')[1]
        seq1, seq2, = get_sequence(elf1), get_sequence(elf2)
        for area in seq1:
            if area in seq2:
                count += 1
                break
    return count

print(count_inclusions(data))