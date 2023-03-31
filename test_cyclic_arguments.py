import unittest

from v2 import grounded, build_arguments_graph, visualize_graph


class TestCyclicArguments(unittest.TestCase):

    def test_grounded_one(self):
        args = ['a', 'b']
        relations = [('a', 'b'), ('b', 'a')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_grounded_two(self):
        args = ['a', 'b', 'c']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_grounded_three(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        self.assertSetEqual(expected_result, result)
        # visualize_graph(args, relations)

    def test_four(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd')]
        expected_result = {'d'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_five(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('e', 'd'), ('e', 'f'), ('f', 'e')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_six(self):
        args = ['a', 'b', 'c']
        relations = [('b', 'a'), ('a', 'c'), ('c', 'a')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_seven(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        # visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_eight(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('c', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_nine(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('c', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'e'), ('f', 'g')]
        expected_result = {'a', 'c', 'g', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_ten(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'f')]
        expected_result = {'a', 'c', 'e', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_eleven(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'),('h', 'g') ]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)


    def test_twelve(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'e')]
        expected_result = {'a', 'd', 'f'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_thirteen(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'c'), ('d', 'b')]
        expected_result = {'a'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)

    def test_fourteen(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'a')]
        expected_result = {'a'}
        graph = build_arguments_graph(args, relations)
        result = grounded(graph)
        visualize_graph(args, relations)
        self.assertSetEqual(expected_result, result)