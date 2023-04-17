#!/usr/bin/env python3
from main import read_user_input, visualize_graph, build_arguments_graph, find_admissible_args_simple_chained_argsV2

if __name__ == '__main__':
    """
    Exemple:
    > a,b,c,d, e
    Veuillez saisir les relations d'attaque entre ces arguments séparer par des points virgules: 
    Exemple:  (a,b); (b,c) signifie 'a' attaque 'b' et 'b' attaque 'c': 
    > (a,b); (b,c); (c,d); (d,e)
    Les arguments:  ['a', 'b', 'c', 'd', 'e']
    Les relations d'attaque : [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
    Les arguments acceptés sont  {'c', 'e', 'a'}
    """
    arguments, relations = read_user_input()
    graph = build_arguments_graph(arguments, relations)
    result = find_admissible_args_simple_chained_argsV2(graph)
    visualize_graph(arguments, relations, result)
    print("Les arguments acceptés sont ", result)
