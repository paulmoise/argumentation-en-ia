from collections import defaultdict, OrderedDict
from copy import deepcopy
from itertools import chain
import random

from graphviz import Digraph
from graphviz import Graph as GraphViz


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
            if not visited[node]:
                if self.is_cyclic_helper(node, visited, rec_stack):
                    return True
        return False

    def find_cycles(self):
        cycles = []
        visited = set()

        def dfs(node, path):
            if node in visited:
                if node in path:
                    cycle_start = path.index(node)
                    cycle = path[cycle_start:]
                    cycles.append(cycle)
                return
            visited.add(node)
            path.append(node)
            for neighbor in self.adj_list[node]:
                dfs(neighbor, path)
            path.pop()

        nodes = list(self.adj_list.keys())
        for node in nodes:
            dfs(node, [])
        return cycles


def visualize_graph(args, relations, solution):
    g = Digraph(graph_attr={'rankdir': 'LR'})
    for arg in args:
        if arg in solution:
            g.node(arg, arg, style="filled", fillcolor='#ff000042')
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
    print('Les arguments: ', args)
    print("Les relations d'attaque :", relations)

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


def solve_simple_chain_args(graph: Graph):
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


def find_admissible_args_simple_chained_args(graph: Graph):
    # Get all arguments defeated by at least one argument
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # Get all initial not attacked arguments
    initial_not_attacked_args = set(graph.nodes).difference(defeated_args)
    admissible_args = set()
    for curr_arg in initial_not_attacked_args:
        visited = {curr_arg: None}  # mark this element as not visited
        admissible_args.add(curr_arg)
        not_admissible_args = set()
        Q = [curr_arg]
        while Q:
            u = Q.pop(0)
            for v in graph.adj_list[u]:
                if v in visited:
                    continue
                visited[v] = u
                Q.append(v)

                if u in admissible_args:
                    not_admissible_args.add(v)
                else:
                    admissible_args.add(v)
                # print(v)
        # print("visited", visited)
        # print("admissible args", admissible_args)
        # print("not_admissible args", not_admissible_args)
    return admissible_args


def find_admissible_args_simple_chained_argsV2(graph: Graph):
    # Get all arguments defeated by at least one argument
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # Get all initial not attacked arguments
    initial_not_attacked_args = set(graph.nodes).difference(defeated_args)
    # if any element can help to solve the cycle (not attacked)
    admissible_args = set()
    possible_axes_solutions = []
    for curr_arg in initial_not_attacked_args:
        visited = OrderedDict()  # mark this element as chose
        visited[curr_arg] = 'IN'
        Q = [curr_arg]
        while Q:
            u = Q.pop(0)
            for v in graph.adj_list[u]:
                if v in visited:
                    continue
                visited[v] = 'OUT' if visited[u] == 'IN' else 'IN'
                Q.append(v)
        # print(f'current = {curr_arg}, label ={visited}')
        possible_axes_solutions.append(visited)
    # find possible conflict indice in order to know where to start correction
    conflictual_nodes = get_conflict_nodes(graph.nodes, possible_axes_solutions)
    # print(conflictual_nodes)
    if len(conflictual_nodes) == 0:
        return get_solution(possible_axes_solutions)
    while len(conflictual_nodes) >= 1:
        if len(conflictual_nodes) == 1:
            for s in possible_axes_solutions:
                k = conflictual_nodes[0]
                v = s.get(k, None)
                if v is not None and v == 'IN':
                    s[k] = 'OUT'
            break
        else:
            start_node = conflictual_nodes[0]
            possible_axes_solutions = remove_conflict_nodes(conflictual_nodes, possible_axes_solutions)
            conflictual_nodes.pop(0)
            possible_axes_solutions = resolve_conflict(start_node, graph, possible_axes_solutions)
            # print('possible_axes_solutions ', possible_axes_solutions)
            conflictual_nodes = get_conflict_nodes(graph.nodes, possible_axes_solutions)
            # print('conflictual_nodes', conflictual_nodes)
    # print(possible_axes_solutions)
    return get_solution(possible_axes_solutions)


