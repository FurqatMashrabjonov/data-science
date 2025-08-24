from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 2000, 2010]
gdp   = [300, 543.3, 1075, 2322, 12044]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")

plt.title("my line chart")

plt.ylabel("Billions of $")

plt.show()
