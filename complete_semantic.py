#!/usr/bin/env python3
from main import read_user_input, visualize_graph, build_arguments_graph, completed_semantic_admissible_args

args = ['a', 'b', 'c', 'd', 'e', 'f']
relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
solutions = [{'a', 'c', 'f'}, {'a', 'c', 'e'}, {'b', 'd', 'f'}]
if __name__ == '__main__':
    """
    Exemple:
    > a,b,c,d, e,f
    Veuillez saisir les relations d'attaque entre ces arguments séparer par des points virgules: 
    Exemple:  (a,b); (b,c) signifie 'a' attaque 'b' et 'b' attaque 'c': 
    
    > (a, b); (b, c); (c, d); (d, a); (d, e); (e, f); (f, e)
    Les arguments:  ['a', 'b', 'c', 'd', 'e', 'f']
    Les relations d'attaque : [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'f'), ('f', 'e')]
    Les arguments admissibles selon la complete semantic sont  [{'b', 'f', 'd'}, {'c', 'a', 'e'}, {'c', 'f', 'a'}, {}]
    """
    arguments, relations = read_user_input()
    graph = build_arguments_graph(arguments, relations)
    result = completed_semantic_admissible_args(graph)
    # visualize_graph(arguments, relations, {'c', 'e', 'f', 'a', 'i'})
    visualize_graph(arguments, relations, set())
    # visualize_graph(arguments, relations, result[2])
    print("Les arguments admissibles selon la complete semantic sont ", result)