def get_solution(possible_axes_solutions):
    solutions = set()
    for s in possible_axes_solutions:
        for k, v in s.items():
            if v == 'IN':
                solutions.add(k)
    return solutions


def get_one_solution(labelled_args):
    solutions = set()
    for k, v in labelled_args.items():
        if v == 'IN':
            solutions.add(k)
    return solutions


def remove_conflict_nodes(nodes, possibles_axes_solutions):
    update = []
    for s in possibles_axes_solutions:
        if set(nodes).issubset(set(s.keys())):
            for node in nodes[1:]:
                del s[node]
        update.append(s)
    return update


def resolve_conflict(node, graph, possibles_axes_solutions):
    for s in possibles_axes_solutions:
        x = s.get(node, None)
        if x is not None:
            s[node] = 'OUT'
            to_visit = [node]
            while to_visit:
                u = to_visit.pop(0)
                for v in graph.adj_list[u]:
                    if v in s:
                        continue
                    s[v] = 'OUT' if s[u] == 'IN' else 'IN'
                    to_visit.append(v)
    return possibles_axes_solutions


def get_conflict_nodes(nodes, possible_axes_solutions):
    conflictual_nodes = []
    for node in nodes:
        labels = []
        for s in possible_axes_solutions:
            label = s.get(node, None)
            if label is not None:
                labels.append(label)
        if len(labels) > 1 and not all(x == labels[0] for x in labels):
            conflictual_nodes.append(node)
    return conflictual_nodes


def is_defeated_by_one_args(current_arg, cycle, graph):
    # check if element is at least by one args
    for arg in cycle:
        if current_arg in graph.adj_list[arg]:
            return True
    return False


def grounded_admissible_args_cycle_args(graph: Graph):
    # Get all arguments defeated by at least one argument
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # Get all initial not attacked arguments
    initial_not_attacked_args = set(graph.nodes).difference(defeated_args)
    # if any element can help to solve the cycle (not attacked)
    if len(initial_not_attacked_args) == 0:
        return set()

    if len(initial_not_attacked_args) == 1:
        curr_arg = initial_not_attacked_args.pop()
        labelled_args = labelled_args_from_unattacked_args(curr_arg, graph)
        admissible_args = {k: v for k, v in labelled_args.items() if v == 'IN'}
        return set(admissible_args.keys())
    else:
        possible_axes_solutions = [labelled_args_from_unattacked_args(arg, graph) for arg in initial_not_attacked_args]
        admissible_args = set()
        cycles = graph.find_cycles()
        max_length_index = max(range(len(possible_axes_solutions)), key=lambda i: len(possible_axes_solutions[i]))
        s1 = possible_axes_solutions[max_length_index]
        s2 = possible_axes_solutions[1] if max_length_index == 0 else possible_axes_solutions[0]
        s1_items = list(s1.items())
        s2_items = list(s2.items())
        s2_keys = list(s2.keys())
        for i in range(len(s1_items)):
            k, v = s1_items[i]
            x = s2.get(k, None)
            if x is None and not is_arg_belong_to_cycle(v, cycles):
                admissible_args.add(v)
            if x is not None:
                # print(x, v)
                if (v == 'IN' and x == 'OUT') or (v == 'OUT' and x == 'IN'):
                    if is_arg_belong_to_cycle(k, cycles):
                        prev_s1_k, prev_s1_v = s1_items[i - 1]
                        j = s2_keys.index(k)
                        prev_s2_k, prev_s2_v = s2_items[j - 1]
                        if (prev_s1_v == 'IN' and not is_arg_belong_to_cycle(prev_s1_k, cycles)) \
                                and is_arg_belong_to_cycle(prev_s2_k, cycles):
                            s1[k] = 'OUT'
                            s2[k] = 'OUT'
                        elif prev_s2_v == 'IN' and not is_arg_belong_to_cycle(prev_s2_k, cycles) \
                                and is_arg_belong_to_cycle(prev_s1_k, cycles):
                            s1[k] = 'OUT'
                            s2[k] = 'OUT'
                    else:
                        s1[k] = 'OUT'
                        s2[k] = 'OUT'
                elif x == 'UNDEC' and v != 'UNDEC':
                    s1[k] = v
                elif x != 'UNDEC' and v == 'UNDEC':
                    prev_s1_k, prev_s1_v = s1_items[i - 1]
                    j = s2_keys.index(k)
                    prev_s2_k, prev_s2_v = s2_items[j - 1]
                    if is_arg_belong_to_cycle(prev_s2_k, cycles) and prev_s2_v == 'OUT':
                        s1[k] = 'OUT'
                        s2[k] = 'OUT'
                    else:
                        s1[k] = v
        solutions = get_solution([s1, s2])
        return solutions



