import unittest

from v2 import grounded_semantic, build_arguments_graph, visualize_graph


class TestSimpleChainArguments(unittest.TestCase):

    def test_one(self):
        args = ['a', 'b', 'c']
        relations = [('a', 'b'), ('b', 'c')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_two(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_three(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        self.assertSetEqual(expected_result, result)
        # visualize_graph(args, relations)

    def test_four(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('d', 'c')]
        expected_result = {'a', 'd'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_five(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('d', 'c'), ('e', 'd')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_six(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('e', 'd')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_seven(self):
        args = ['a', 'b', 'c']
        relations = [('c', 'a'), ('c', 'b')]
        expected_result = {'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_eight(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('c', 'a'), ('c', 'b'), ('d', 'b'), ('d', 'e')]
        expected_result = {'c', 'd'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_night(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('b', 'a'), ('b', 'c'), ('f', 'c'), ('c', 'd'), ('e', 'd')]
        expected_result = {'e', 'b', 'f'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_ten(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('b', 'a'), ('b', 'c'), ('f', 'c'), ('c', 'd'), ('d', 'e'), ('g', 'e')]
        expected_result = {'b', 'd', 'g', 'f'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_eleven(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('b', 'c'), ('f', 'e'), ('c', 'e'), ('d', 'c')]
        expected_result = {'a', 'd', 'f'}
        graph = build_arguments_graph(args, relations)
        result = grounded_semantic(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)
