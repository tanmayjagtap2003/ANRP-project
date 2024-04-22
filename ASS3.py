INF = 999
def floydwarshall(graph):
    dist = list(map(lambda i: list(map(lambda j : j, i)), graph))

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min( dist[i][j], dist[i][k] + dist[k][j])
    printsolution(dist)

def printsolution(dist):
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("Infinite!!!!!")
            else: 
                print("%7d\t" % (dist[i][j]), end='')
            if j == V - 1:
                print()

if __name__ == "__main__":
    V = int(input('vertex'))
    graph = []
    for i in range(V):
        row = graph.append(list(map()))

    floydwarshall(graph)