def preferred_semantic_admissible_args(graph: Graph):
    # Get all arguments defeated by at least one argument
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # Get all initial not attacked arguments
    initial_not_attacked_args = set(graph.nodes).difference(defeated_args)
    # if any element can help to solve the cycle (not attacked)
    possible_set_solutions = []
    labels = ['IN', 'OUT', 'UNDEC']

    if len(initial_not_attacked_args) == 0:
        cycles = graph.find_cycles()

        if len(cycles) == 1:
            # there is one cycle in the argumentation graph
            cycle = cycles[0]
            if len(cycle) % 2 != 0:
                # if the cycle is odd
                return [{}]
            else:
                # if the cycle is even
                solutions = []
                start_point = cycle[0]
                for label in ['IN', 'OUT']:
                    case_solution = treat_one_case(OrderedDict(), start_point, label, graph)
                    solutions.append(get_one_solution(case_solution))
                return solutions
        elif len(cycles) == 2:
            start_points = find_start_point(graph)
            if len(start_points) == 1:
                # be sure that the second cycle of the graph is at the end of the graph
                # print(start_points)
                key_point, cycle, start_point = start_points[0]
                if len(cycle) % 2 != 0:
                    second_cyle = None
                    for c in cycles:
                        if key_point not in c:
                            second_cyle = c
                    solution = set()
                    for arg in second_cyle:
                        if len(get_defeated_by(arg, graph)) == 1 and len(graph.adj_list[arg]) == 1:
                            solution.add(arg)
                    return [solution]
                else:
                    labelled_args = OrderedDict()
                    label = 'IN'
                    res1 = treat_one_case_with_cycle_at_end(labelled_args, start_point, label, graph)
                    res2 = treat_one_case_with_cycle_at_end(labelled_args, start_point, 'OUT', graph)
                    s1 = [get_one_solution(r) for r in res1]
                    s2 = [get_one_solution(r) for r in res2]
                    s = s1
                    for sol in s2:
                        if sol not in s:
                            s.append(sol)
                    return s

            elif len(start_points) == 2:
                key, cycle, start_point = get_key_start_point_from_cycle(start_points, graph)
                labelled_args = OrderedDict()
                label = 'IN'
                res1 = treat_one_case_with_cycle_at_end(labelled_args, start_point, label, graph)
                res2 = treat_one_case_with_cycle_at_end(labelled_args, start_point, 'OUT', graph)
                s1 = [get_one_solution(r) for r in res1]
                s2 = [get_one_solution(r) for r in res2]
                s = s1
                for sol in s2:
                    if sol not in s:
                        s.append(sol)
                return s
    elif len(initial_not_attacked_args) == 1:
        cycles = graph.find_cycles()
        if len(cycles) == 1:
            # if cycle is even (pair)

            start_point = initial_not_attacked_args.pop()
            res = treat_one_case_with_cycle_at_end(OrderedDict(), start_point, 'IN', graph)
            if len(res) == 1:
                return get_one_solution(res[0])
            else:
                s = [get_one_solution(r) for r in res]
                return s


