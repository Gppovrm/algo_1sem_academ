cands = {}
with open('input.txt', 'r') as input_file:
    for line in input_file:
        name, votes = line.split()
        votes = int(votes)
        if name in cands:
            cands[name] += votes
        else:
            cands[name] = votes
sorted_cands = sorted(cands.items())
with open('output.txt', 'w') as output_file:
    for name, votes in sorted_cands:
        output_file.write(f"{name} {votes}\n")
