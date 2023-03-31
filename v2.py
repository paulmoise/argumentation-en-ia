from collections import defaultdict
from itertools import chain
from graphviz import Digraph


class Graph:
    def __init__(self, Nodes):
        # default a value if that key has not set yet
        self.adj_list = defaultdict(list)
        self.nodes = Nodes

    def add_edge(self, v, e):
        self.adj_list[v].append(e)

    def print_adj(self):
        for node in self.nodes:
            print(node, ':', self.adj_list[node])

    def degree_vertex(self, node):
        degree = len(self.adj_list[node])
        return degree

    def is_cyclic_helper(self, v, visited, rec_stack):
        # mark current node as visited and add to recursion stack
        visited[v] = True
        rec_stack[v] = True

        # for all neighbours if any neighbour is visited in rec_stack the graph is cyclic
        for neighbour in self.adj_list[v]:
            if visited[neighbour] == False:
                if self.is_cyclic_helper(neighbour, visited, rec_stack) == True:
                    return True
            elif rec_stack[neighbour] == True:
                return True
        # the node needs to be popped from
        # recursion stack before function ends
        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = {node: False for node in self.nodes}
        rec_stack = {node: False for node in self.nodes}
        for node in self.nodes:
            if visited[node] == False:
                if self.is_cyclic_helper(node, visited, rec_stack) == True:
                    return True
        return False


def visualize_graph(args, relations):
    g = Digraph()
    for arg in args:
        g.node(arg, arg)

    edges = [x + y for x, y in relations]
    g.edges(edges)
    g.render('simple_graph', format='png', view=True)


def read_user_input():
    print('Veuillez entrer les arguments à tester séparer par des virgules:')
    inputs = input('> ')
    args = list(map(lambda x: x.strip(), inputs.split(',')))
    print("Veuillez saisir les relations d'attaque entre ces arguments séparer par des points virgules: ")
    print("Exemple:  (a,b); (b,c) signifie 'a' attaque 'b' et 'b' attaque 'c': ")
    inputs = input('> ')
    relations = list(map(lambda x: tuple(x.strip().lstrip('(').rstrip(')').split(',')), inputs.split(';')))
    relations = [(x.strip(), y.strip()) for x, y in relations]
    print('arguments: ', args)
    print("relations d'attaque :", relations)

    return args, relations


def build_arguments_graph(args, relations):
    graph = Graph(args)
    for v, e in relations:
        if v in args and e in args:
            graph.add_edge(v, e)
        else:
            # Throw an exception and ask if user want to add this argument to the list of existing argument
            print(
                f'Un arguments ne fait pas partir de la liste des arguments !: ({v}, {e}) not in {graph.nodes}X{graph.nodes}')

    return graph


def is_defeated_by_chosen_args(current_arg, selected_arg, graph):
    for arg in selected_arg:
        if current_arg in graph.adj_list[arg]:
            return True
    return False


def grounded_semantic(graph: Graph):
    admissible_args = []
    # get all arguments which where not attacked
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # print(defeated_args)
    admissible_args = set(graph.nodes).difference(defeated_args)
    not_admissible_args = set()
    for node in graph.nodes:
        if node not in admissible_args:
            if is_defeated_by_chosen_args(node, admissible_args, graph):
                not_admissible_args.add(node)
            else:
                admissible_args.add(node)
    # print("admissible arguments: ", admissible_args)
    # print("defeated arguments: ", not_admissible_args)
    return admissible_args


if __name__ == '__main__':

    # args, relations = read_user_input()
    args = ['a', 'b', 'c', 'd', 'e']
    relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    graph = build_arguments_graph(args, relations)
    graph.print_adj()
    grounded_semantic(graph)
    visualize_graph(args, relations)
    if graph.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")

# (a,b); (b,c); (c, a); (c,d); (d,e)
# edges = [("A", "B"), ("B", "C"), ("C", "A"), ("B", "D"),
#          ("B", "E"), ("C", "D"), ("D", "E")]
# nodes = ["A", "B", "C", "D", "E"]
# graph = Graph(nodes)
# for v, e in edges:
#     graph.add_edge(v, e)
# graph.print_adj()
# print(graph.degree_vertex("B"))
#
# if graph.is_cyclic() == 1:
#     print("Graph contains cycle")
# else:
#     print("Graph doesn't contain cycle")
