import matplotlib.pyplot as plt

lines = []
line_styles = ['-', '--']
line_colors = ['red', 'blue']

x = [7,8,9,10]
y_num_total_graphs =  [62092,24402,17355,15832]
y_num_closed_graphs = [1195,995,827,723]

line, = plt.plot(x, y_num_total_graphs, line_styles[0], color=line_colors[0])
lines.append(line)

line, = plt.plot(x, y_num_closed_graphs, line_styles[1], color=line_colors[1])
lines.append(line)


legend1 = plt.legend(lines, ['Total graphs produced', 'Closed Graphs Produced'], loc='upper right')
plt.gca().add_artist(legend1)

plt.xlabel("Percent of Database As Minimum Support")
plt.ylabel("Number of Graphs Produced")
plt.title("Graphs Created vs Minimum Support of Compound Benchmark Dataset")
plt.show()