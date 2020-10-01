import matplotlib.pyplot as plt

lines = []
line_styles = ['-', '-.', '--']
line_colors = ['red', 'blue', 'green']

# Data - with 3% test case
x = [3,4,5,6,7,8,9,10]
y_ovr_runtime =  [6372.42,1171.89,511.14,231.13,168.27,96.66,68.59,48.1]
y_gspan_runtime = [713,278.83,137.37,82.39,61.92,40.68,30.97,24.1]
y_filter_runtime = [5654.18,892.95,373.67,148.62,106.25,55.88,37.52,23.91]

# Data - without 3% test case
# x = [4,5,6,7,8,9,10]
# y_ovr_runtime =  [1171.89,511.14,231.13,168.27,96.66,68.59,48.1]
# y_gspan_runtime = [278.83,137.37,82.39,61.92,40.68,30.97,24.1]
# y_filter_runtime = [892.95,373.67,148.62,106.25,55.88,37.52,23.91]

line, = plt.plot(x, y_ovr_runtime, line_styles[0], color=line_colors[0])
lines.append(line)

line, = plt.plot(x, y_gspan_runtime, line_styles[1], color=line_colors[1])
lines.append(line)

line, = plt.plot(x, y_filter_runtime, line_styles[2], color=line_colors[2])
lines.append(line)

legend1 = plt.legend(lines, ['Overall Runtime', 'Gspan Runtime', 'Filter Runtime'], loc='upper right')
plt.gca().add_artist(legend1)

plt.xlabel("Percent of Database As Minimum Support")
plt.ylabel("Runtime of Naive Close Graph (sec)")
plt.title("Runtimes vs Minimum Support of Chemical Benchmark Dataset")
plt.show()