import matplotlib.pyplot as plt

lines = []
line_styles = ['-', '--']
line_colors = ['red', 'blue']

x = [3,4,5,6,7,8,9,10]
y_num_total_graphs =  [18121,5935,3608,2121,1770,1224,977,844]
y_num_closed_graphs = [2704,1642,1177,813,689,552,481,401]

line, = plt.plot(x, y_num_total_graphs, line_styles[0], color=line_colors[0])
lines.append(line)

line, = plt.plot(x, y_num_closed_graphs, line_styles[1], color=line_colors[1])
lines.append(line)


legend1 = plt.legend(lines, ['Total graphs produced', 'Closed Graphs Produced'], loc='upper right')
plt.gca().add_artist(legend1)

plt.xlabel("Percent of Database As Minimum Support")
plt.ylabel("Number of Graphs Produced")
plt.title("Graphs Created vs Minimum Support of Chemical Benchmark Dataset")
plt.show()