def completed_semantic_admissible_args(graph: Graph):
    # Get all arguments defeated by at least one argument
    defeated_args = set(chain.from_iterable([v for k, v in graph.adj_list.items()]))
    # Get all initial not attacked arguments
    initial_not_attacked_args = set(graph.nodes).difference(defeated_args)
    # if any element can help to solve the cycle (not attacked)
    possible_set_solutions = []
    labels = ['IN', 'OUT', 'UNDEC']

    if len(initial_not_attacked_args) == 0:
        cycles = graph.find_cycles()

        if len(cycles) == 1:
            # there is one cycle in the argumentation graph
            cycle = cycles[0]
            if len(cycle) % 2 != 0:
                # if the cycle is odd
                return [{}]
            else:
                # if the cycle is even
                solutions = []
                start_point = cycle[0]
                for label in ['IN', 'OUT']:
                    case_solution = treat_one_case(OrderedDict(), start_point, label, graph)
                    solutions.append(get_one_solution(case_solution))
                solutions.append({})
                return solutions
        elif len(cycles) == 2:
            start_points = find_start_point(graph)
            if len(start_points) == 1:
                # be sure that the second cycle of the graph is at the end of the graph
                key_point, cycle, start_point = start_points[0]
                if len(cycle) % 2 != 0:
                    second_cyle = None
                    for c in cycles:
                        if key_point not in c:
                            second_cyle = c
                    solution = set()
                    for arg in second_cyle:
                        if len(get_defeated_by(arg, graph)) == 1 and len(graph.adj_list[arg]) == 1:
                            solution.add(arg)
                    s = [solution, {}]
                    return s
                else:
                    labelled_args = OrderedDict()
                    label = 'IN'
                    res1 = treat_one_case_with_cycle_at_end(labelled_args, start_point, label, graph)
                    res2 = treat_one_case_with_cycle_at_end(labelled_args, start_point, 'OUT', graph)
                    s1 = [get_one_solution(r) for r in res1]
                    s2 = [get_one_solution(r) for r in res2]
                    s = s1
                    for sol in s2:
                        if sol not in s:
                            s.append(sol)
                    s.append({})
                    return s

            elif len(start_points) == 2:
                key, cycle, start_point = get_key_start_point_from_cycle(start_points, graph)
                labelled_args = OrderedDict()
                label = 'IN'
                res1 = treat_one_case_with_cycle_at_end(labelled_args, start_point, label, graph)
                res2 = treat_one_case_with_cycle_at_end(labelled_args, start_point, 'OUT', graph)
                s1 = [get_one_solution(r) for r in res1]
                s2 = [get_one_solution(r) for r in res2]
                s = s1
                for sol in s2:
                    if sol not in s:
                        s.append(sol)
                s.append({})
                return s
    elif len(initial_not_attacked_args) == 1:
        cycles = graph.find_cycles()
        if len(cycles) == 1:
            # if cycle is even (pair)

            start_point = initial_not_attacked_args.pop()
            res = treat_one_case_with_cycle_at_end(OrderedDict(), start_point, 'IN', graph)
            if len(res) == 1:
                return [get_one_solution(res[0])]
            else:
                s = [get_one_solution(r) for r in res]
                return s


def get_key_start_point_from_cycle(start_points, graph):
    for point in start_points:
        key, cycle, _ = point
        r = [set(get_defeated_by(arg, graph)).issubset(set(cycle)) for arg in cycle]
        if all(r):
            return point
    return None


# start_points = find_start_point(graph)
# print(start_points)
# if len(start_points) == 1:
#     points = start_points[0]
#     labelled_args = OrderedDict()
#     for point in points:
#         for label in ['IN', 'OUT']:
#             case_solution = treat_one_case(labelled_args, point, label, graph)
#             print("case_solution = ", case_solution)
#             possible_set_solutions.append(get_one_solution(case_solution))

# print('solutions', possible_set_solutions)
# if len(initial_not_attacked_args) == 0:
#     start_points = find_start_point(graph)
#     print(start_points)
#     labelled_args = OrderedDict()
#     start = start_points.pop()
#     print(treat_one_case(labelled_args, start, 'IN', graph))
#     print(treat_one_case(labelled_args, start, 'OUT', graph))


def is_second_cycle_inside_graph(graph):
    for node in graph.nodes:
        if len(graph.adj_list[node]) == 0:
            return True
    return False


