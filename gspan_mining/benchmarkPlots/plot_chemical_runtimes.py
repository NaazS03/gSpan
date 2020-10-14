import matplotlib.pyplot as plt

lines = []
line_styles = ['-', '-.', '--']
line_colors = ['red', 'blue', 'green']

# Data - with 3% test case
x = [3,4,5,6,7,8,9,10]
y_ovr_runtime =  [4578.7,1017.19,310.17,148.24,109.61,67.01,45.86,36.85]
y_gspan_runtime = [1155.84,289.2,141.96,76.46,59.47,40.47,30.03,25.48]
y_filter_runtime = [3422.76,727.9,168.11,71.69,50.03,26.45,15.74,11.28]

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