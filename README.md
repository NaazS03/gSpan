# <div align = center>Enhanced gSpan/Naive CloseGraph</div>

**gSpan** is an algorithm for mining frequent subgraphs.

This program implements a enhanced gSpan also known as naive close graph with Python. The algorithm filters non-maximal subgraphs from the gSpan output. The repository on GitHub is  The repository on GitHub is [https://github.com/NaazS03/gSpan](https://github.com/NaazS03/gSpan). The naive close graph builds on top of the gSpan implementation found here: [https://github.com/betterenvi/gSpan](https://github.com/betterenvi/gSpan).

### Undirected Graphs
This program supports undirected graphs 

### How to install

This program supports both **Python 2** and **Python 3**.

##### Method 1

First, clone the project:

```sh
git clone https://github.com/NaazS03/gSpan.git
cd gSpan
```

### How to run

The command is:

```sh
python -m gspan_mining [-s min_support] [-n num_graph] [-l min_num_vertices] [-u max_num_vertices] [-d True/False] [-v True/False] [-p True/False] [-w True/False] [-h] database_file_name 
```


##### Some examples

- Read graph data from ./graphdata/graph.data, and mine undirected subgraphs given min support is 5000
```
python -m gspan_mining -s 5000 ./graphdata/graph.data
```

- Read graph data from ./graphdata/graph.data, mine undirected subgraphs given min support is 5000, and visualize these frequent subgraphs(matplotlib and networkx are required)
```
python -m gspan_mining -s 5000 -p True ./graphdata/graph.data
```

- Print help info
```
python -m gspan_mining -h
```

### Reference
- [gSpan Paper](http://www.cs.ucsb.edu/~xyan/papers/gSpan-short.pdf)

gSpan: Graph-Based Substructure Pattern Mining, by X. Yan and J. Han. 
Proc. 2002 of Int. Conf. on Data Mining (ICDM'02). 

- [CloseGraph Paper](https://sites.cs.ucsb.edu/~xyan/papers/CloseGraph.pdf)

Xifeng Yan. Jiawei Han. CloseGraph: Mining Closed Frequent Graph Patterns. Department of Computer Science, University of Illinois at Urbana-Champaign. 2003