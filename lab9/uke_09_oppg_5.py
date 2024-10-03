def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def collect_collatz(a, b):
    d = dict()
    for number in range(a, b):
        sequence = collatz_sequence(number)
        d[number] = sequence
    return d

print(collect_collatz(3, 6))
