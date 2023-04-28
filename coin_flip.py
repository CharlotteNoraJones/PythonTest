import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    return np.random.choice([0,1], p=[1-p1, p1], size=10000)

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    occurrences = 0
    for i in range(len(seq) - 4):
        if seq[i] == 1:
            if 0 not in seq[i:i + 5]:
                occurrences += 1
    return occurrences

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
