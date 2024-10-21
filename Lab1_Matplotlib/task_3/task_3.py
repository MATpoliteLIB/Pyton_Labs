import csv
import matplotlib.pyplot as plt
import numpy as np

data = []
label = []

with open('students.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        a=str(*row).split(";")
        name=a[0]
        group=int(a[1])
        grade=int(a[2])
        strok=[name,group,grade]
        data.append(strok)

# Sorted by preps
data=sorted(data, key = lambda e: e[1])
ded=data[0][1]
label.append(ded)
for i in data:
    if (ded!=i[1]):
        ded=i[1]
        label.append(ded)

grades=[3,4,5,6,7,8,9,10]
quantity=[0]*len(label)
for i in range (len(label)):
    quantity[i]=[0]*len(grades)

k=0
ded=data[0][1]
for i in data:
    if (i[1]==ded):
        quantity[k][i[2]-3]+=1
    else:
        ded=i[1]
        k+=1
        quantity[k][i[2]-3]+=1

category_names = list(map(str,grades))
results = {}

i=0
for m in label:
    results[str(m)]=quantity[i]
    i+=1

def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0, 1, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if c > 0:  # Добавляем условие, чтобы не выводить 0
                ax.text(x, y, str(int(c)), ha='center', va='center',
                        color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax


survey(results, category_names)
plt.title('Оценки групп',pad=30)
plt.savefig("task3_plot2.png")
plt.show()

