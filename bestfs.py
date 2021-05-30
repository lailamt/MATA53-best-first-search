import networkx as nx
import matplotlib.pyplot as plt

# addedge vincula um vértice ao outro e guarda o valor de custo
def addedge(x, y, cost):
    grafo[x].append((y, cost))

    G.add_nodes_from([x,y])
    G.add_edge(x,y)

    edges.append((x,y))
# deve inserir os dados de (v_partida,v_chegada,custo_caminho)

# Ordena de acordo com o valor de custo da Tupla (y,custo)
def Sort_Tuple(tup): 
      
    # pega o tamanho da lista de tuplas
    lst = len(tup) 
    for i in range(0, lst): 
          
        for j in range(0, lst-i-1): 
            if (tup[j][1] > tup[j + 1][1]): 
                temp = tup[j] 
                tup[j]= tup[j + 1] 
                tup[j + 1]= temp 
    return tup 

    # recebe dois valores como parâmetro
# start = vértice_saída
# end = vértice_chegada
def best_first_search(start, end):
    visitado = []
    visitar = []
    total_custo = 0

    visitado.append(start)

    for x in grafo[start]:
        visitar.append(x)

    Sort_Tuple(visitar)
    visitado.append(visitar[0][0])

    while visitar[0][0] != end:
        total_custo += visitar[0][1]
        for x in grafo[visitar[0][0]]:
            visitar.append(x)
        visitar.pop(0)
        Sort_Tuple(visitar)
        visitado.append(visitar[0][0])

    total_custo+=visitar[0][1] 
    visitado.append(total_custo)
    return visitado

  # recebe uma tupla como parâmetro
# caminho = (vértice_saída, vértice_chegada)
def best_first_search2(caminho):
    visitado = []
    visitar = []
    total_custo = 0

    visitar.append((caminho[0],total_custo))
    #print(visitar)
  
    if visitar[0][0] == caminho[1]:
        #visitado.append(visitar[0][0])
        visitado.append(total_custo)
        print("O vértice de saída é igual ao vértice de entrada.")
    else:
        while visitar[0][0] != caminho[1]:
            visitado.append(visitar[0][0])
            total_custo += visitar[0][1]
            for x in grafo[visitar[0][0]]:
                visitar.append(x)
            visitar.pop(0)
            Sort_Tuple(visitar)

    visitado.append(visitar[0][0])
    total_custo+=visitar[0][1] 
    visitado.append(total_custo)
    return visitado

def calc_path_edges():
    path_edges=[]
    for x in range(len(caminho_do_grafo)):
        for y in range(len(edges)):
            if ((caminho_do_grafo[x] == edges[y][1]) and (edges[y][0] in caminho_do_grafo)):
                path_edges.append(edges[y])
    return path_edges

def draw_graph():
    pos = nx.spring_layout(G)

    path_edges = calc_path_edges()

    # Draw nodes and edges not included in path
    nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes)-set(caminho_do_grafo))
    nx.draw_networkx_edges(G, pos, edgelist=set(G.edges)-set(path_edges), connectionstyle='arc3, rad = 0.3')
    # Draw nodes and edges included in path
    nx.draw_networkx_nodes(G, pos, nodelist=caminho_do_grafo, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', connectionstyle='arc3, rad = 0.3')

    # Draw labels
    nx.draw_networkx_labels(G,pos)

    #plt.savefig("simple_path.png") # save as png
    plt.show() # display


def main():
    # v é a quantidade de vértices em G
    # DEVE SER INSERIDO
    #v = 14
    global G, v, grafo, caminho_do_grafo, custo_total, edges
    
    v = 14
    # grafo é uma lista de listas de tamanho v
    grafo = [[] for i in range(v)]

    G=nx.Graph()
    edges = []

    caminho_do_grafo = best_first_search(0, 9)
    custo_total = caminho_do_grafo.pop(-1)
    custo_total

    caminho_do_grafo

    draw_graph()

