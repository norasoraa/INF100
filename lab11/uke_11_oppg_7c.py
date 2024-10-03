import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# legger til minor ticks til x- og y-aksen
plt.minorticks_on()

# legger til første interseksjon-punktet etter (0,0)
x = [3.15]
y = [0]
plt.plot(x, y, marker="o", markersize=5, color='black')

# legger til pil til punktet
x1, y1 = [3.15, 4.75], [0, 2]
plt.plot(x1, y1, color='black')

# legger til tekst
plt.text(3, 2.2, 'Første interseksjonen', fontweight='bold')

# savefig lagrer filene
plt.savefig("test.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show() # Hva skjer om vi ikke har med den raden: plt.show()?