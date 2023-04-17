import unittest

from main import grounded, build_arguments_graph, visualize_graph, grounded_admissible_args_cycle_args


class TestCyclicArguments(unittest.TestCase):

    def test_grounded_one(self):
        args = ['a', 'b']
        relations = [('a', 'b'), ('b', 'a')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_grounded_one2(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('d', 'c')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_grounded_two(self):
        args = ['a', 'b', 'c']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_grounded_three(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_four(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, expected_result)
        self.assertSetEqual(expected_result, result)

    def test_five(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'd'), ('e', 'd'), ('e', 'f'), ('f', 'e')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_six(self):
        args = ['a', 'b', 'c']
        relations = [('b', 'a'), ('a', 'c'), ('c', 'a')]
        expected_result = {'b', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_seven(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_eight(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('c', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_nine(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('c', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'e'), ('f', 'g')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_ten(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'f')]
        expected_result = {'a', 'c', 'e', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_eleven(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'),
                     ('h', 'g')]
        expected_result = {'a', 'c', 'e'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_twelve(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'e')]
        expected_result = {'a'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_thirteen(self):
        args = ['a', 'b', 'c', 'd']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'c'), ('d', 'b')]
        expected_result = {'a', 'c'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_fourteen(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'e'), ('e', 'a')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_fifteen(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'e'), ('e', 'd')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_sixteen(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a'), ('c', 'e'), ('e', 'f'), ('f', 'e')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_sixteen2(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('e', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')]
        expected_result = {'e', 'b', 'd'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_seventeen(self):
        args = ['a', 'b', 'c', 'd', 'e']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'd'), ('d', 'e'), ('a', 'd'), ('b', 'd')]
        expected_result = set()
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, solution=set())
        self.assertSetEqual(expected_result, result)

    def test_eighteen(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'e'), ('g', 'f')]
        expected_result = {'a', 'c', 'e', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_nineteen(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'h'), ('h', 'e'), ('e', 'f'), ('f', 'e'), ('g', 'f')]
        expected_result = {'a', 'c', 'h', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)


    def test_nineteenV3(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'h'), ('e', 'h'), ('e', 'f'), ('f', 'e'), ('g', 'f')]
        expected_result = {'a', 'c', 'e', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_nineteenV1(self):
        args = ['i', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('i', 'a'), ('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'h'), ('h', 'e'), ('e', 'f'), ('f', 'e'), ('g', 'f')]
        expected_result = {'i',  'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_nineteenV2(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'b'), ('c', 'd'), ('d', 'h'), ('h', 'e'), ('e', 'f'), ('f', 'e'), ('g', 'f')]
        expected_result = {'a', 'c', 'h', 'g'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    def test_twenty(self):
        args = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        relations = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'c'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'e')]
        expected_result = {'a'}
        graph = build_arguments_graph(args, relations)
        result = grounded_admissible_args_cycle_args(graph)
        print(result)
        visualize_graph(args, relations, result)
        self.assertSetEqual(expected_result, result)

    # def test_twenty_one(self):
    #     args = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    #     relations = [('a', 'b'), ('c', 'b'), ('d', 'b'), ('b', 'e'), ('e', 'f'), ('f', 'e'), ('g', 'f'),
    #                  ('h', 'g'), ('i', 'h'), ('j', 'i'), ('k', 'g'), ('l', 'k')]
    #     expected_result = {'a'}
    #     graph = build_arguments_graph(args, relations)
    #     result = grounded_admissible_args_cycle_args(graph)
    #     print(result)
    #     visualize_graph(args, relations, set())
    #     self.assertSetEqual(expected_result, set())

