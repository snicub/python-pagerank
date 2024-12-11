import numpy as np
import pandas as pd

#load graph from text to create adjency list
def load_graph(file_path):
    data = pd.read_csv(file_path, sep="\t", header=None, names=["source", "destination"])
    return data
#create transition matrix M from graph data
def construct_transition_matrix(graph, n):
    M = np.zeros((n, n))
    out_degree = np.zeros(n)

    for _, row in graph.iterrows():
        source, destination = row["source"] - 1, row["destination"] - 1
        M[destination, source] += 1
        out_degree[source] += 1

    for i in range(n):
        if out_degree[i] > 0:
            M[:, i] /= out_degree[i]

    return M

#computer pagerank vector by iterating
def compute_pagerank(M, beta, iterations, n):
    r = np.ones(n) / n
    teleport = (1 - beta) / n * np.ones(n)

    for _ in range(iterations):
        r = teleport + beta * np.dot(M, r)

    return r

#driver code 
def main():
    file_path = "graph.txt"
    n = 100  #number of nodes in the graph
    beta = 0.8  #damping factor
    iterations = 40  #number of iterations

    #load the graph
    graph = load_graph(file_path)

    #create the transition matrix
    M = construct_transition_matrix(graph, n)

    #compute the PageRank vector
    pagerank = compute_pagerank(M, beta, iterations, n)

    #get top 5 and bottom 5 nodes by PageRank score
    top_5 = np.argsort(pagerank)[-5:][::-1] + 1
    bottom_5 = np.argsort(pagerank)[:5] + 1

    print("Top 5 nodes with highest PageRank scores:", top_5)
    print("Bottom 5 nodes with lowest PageRank scores:", bottom_5)

if __name__ == "__main__":
    main()