def treat_one_case_in_undec(labelled_args, curr_arg, to_visit, second_undec_label, graph):
    # print(labelled_args, to_visit, curr_arg, 7777777777777777)
    labelled_args_copy = deepcopy(labelled_args)
    labelled_args_copy[curr_arg] = second_undec_label
    # print("labelled_copy after = ", labelled_args_copy)
    to_visited = deepcopy(to_visit)
    to_visited.append(curr_arg)

    while to_visited:
        u = to_visited.pop(0)
        for v in graph.adj_list[u]:
            if v not in labelled_args_copy:
                labelled_args_copy[v] = 'OUT' if labelled_args_copy[u] == 'IN' else 'IN'
                to_visited.append(v)
    # print(labelled_args_copy, 21212121)
    return labelled_args_copy


def treat_one_case(labelled_args, curr_arg, label, graph):
    labelled_args_copy = deepcopy(labelled_args)
    labelled_args_copy[curr_arg] = label
    to_visited = [curr_arg]

    while to_visited:
        u = to_visited.pop(0)
        for v in graph.adj_list[u]:
            if v not in labelled_args_copy:
                labelled_args_copy[v] = 'OUT' if labelled_args_copy[u] == 'IN' else 'IN'
                to_visited.append(v)
    return labelled_args_copy


def treat_one_case_with_cycle_at_end(labelled_args, curr_arg, first_undec_label, graph):
    labelled_args_copy = deepcopy(labelled_args)
    labelled_args_copy[curr_arg] = first_undec_label
    to_visited = [curr_arg]
    cycles = graph.find_cycles()
    while to_visited:
        prev = to_visited.pop(0)
        for curr in graph.adj_list[prev]:
            if curr not in labelled_args_copy:
                if labelled_args_copy[prev] == 'OUT' and is_arg_belong_to_cycle(curr, cycles) \
                        and not is_args_belong_to_same_cycle(prev, curr, cycles):
                    # print(f'{prev}, {curr}, {is_args_belong_to_same_cycle(prev, curr, cycles)}')
                    cycle = get_argument_cycle_belong_to(curr, cycles)
                    if len(cycle) % 2 == 0:
                        res1 = treat_one_case_in_undec(labelled_args_copy, curr, to_visited, "IN",
                                                       graph)
                        res2 = treat_one_case_in_undec(labelled_args_copy, curr, to_visited, 'OUT',
                                                       graph)
                        res = [res1, res2]
                        # print(res)
                        return res
                    else:
                        return [labelled_args_copy]
                elif labelled_args_copy[prev] == 'OUT' and is_arg_belong_to_cycle(curr,
                                                                                  cycles) and is_args_belong_to_same_cycle(
                    prev, curr, cycles):
                    labelled_args_copy[curr] = 'IN'
                elif labelled_args_copy[prev] == 'OUT':
                    labelled_args_copy[curr] = 'IN'
                elif labelled_args_copy[prev] == 'IN':
                    labelled_args_copy[curr] = 'OUT'
                to_visited.append(curr)
    # print(labelled_args_copy)
    return [labelled_args_copy]

    # if not is_arg_belong_to_cycle(prev, cycles):
    #     prev_label = labelled_args_copy[prev]
    #     if len(prev_label) == 1:
    #         if prev_label[0] == 'IN':
    #             labelled_args_copy[curr] = ['OUT']
    #         else:
    #             labelled_args_copy[curr] = ['IN']
    #     elif len(prev_label) == 2:
    #         if prev_label[0] == 'IN':
    #             labelled_args_copy[curr] = ['OUT', 'OUT']
    #         else:
    #             labelled_args_copy[curr] = ['IN', 'IN']
    # else:
    #     prev_label = labelled_args_copy[prev]
    #     if len(prev_label) == 1:
    #         if prev_label[0] == 'IN':
    #             labelled_args_copy[curr] = ['OUT']
    #         else:
    #             labelled_args_copy[curr] = ['IN']
    #     elif len(prev_label) == 2:
    #         if prev_label[0] == 'IN':
    #             labelled_args_copy[curr] = ['OUT', 'OUT']
    #         else:
    #             labelled_args_copy[curr] = ['IN', 'IN']
    # to_visited.append(curr)


def get_argument_cycle_belong_to(arg, cycles):
    for c in cycles:
        if arg in c:
            return c
    return None


def is_args_belong_to_same_cycle(arg1, arg2, cycles):
    for cycle in cycles:
        if arg1 in cycle and arg2 in cycle:
            return True
    return False


