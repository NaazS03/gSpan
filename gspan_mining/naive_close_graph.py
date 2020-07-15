import unittest
from gspan import gSpan
from gspan import DFScode

class SimpleCloseGraphTests(unittest.TestCase):

    def test_testcase_1(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.1",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph = DFScode()
        DFScode.push_back(subgraph, 0, 1,("A","x","B"))
        DFScode.push_back(subgraph, 1, 2, (-1, "y", "C"))
        DFScode.push_back(subgraph, 2, 3, (-1, "z", "D"))

        # result[-1] gets the largest bin of frequent subgraphs
        # result[1][0] gets the tuple of DFS code and projection of the largest frequent subgraph
        # result[-1][0][0] gets the DFS code of the largest frequent subgraph

        self.assertEqual(result[-1][0][0], subgraph)

    def test_testcase_2(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.2",
            min_support=2
        )
        gs.run()
        result = gs._max_subgraphs

        subgraph = DFScode()
        DFScode.push_back(subgraph, 0, 1,("A","x","B"))
        DFScode.push_back(subgraph, 1, 2, (-1, "y", "C"))
        DFScode.push_back(subgraph, 2, 0, (-1, "z", -1))

        self.assertEqual(result[-1][0][0], subgraph)


if __name__ == '__main__':
    unittest.main()
