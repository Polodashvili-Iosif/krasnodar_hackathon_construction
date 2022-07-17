import matplotlib.pyplot as plt

# create data
size = [12, 11, 3, 30]

# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Give color names
plt.pie(
    size,
    labels=size,
    textprops={'fontsize': 20},
    wedgeprops={'linewidth': 4, 'edgecolor': 'white'}
)
p = plt.gcf()
p.gca().add_artist(my_circle)
p.gca()
# Show the graph
plt.show()
