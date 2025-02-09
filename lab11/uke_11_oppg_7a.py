import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

# endrer farge og stil på grafene
plt.plot(xs, ys_1, "*", color='violet')
plt.plot(xs, ys_2, ":", color='green')

# savefig lagrer filene
plt.savefig("test.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show() # Hva skjer om vi ikke har med den raden: plt.show()?