def find_start_point(graph):
    start_points = []
    key_points = []
    cycles = graph.find_cycles()
    # print("cycles = ", cycles)
    for arg in graph.nodes:
        if is_arg_belong_to_cycle(arg, cycles):
            if len(graph.adj_list[arg]) == 2 and len(get_defeated_by(arg, graph)) == 1:
                key_points.append(arg)

    for point in key_points:
        for cycle in cycles:
            if point in cycle:
                key = random.choice(cycle)
                while key == point:
                    key = random.choice(cycle)
                start_points.append([point, cycle, key])
    return start_points


def get_defeated_by(curr_arg, graph):
    defeated_by = set()
    for arg in graph.nodes:
        if arg != curr_arg:
            if curr_arg in graph.adj_list[arg]:
                defeated_by.add(arg)
    return defeated_by


def labelled_args_from_unattacked_args(arg, graph):
    cycles = graph.find_cycles()
    labelled_args = OrderedDict()
    labelled_args[arg] = 'IN'
    to_visit = [arg]
    while to_visit:
        u = to_visit.pop(0)
        for v in graph.adj_list[u]:
            if v not in labelled_args:
                if labelled_args[u] == 'IN':
                    labelled_args[v] = 'OUT'
                if labelled_args[u] == 'OUT':
                    if not is_arg_belong_to_cycle(u, cycles) and is_arg_belong_to_cycle(v, cycles):
                        labelled_args[v] = 'UNDEC'
                    else:
                        labelled_args[v] = 'IN'
                if labelled_args[u] == 'UNDEC':
                    labelled_args[v] = 'UNDEC'
                to_visit.append(v)

    return labelled_args


def is_arg_belong_to_cycle(arg, cycles):
    for cycle in cycles:
        if arg in cycle:
            return True
    return False
    # if len(initial_not_attacked_args) == 0:
    #     # manage basic cycle
    #     cycles = graph.find_cycles()
    #     print("cycles", cycles)
    #     args_size = len(graph.adj_list)
    #     # if all args in contained in the union of all cycles
    #     flatten_cycles_args = [arg for sub_args in cycles for arg in sub_args]
    #     if set(graph.nodes) == set(flatten_cycles_args):
    #         return set()
    #     # size of three with cycle
    #     if args_size == 3:
    #         if len(cycles) == 1:
    #             c = cycles[0]
    #             rest = set(args).intersection(c)
    #             if is_defeated_by_chosen_args(rest.pop(), c, graph):
    #                 return set()
    #
    # for curr_arg in initial_not_attacked_args:
    #     visited = OrderedDict()  # mark this element as chose
    #     visited[curr_arg] = 'IN'
    #     Q = [curr_arg]
    #     while Q:
    #         u = Q.pop(0)
    #         for v in graph.adj_list[u]:
    #             if v in visited:
    #                 continue
    #             visited[v] = 'OUT' if visited[u] == 'IN' else 'IN'
    #             Q.append(v)
    #     admissible_args = {k: v for k, v in visited.items() if v == 'IN'}
    #     print(f'current = {curr_arg}, label ={visited}')
    #     return set(admissible_args.keys())


def bfs(G, S):
    color = dict()
    for x in G:
        color[x] = 'W'
    P = dict()
    P[S] = None
    color[S] = 'G'
    Q = [S]
    while Q:
        u = Q[0]
        for v in G[u]:
            if color[v] == 'W':
                P[v] = u
                color[v] = 'G'
                Q.append(v)
                # print(v)
        Q.pop(0)
        color[u] = 'B'
    return P



def visualize_single_graph(args, relations, solution):
    g = GraphViz(graph_attr={'rankdir': 'LR'})
    for arg in args:
        if arg in solution:
            g.node(arg, arg, style="filled", fillcolor='#ff000042')
        g.node(arg, arg)

    edges = [x + y for x, y in relations]
    g.edges(edges)
    return g


