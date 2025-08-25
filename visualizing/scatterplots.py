# from matplotlib import pyplot as plt

# friends = [70, 65, 72, 63]
# minutes = [175, 170, 205, 220]
# labels  = ['a', 'b', 'c', 'd']

# plt.scatter(friends, minutes)

# for label, friends_count, minute_count in zip(labels, friends, minutes):
#     plt.annotate(
#         label,
#         xy=(friends_count, minute_count),
#         xytext=(5, -5),
#         textcoords='offset'
#     )

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
