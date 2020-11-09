import numpy as np
import matplotlib.pyplot as plt

# NOTE: This code was adapted from: 
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py

labels = ["63k", "126k", "189k", "315k"]
cyac_mem = [48, 62, 77, 105]
pyahocorasick_mem = [66, 82, 96, 125]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, cyac_mem, width, label='cyac', color="red")
rects2 = ax.bar(x + width/2, pyahocorasick_mem, width, label='pyahocorasick', color="black")

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('AC automaton patterns')
ax.set_ylabel('Memory(MegaBytes)')
ax.set_title('Memory Consumption')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.savefig("memory_consumption_cyac_pyahocorasick.png")