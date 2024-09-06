import networkx as nx
import time
from greedy_algorithm_l321 import Greedy_Algorithm_L321

# Função para criar o grafo a partir do arquivo.
def create_graph_from_file(filename, graph_is_0_indexed):
  G = nx.Graph()
  with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'c' or line[0] == 'p':
                continue
            if line[0] == 'e':
                line = line.rstrip()
                e = line.split(' ')
                u = int(e[1])
                v = int(e[2])
                if graph_is_0_indexed == False:
                    u = u - 1
                    v = v - 1
                G.add_edge(u,v)
  return G
  
# Função para executar o algoritmo genético e salvar os resultados em um arquivo.
def run_experiment(graph_name, graph, iterations, file_name):

  greedy_algorithm = Greedy_Algorithm_L321(graph)
  start_time = time.time()
  best_fitness = greedy_algorithm.run(iterations)
  end_time = time.time()
  execution_time = end_time - start_time

  with open(file_name, 'a') as file:  
      file.write(f"Grafo: {graph_name}\n")
      file.write(f"Melhor fitness: {best_fitness}\n")
      file.write(f"Tempo de execução: {execution_time:.4f} segundos\n")
      file.write("\n")

  print(f"Grafo: {graph_name}")
  print(f"Melhor fitness encontrado: {best_fitness}")
  print(f"Tempo de execução: {execution_time:.4f} segundos\n")

  return best_fitness, execution_time

# Função main.
# Instancia os grafos e chama a função run_experiment.
# Salva os resultados em um arquivo.
# Executa a função main.
def main():
  
  file_name = "result.txt"
  iterations = 100  
  
  # Grafos gerados pela biblioteca NetworkX
  graphs = [
        ("complete_graph(20)", nx.complete_graph(20)),
        ("complete_graph(70)", nx.complete_graph(70)),
        ("complete_bipartite_graph(20, 10)", nx.complete_bipartite_graph(20, 10)),
        ("complete_bipartite_graph(50, 50)", nx.complete_bipartite_graph(50, 50)),
        ("cycle_graph(10)", nx.cycle_graph(10)),
        ("cycle_graph(30)", nx.cycle_graph(30)),
        ("cycle_graph(50)", nx.cycle_graph(50)),
        ("path_graph(50)", nx.path_graph(50)),
        ("path_graph(70)", nx.path_graph(70)),
        ("path_graph(100)", nx.path_graph(100)),
        ("grid_2d_graph(10, 8)", nx.grid_2d_graph(10, 8)),
        ("grid_2d_graph(7, 6)", nx.grid_2d_graph(7, 6)),
        ("grid_2d_graph(3, 35)", nx.grid_2d_graph(3, 35)),
    ]
  
  # Executa o algoritmo genético para os grafos da biblioteca NetworkX
  for graph_name, graph in graphs:
    
    # Gerar um mapeamento de coordenadas (i, j) para inteiros
    mapping = {node: i for i, node in enumerate(graph.nodes())}

    # Renomeie os nós no gráfico usando o mapeamento
    graph = nx.relabel_nodes(graph, mapping)
    
    run_experiment(graph_name, graph, iterations, file_name)
  
  # Grafos gerados a partir dos arquivos.
  file_graphs = [
    ("Grafo do arquivo 1", create_graph_from_file("dsjc250.5.col", False)),
        ("Grafo do arquivo 2", create_graph_from_file("dsjc500.1.col", False)),
        ("Grafo do arquivo 3", create_graph_from_file("dsjc500.5.col", False)),
        ("Grafo do arquivo 4", create_graph_from_file("dsjc1000.1.col", False)),
    ]
  
  # Executa o algoritmo genético para os grafos dos arquivos
  for graph_name, graph in file_graphs:
    run_experiment(graph_name, graph, iterations, file_name)


# Executa a função main.
if __name__ == "__main__":
  main()