# TODO visualize multiple graph
def visualize_multiple_graph(args, relations, solutions):
    graphs = Digraph(name="parent", format="png", engine="neato")

    # for i in range(len(solutions)):
    #     graph = GraphViz(name=f'solution {i}', node_attr={'shape': 'box'})
    #     for arg in args:
    #         if arg in solutions[i]:
    #             graph.node(arg, arg, style="filled", fillcolor='#ff000042')
    #         graph.node(arg, arg)
    #     edges = [x + y for x, y in relations]
    #     graph.edges(edges)
    #     graphs.subgraph(graph)
    # graphs.render('solutions_args', format='png', view=True)

    for i in range(len(solutions)):
        with graphs.subgraph(name=f"cluster{i}") as sg:
            for arg in args:
                if arg in solutions[i]:
                    sg.node(arg, arg, style="filled", fillcolor='#ff000042')
                sg.node(arg, arg)

            edges = [x + y for x, y in relations]
            sg.edges(edges)

    graphs.render('simple_graph', format='png', view=True)


if __name__ == '__main__':
    # args, relations = read_user_input()
    # args = ['a', 'b', 'c', 'd', 'e']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    # graph = build_arguments_graph(args, relations)
    # graph.print_adj()
    # solve_simple_chain_args(graph)
    # visualize_graph(args, relations)
    # if graph.is_cyclic():
    #     print("Graph contains cycle")
    # else:
    #     print("Graph doesn't contain cycle")

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

    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
    # expected_result = {'a', 'b'}
    # args = ['a', 'b', 'c', 'd']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('d', 'c')]
    # expected_result = set()

    # args = ['a', 'b', 'c']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
    # expected_result = set()

    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('a', 'b'), ('b', 'f'), ('f', 'a'), ('e', 'a'), ('b', 'c'), ('c', 'd')]
    # expected_result = set()
    # args = ['a', 'b', 'c', 'd', 'f']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'f')]
    # expected_result = set()

    # args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('i', 'h'), ('h', 'g'), ('g', 'c'),
    #              ('c', 'j'), ('k', 'l'), ('l', 'b')]
    # expected_result = {'a', 'i', 'g', 'd', 'e'}
    #
    # graph = build_arguments_graph(args, relations)
    # # graph.print_adj()
    # solution = find_admissible_args_simple_chained_argsV2(graph)
    # print("solution =", solution)
    # visualize_graph(args, relations, solution)
    # args = ['a', 'b', 'c']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
    # solutions = [set(), {'a', 'c'}, {'b'}]

    # args = ['a', 'b', 'c', 'd']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
    # solutions = [set(), {'a', 'c'}, {'b'}]

    # args = ['a', 'b', 'c', 'd']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('d', 'c')]
    # solutions = [set(), {'a', 'c'}, {'b'}]

    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
    # solutions = [set(), {'a', 'c'}, {'b'}]

    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
    # solutions = [{'a', 'c', 'f'}, {'a', 'c', 'e'}, {'b', 'd', 'f'}]

    args = ['a', 'b', 'c', 'd', 'e', 'f']
    relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
    solutions = [{'a', 'c', 'f'}, {'a', 'c', 'e'}, {'b', 'd', 'f'}]
    #
    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
    # solutions = [{'a', 'c', 'f'}, {'a', 'c', 'e'}, {'b', 'd', 'f'}]

    # args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    # relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'g'), ('g', 'f'), ('f', 'g'),
    #              ('f', 'h'), ('h', 'i')]
    # solutions = [{'a', 'c', 'f'}, {'b', 'd', 'e'}, {'b', 'd', 'f'}]

    # args = ['a', 'b', 'c', 'd', 'e', 'f']
    # relations = [('e', 'a'), ('a', 'e'), ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('c', 'f')]
    # solutions = [{'a', 'c', 'f'}, {'b', 'd', 'e'}, {'b', 'd', 'f'}]

    # args = ['a', 'b', 'c', 'd']
    # relations = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
    # solutions = [{'a', 'c', 'f'}, {'b', 'd', 'e'}, {'b', 'd', 'f'}]

    # args = ['a', 'b', 'c']
    # relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
    # solutions = [{}, {'a'}, {'b'}]

    visualize_graph(args, relations, set())
    graph = build_arguments_graph(args, relations)
    result = completed_semantic_admissible_args(graph)
    print("result = ", result)
