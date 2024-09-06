import networkx as nx
import random

# Algoritmo guloso para rotulação L321.
# Geração do cromossomo por permutação.
class Greedy_Algorithm_L321:
  def __init__(self, graph):
    self.G = graph
    self.dict1 = self.neighbors_at_distance_1()
    self.dict2 = self.neighbors_at_distance_2()
    self.dict3 = self.neighbors_at_distance_3()

  def run(self, iterations):
    
    max_color_values = []
    
    for i in range(iterations):

      permutation = [x for x in range(0,len(self.G))]
      random.shuffle(permutation)
      max_color = self.greedy_coloring_L321(permutation, self.dict1, self.dict2, self.dict3)
      max_color_values.append(max_color)

    min_max_color = min(max_color_values)

    return min_max_color


  def condition_satisfied(self, neighbors_dict, vertex, color_list, value, newcolor):
      for w in neighbors_dict[vertex]:
          if abs(newcolor - color_list[w]) < value:
              return False
      return True

  def greedy_coloring_L321(self, vertex_permutation, neighbors1, neighbors2, neighbors3):
      color_list = [-1] * len(vertex_permutation)
      for v in vertex_permutation:
          color = 0
          while True:
              if self.condition_satisfied(neighbors1, v, color_list, 3, color) and \
                  self.condition_satisfied(neighbors2, v, color_list, 2, color) and \
                  self.condition_satisfied(neighbors3, v, color_list, 1, color):
                color_list[v] = color
                break
              else:
                  color += 1
      return max(color_list)


  # retorna um dicionário contendo os vizinhos na distância 1
  # para cada vértice
  def neighbors_at_distance_1(self):
      dict1 = dict()
      for v in self.G:
          dict1[v] = []
          for u in self.G[v]:
              dict1[v].append(u)
      return dict1


  # retorna um dicionário contendo os vizinhos na distância 2
  # para cada vértice
  def neighbors_at_distance_2(self):
      dict2 = dict()
      for v in self.G:
          dict2[v] = []
          for u in self.G[v]:
              for w in self.G[u]:
                  if w != v and w not in self.dict1[v]:
                      dict2[v].append(w)
      return dict2


  # retorna um dicionário contendo os vizinhos na distância 3
  # para cada vértice
  def neighbors_at_distance_3(self):
      dict3 = dict()
      for v in self.G:
          dict3[v] = []
          for u in self.G[v]:
              for w in self.G[u]:
                  for z in self.G[w]:
                      if z != u and z != v and z not in self.dict2[v] and z not in self.dict1[v]:
                          dict3[v].append(z)
      return dict3