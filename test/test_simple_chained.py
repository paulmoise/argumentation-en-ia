import unittest

from main import solve_simple_chain_args, build_arguments_graph, visualize_graph, \
    find_admissible_args_simple_chained_args, find_admissible_args_simple_chained_argsV2


class TestSimpleChainArguments(unittest.TestCase):

    def test_one(self):
        args = ['a', 'b', 'c']
        relations = [('a', 'b'), ('b', 'c')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_two(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_three(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        self.assertSetEqual(expected_result, result)
        visualize_graph(args, relations, result)

    def test_four(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('d', 'c')]
        expected_result = {'a', 'd'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_five(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('d', 'c'), ('e', 'd')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_six(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('e', 'd')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_sixV2(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('d', 'c')]
        expected_result = {'a', 'd'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_seven(self):
        args = ['a', 'b', 'c']
        relations = [('c', 'a'), ('c', 'b')]
        expected_result = {'c'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_eight(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('c', 'a'), ('c', 'b'), ('d', 'b'), ('d', 'e')]
        expected_result = {'c', 'd'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_night(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('b', 'a'), ('b', 'c'), ('f', 'c'), ('c', 'd'), ('e', 'd')]
        expected_result = {'e', 'b', 'f'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_ten(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('b', 'a'), ('b', 'c'), ('f', 'c'), ('c', 'd'), ('d', 'e'), ('g', 'e')]
        expected_result = {'b', 'd', 'g', 'f'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_eleven(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('b', 'c'), ('f', 'e'), ('c', 'e'), ('d', 'c')]
        expected_result = {'a', 'd', 'f'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_twelve(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('i', 'h'), ('h', 'g'), ('g', 'c')]
        expected_result = {'a', 'i', 'g', 'd', 'e'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_twelveV2(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'e'), ('e', 'f'), ('g', 'c'), ('c', 'd')]
        expected_result = {'a', 'g', 'd', 'e'}
        graph = build_arguments_graph(args, relations)
        result = solve_simple_chain_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_thirteen(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('h', 'i'),
                     ('i', 'j')]
        expected_result = {'a', 'c', 'e', 'g', 'i'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_fourteen(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('e', 'f'), ('i', 'h'), ('h', 'g'), ('g', 'c'),
                     ('c', 'j'), ('k', 'l'), ('l', 'b')]
        expected_result = {'a', 'i', 'g', 'd', 'e', 'j', 'k'}
        graph = build_arguments_graph(args, relations)
        result = find_admissible_args_simple_chained_argsV2(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)
