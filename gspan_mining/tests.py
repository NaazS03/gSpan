import itertools
import unittest
import numpy as np
from gspan import gSpan

class SimpleCloseGraphTests(unittest.TestCase):

    def test_testcase_1(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.1",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        # max_subgraphs[-1] gets the largest bin of frequent subgraphs
        # max_subgraphs[1][0] gets the tuple of DFS code and projection of the largest frequent subgraph
        # max_subgraphs[-1][0][0] gets the DFS code of the largest frequent subgraph

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        support = gs._get_support(projection)
        description = g.display()
        num_vert = dfs_code.get_num_vertices()
        result = np.array([support,description,num_vert]).astype(str).reshape(1,-1)

        # subgraph = DFScode()
        # DFScode.push_back(subgraph, 0, 1,("A","x","B"))
        # DFScode.push_back(subgraph, 1, 2, (-1, "y", "C"))
        # DFScode.push_back(subgraph, 2, 3, (-1, "z", "D"))
        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C v 3 D e 0 1 x e 1 2 y e 2 3 z "
        solution_num_vert = "4"
        answer = np.array([solution_support, solution_description, solution_num_vert]).astype(str).reshape(1,-1)

        self.assertEqual(answer[0][0], result[0][0])
        self.assertEqual(answer[0][1], result[0][1])
        self.assertEqual(answer[0][2], result[0][2])
        self.assertEqual(len(max_subgraphs[-1]), 1)

    def test_testcase_2(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.2",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        support = gs._get_support(projection)
        description = g.display()
        num_vert = dfs_code.get_num_vertices()
        result = np.array([support,description,num_vert]).astype(str).reshape(1,-1)

        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C e 0 1 x e 0 2 z e 1 2 y "
        solution_num_vert = "3"
        answer = np.array([solution_support, solution_description, solution_num_vert]).astype(str).reshape(1,-1)


        self.assertEqual(answer[0][0], result[0][0])
        self.assertEqual(answer[0][1], result[0][1])
        self.assertEqual(answer[0][2], result[0][2])
        self.assertEqual(len(max_subgraphs[-1]), 1)

    def test_testcase_3(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.3",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        support = gs._get_support(projection)
        description = g.display()
        num_vert = dfs_code.get_num_vertices()
        result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C v 3 D v 4 E e 0 1 w e 0 2 x e 0 3 y e 0 4 z "
        solution_num_vert = "5"
        answer = np.array([solution_support, solution_description, solution_num_vert]).astype(str).reshape(1, -1)

        self.assertEqual(answer[0][0], result[0][0])
        self.assertEqual(answer[0][1], result[0][1])
        self.assertEqual(answer[0][2], result[0][2])
        self.assertEqual(len(max_subgraphs[-1]), 1)

    def test_testcase_4(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.4",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        support = gs._get_support(projection)
        description = g.display()
        num_vert = dfs_code.get_num_vertices()
        result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

        solution_support = "2"
        solution_description = "v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 1 2 v e 2 3 w "
        solution_num_vert = "4"
        answer = np.array([solution_support, solution_description, solution_num_vert]).astype(str).reshape(1, -1)

        self.assertEqual(answer[0][0], result[0][0])
        self.assertEqual(answer[0][1], result[0][1])
        self.assertEqual(answer[0][2], result[0][2])
        self.assertEqual(len(max_subgraphs[-1]), 1)

    def test_testcase_5(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.5",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        support = gs._get_support(projection)
        description = g.display()
        num_vert = dfs_code.get_num_vertices()
        result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

        solution_support = "2"
        solution_description = "v 0 A v 1 D v 2 E v 3 B v 4 C e 0 1 y e 0 3 z e 1 2 w e 3 4 x "
        solution_num_vert = "5"
        answer = np.array([solution_support, solution_description, solution_num_vert]).astype(str).reshape(1, -1)

        self.assertEqual(answer[0][0], result[0][0])
        self.assertEqual(answer[0][1], result[0][1])
        self.assertEqual(answer[0][2], result[0][2])
        self.assertEqual(len(max_subgraphs[-1]), 1)

    def test_testcase_6(self):
        #Placeholder test for repeat of testcase 1 with a third graph added
        self.assertEqual(True,True)

    def test_testcase_7(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.7",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 B v 2 C e 0 1 x e 1 2 y '
        solution_num_vert_1 = "3"
        solution_1 = np.array([solution_support_1, solution_description_1, solution_num_vert_1]).astype(str).reshape(1, -1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 B v 2 C e 0 1 x e 0 2 z e 1 2 y '
        solution_num_vert_2 = "3"
        solution_2 = np.array([solution_support_2, solution_description_2, solution_num_vert_2]).astype(str).reshape(1, -1)

        solutions = [solution_1, solution_2]

        for bin in max_subgraphs:
            for dfscode_and_projection in bin:
                dfs_code = dfscode_and_projection[0]
                projection = dfscode_and_projection[1]
                counter = itertools.count()
                g = dfs_code.to_graph(gid=next(counter), is_undirected=True)
                support = gs._get_support(projection)
                description = g.display()
                num_vert = dfs_code.get_num_vertices()
                result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

                for solution_index in range(0,len(solutions)):
                    solution = solutions[solution_index]
                    if solution[0][0] == result[0][0] and solution[0][1] == result[0][1] and solution[0][2] == result[0][2]:
                        self.assertTrue(True, "The proposed answer matches an existing solution.")
                        del solutions[solution_index]
                        break

        if len(solutions) != 0:
            self.assertTrue(False, "All possible solutions were not found")

    def test_testcase_8(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.8",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 B v 2 C v 3 D e 0 1 w e 0 2 x e 0 3 y '
        solution_num_vert_1 = "4"
        solution_1 = np.array([solution_support_1, solution_description_1, solution_num_vert_1]).astype(str).reshape(1,-1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 B v 2 C v 3 D v 4 E e 0 1 w e 0 2 x e 0 3 y e 0 4 z '
        solution_num_vert_2 = "5"
        solution_2 = np.array([solution_support_2, solution_description_2, solution_num_vert_2]).astype(str).reshape(1,-1)

        solutions = [solution_1, solution_2]

        for bin in max_subgraphs:
            for dfscode_and_projection in bin:
                dfs_code = dfscode_and_projection[0]
                projection = dfscode_and_projection[1]
                counter = itertools.count()
                g = dfs_code.to_graph(gid=next(counter), is_undirected=True)
                support = gs._get_support(projection)
                description = g.display()
                num_vert = dfs_code.get_num_vertices()
                result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

                for solution_index in range(0, len(solutions)):
                    solution = solutions[solution_index]
                    if solution[0][0] == result[0][0] and solution[0][1] == result[0][1] and solution[0][2] == result[0][2]:
                        self.assertTrue(True, "The proposed answer matches an existing solution.")
                        del solutions[solution_index]
                        break

        if len(solutions) != 0:
            self.assertTrue(False, "All possible solutions were not found")

    def test_testcase_9(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.9",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 2 3 w '
        solution_num_vert_1 = "4"
        solution_1 = \
            np.array([solution_support_1, solution_description_1, solution_num_vert_1]).astype(str).reshape(1,-1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 1 2 v e 2 3 w '
        solution_num_vert_2 = "4"
        solution_2 = \
            np.array([solution_support_2, solution_description_2, solution_num_vert_2]).astype(str).reshape(1,-1)

        solutions = [solution_1, solution_2]

        for bin in max_subgraphs:
            for dfscode_and_projection in bin:
                dfs_code = dfscode_and_projection[0]
                projection = dfscode_and_projection[1]
                counter = itertools.count()
                g = dfs_code.to_graph(gid=next(counter), is_undirected=True)
                support = gs._get_support(projection)
                description = g.display()
                num_vert = dfs_code.get_num_vertices()
                result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

                for solution_index in range(0, len(solutions)):
                    solution = solutions[solution_index]
                    if solution[0][0] == result[0][0] and solution[0][1] == result[0][1] and solution[0][2] == \
                            result[0][2]:
                        self.assertTrue(True, "The proposed answer matches an existing solution.")
                        del solutions[solution_index]
                        break

        if len(solutions) != 0:
            self.assertTrue(False, "All possible solutions were not found")

    def test_testcase_10(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.10",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 D v 2 B v 3 C e 0 1 y e 0 2 z e 2 3 x '
        solution_num_vert_1 = "4"
        solution_1 = \
            np.array([solution_support_1, solution_description_1, solution_num_vert_1]).astype(str).reshape(1, -1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 D v 2 E v 3 B v 4 C e 0 1 y e 0 3 z e 1 2 w e 3 4 x '
        solution_num_vert_2 = "5"
        solution_2 = \
            np.array([solution_support_2, solution_description_2, solution_num_vert_2]).astype(str).reshape(1, -1)

        solutions = [solution_1, solution_2]

        for bin in max_subgraphs:
            for dfscode_and_projection in bin:
                dfs_code = dfscode_and_projection[0]
                projection = dfscode_and_projection[1]
                counter = itertools.count()
                g = dfs_code.to_graph(gid=next(counter), is_undirected=True)
                support = gs._get_support(projection)
                description = g.display()
                num_vert = dfs_code.get_num_vertices()
                result = np.array([support, description, num_vert]).astype(str).reshape(1, -1)

                for solution_index in range(0, len(solutions)):
                    solution = solutions[solution_index]
                    if solution[0][0] == result[0][0] and solution[0][1] == result[0][1] and solution[0][2] == \
                            result[0][2]:
                        self.assertTrue(True, "The proposed answer matches an existing solution.")
                        del solutions[solution_index]
                        break

        if len(solutions) != 0:
            self.assertTrue(False, "All possible solutions were not found")


if __name__ == '__main__':
    unittest.main()
