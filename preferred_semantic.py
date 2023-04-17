#!/usr/bin/env python3
from main import read_user_input, build_arguments_graph, preferred_semantic_admissible_args


if __name__ == '__main__':
    """
    Exemple:
    > a,b,c,d, e,f,g,h,i
    Veuillez saisir les relations d'attaque entre ces arguments séparer par des points virgules: 
    Exemple:  (a,b); (b,c) signifie 'a' attaque 'b' et 'b' attaque 'c': 
    
    > (a, b); (b, c); (c, d); (d, a); (d, e); (e, g); (g, f); (f, g); (f, h); (h, i)
    Les arguments:  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    Les relations d'attaque : [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('d', 'e'), ('e', 'g'), ('g', 'f'), ('f', 'g'), ('f', 'h'), ('h', 'i')]
    Les arguments admissibles selon la preferred semantic sont  [{'g', 'h', 'd', 'b'}, {'d', 'f', 'b', 'i'}, {'c', 'e', 'f', 'a', 'i'}]
    """
    arguments, relations = read_user_input()
    graph = build_arguments_graph(arguments, relations)
    result = preferred_semantic_admissible_args(graph)
    # visualize_graph(arguments, relations, {'c', 'e', 'f', 'a', 'i'})
    # visualize_graph(arguments, relations, result[1])
    # visualize_graph(arguments, relations, result[2])
    print("Les arguments admissibles selon la preferred semantic sont ", result)
