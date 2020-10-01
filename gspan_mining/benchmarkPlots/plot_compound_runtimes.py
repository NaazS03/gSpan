import matplotlib.pyplot as plt

lines = []
line_styles = ['-', '-.', '--']
line_colors = ['red', 'blue', 'green']

# Data - with 3% test case
x = [7,8,9,10]
y_ovr_runtime =  [31503.94,4879.09,3364.68,2698.77]
y_gspan_runtime = [1144.42,400.75,349.33,313.91]
y_filter_runtime = [30359.39,4478.21,3015.07,2384.64]

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
plt.title("Runtimes vs Minimum Support of Compound Benchmark Dataset")
plt.show()