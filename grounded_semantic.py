#!/usr/bin/env python3
from main import read_user_input, visualize_graph, build_arguments_graph, grounded_admissible_args_cycle_args

if __name__ == '__main__':
    """
    Exemple:
    > a,b,c,d, e,f
    Veuillez saisir les relations d'attaque entre ces arguments séparer par des points virgules: 
    Exemple:  (a,b); (b,c) signifie 'a' attaque 'b' et 'b' attaque 'c': 
    
    > (a, b); (c, b); (b, c); (c, d); (d, e); (e, f)
    Les arguments:  ['a', 'b', 'c', 'd', 'e', 'f']
    Les relations d'attaque : [('a', 'b'), ('c', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
    Les arguments admissibles selon la grounded semantic sont  {'a', 'e', 'c'}
    """
    arguments, relations = read_user_input()
    graph = build_arguments_graph(arguments, relations)
    result = grounded_admissible_args_cycle_args(graph)
    visualize_graph(arguments, relations, result)
    print("Les arguments admissibles selon la grounded semantic sont ", result)
