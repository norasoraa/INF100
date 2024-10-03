# oppgave 4a
def cross_sum(n):
    x = 0
    while n > 0:
        # bakerste tall i n
        x += n % 10
        # fjerner det bakerste tallet i n
        n //= 10
    return x
print(cross_sum(11))

print("Tester cross_sum... ", end="")
assert(1 == cross_sum(1))
assert(3 == cross_sum(12))
assert(6 == cross_sum(123))
assert(10 == cross_sum(1234))
assert(10 == cross_sum(4321))
print("OK")


print()

# oppgave 4b
def nth_number_with_cross_sum_x(n, x):
    count = 0
    guess = -1
    while count < n:
        guess += 1
        if cross_sum(guess) == x:
            count += 1
    return guess
print(nth_number_with_cross_sum_x(2,7))

