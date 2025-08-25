from matplotlib import pyplot as plt

# years    = [2010, 2020, 2030, 2040, 2050]
# students = [1000, 1300, 2300, 3000, 1200]

# plt.bar(years, students)

# plt.title("Yillar bo'yicha talaba bo'lgan abiturentlar")

# plt.ylabel("talabalar soni")
# plt.xlabel("yillar")

# plt.show()

year      = [2010, 2020, 2030]
downloads = [230, 22, 123]
average = [(x + y) / y for x, y in zip(year, downloads)]

plt.plot(year, downloads, 'r-.', label='year+downloads')

plt.show()
