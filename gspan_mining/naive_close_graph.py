import itertools
import unittest
import numpy as np
from gspan import gSpan
from gspan import DFScode

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
        result = gs._max_subgraphs

        subgraph = DFScode()
        DFScode.push_back(subgraph, 0, 1,("A","y","C"))
        DFScode.push_back(subgraph, 1, 2, (-1, "v", "D"))
        DFScode.push_back(subgraph, 0, 3, (-1, "z", "B"))

        self.assertEqual(result[-1][0][0], subgraph)
        self.assertEqual(len(result[-1]), 1)

    def test_testcase_5(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.5",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph = DFScode()
        DFScode.push_back(subgraph, 0, 1,("A","y","D"))
        DFScode.push_back(subgraph, 1, 2, (-1, "w", "E"))
        DFScode.push_back(subgraph, 0, 3, (-1, "z", "B"))
        DFScode.push_back(subgraph, 3, 4, (-1, "x", "C"))

        self.assertEqual(result[-1][0][0], subgraph)
        self.assertEqual(len(result[-1]), 1)

    def test_testcase_6(self):
        #Placeholder test for repeat of testcase 1 with a third graph added
        self.assertEqual(True,True)

    def test_testcase_7(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.7",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph1 = DFScode()
        DFScode.push_back(subgraph1, 0, 1,("A","x","B"))
        DFScode.push_back(subgraph1, 1, 2, (-1, "y", "C"))

        subgraph2 = DFScode()
        DFScode.push_back(subgraph2, 0, 1,("A","x","B"))
        DFScode.push_back(subgraph2, 1, 2, (-1, "y", "C"))
        DFScode.push_back(subgraph2, 2, 0, (-1, "z", -1))

        self.assertEqual(result[-1][0][0], subgraph1)
        self.assertEqual(result[-1][1][0], subgraph2)
        self.assertEqual(len(result[-1]), 2)

    def test_testcase_8(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.8",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph1 = DFScode()
        DFScode.push_back(subgraph1, 0, 1,("A","w","B"))
        DFScode.push_back(subgraph1, 0, 2, (-1, "x", "C"))
        DFScode.push_back(subgraph1, 0, 3, (-1, "y", "D"))
        DFScode.push_back(subgraph1, 0, 4, (-1, "z", "E"))

        subgraph2 = DFScode()
        DFScode.push_back(subgraph2, 0, 1,("A","w","B"))
        DFScode.push_back(subgraph2, 0, 2, (-1, "x", "C"))
        DFScode.push_back(subgraph2, 0, 3, (-1, "y", "D"))

        self.assertEqual(result[-1][0][0], subgraph1)
        self.assertEqual(result[-2][0][0], subgraph2)

        total_subgraphs = 0
        for bin in result:
            total_subgraphs += len(bin)

        self.assertEqual(total_subgraphs, 2)

    def test_testcase_8(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.8",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph1 = DFScode()
        DFScode.push_back(subgraph1, 0, 1, ("A", "w", "B"))
        DFScode.push_back(subgraph1, 0, 2, (-1, "x", "C"))
        DFScode.push_back(subgraph1, 0, 3, (-1, "y", "D"))
        DFScode.push_back(subgraph1, 0, 4, (-1, "z", "E"))

        subgraph2 = DFScode()
        DFScode.push_back(subgraph2, 0, 1, ("A", "w", "B"))
        DFScode.push_back(subgraph2, 0, 2, (-1, "x", "C"))
        DFScode.push_back(subgraph2, 0, 3, (-1, "y", "D"))

        self.assertEqual(result[-1][0][0], subgraph1)
        self.assertEqual(result[-2][0][0], subgraph2)

        total_subgraphs = 0
        for bin in result:
            total_subgraphs += len(bin)

        self.assertEqual(total_subgraphs, 2)

    def test_testcase_9(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.9",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph1 = DFScode()
        DFScode.push_back(subgraph1, 0, 1, ("A", "y", "C"))
        DFScode.push_back(subgraph1, 1, 2, (-1, "v", "D"))
        DFScode.push_back(subgraph1, 0, 3, (-1, "z", "B"))

        subgraph2 = DFScode()
        DFScode.push_back(subgraph2, 0, 1, ("A", "x", "D"))
        DFScode.push_back(subgraph2, 0, 2, (-1, "y", "C"))
        DFScode.push_back(subgraph2, 2, 3, (-1, "w", "B"))
        DFScode.push_back(subgraph2, 3, 0, (-1, "z", -1))

        self.assertEqual(result[-1][0][0], subgraph1)
        self.assertEqual(result[-1][1][0], subgraph2)

        total_subgraphs = 0
        for bin in result:
            total_subgraphs += len(bin)

        self.assertEqual(total_subgraphs, 2)

    def test_testcase_10(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.10",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph1 = DFScode()
        DFScode.push_back(subgraph1, 0, 1, ("A", "y", "D"))
        DFScode.push_back(subgraph1, 1, 2, (-1, "w", "E"))
        DFScode.push_back(subgraph1, 0, 3, (-1, "z", "B"))
        DFScode.push_back(subgraph1, 3, 4, (-1, "x", "C"))

        subgraph2 = DFScode()
        DFScode.push_back(subgraph2, 0, 1, ("A", "y", "D"))
        DFScode.push_back(subgraph2, 0, 2, (-1, "z", "B"))
        DFScode.push_back(subgraph2, 2, 3, (-1, "x", "C"))

        self.assertEqual(result[-1][0][0], subgraph1)
        self.assertEqual(result[-2][0][0], subgraph2)

        total_subgraphs = 0
        for bin in result:
            total_subgraphs += len(bin)

        self.assertEqual(total_subgraphs, 2)


if __name__ == '__main__':
    unittest.main()
