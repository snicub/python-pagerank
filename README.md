# PageRank Algorithm Implementation in Python

This repository contains an implementation of the PageRank algorithm in Python. The algorithm calculates the PageRank scores of nodes in a graph, representing their relative importance. The input graph is loaded from a text file, and the results include the top 5 and bottom 5 nodes based on their PageRank scores.

## Features
- Load graph data from a text file.
- Construct a transition matrix based on the graph's adjacency list.
- Iteratively compute PageRank scores using the power iteration method.
- Output the top 5 and bottom 5 nodes based on PageRank scores.

## Requirements
- Python 3.7+
- NumPy
- Pandas

Install the required libraries using pip:
```bash
pip install numpy pandas
