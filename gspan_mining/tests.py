import itertools
import unittest
from gspan import gSpan

class SimpleCloseGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.f = open("unittestNaiveOutput.txt", "w")

    @classmethod
    def tearDownClass(self) -> None:
        self.f.close()

    def get_info(self,max_subgraphs):
        # max_subgraphs[-1] gets the largest bin of frequent subgraphs
        # max_subgraphs[1][0] gets the tuple of DFS code and projection of the largest frequent subgraph
        # max_subgraphs[-1][0][0] gets the DFS code of the largest frequent subgraph

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        return dfs_code,projection,g

    def get_single_result(self,gs, max_subgraphs):
        dfs_code, projection, g = self.get_info(max_subgraphs=max_subgraphs)

        support = str(gs._get_support(projection))
        description = g.display()
        num_vert = str(dfs_code.get_num_vertices())
        result_1 = (support, description, num_vert)

        results = [result_1]
        return results

    def get_multiple_results(self, gs, max_subgraphs):
        results = []
        for bin in max_subgraphs:
            for dfscode_and_projection in bin:
                dfs_code = dfscode_and_projection[0]
                projection = dfscode_and_projection[1]
                counter = itertools.count()
                g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

                support = str(gs._get_support(projection))
                description = g.display()
                num_vert = str(dfs_code.get_num_vertices())
                result = (support, description, num_vert)
                results.append(result)
        return results

    def updateOutput(self,results):
        self.f.write(str(sorted(results)) + "\n")

    def test_testcase_00(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.0",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        results = self.get_single_result(gs,max_subgraphs)

        solution_1 = ('2', 'v 0 A v 1 B v 2 C v 3 D e 0 1 x e 1 2 y e 1 3 z ', '4')
        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_01(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.1",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs

        results = self.get_single_result(gs,max_subgraphs)

        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C v 3 D e 0 1 x e 1 2 y e 2 3 z "
        solution_num_vert = "4"
        solution_1 = (solution_support, solution_description, solution_num_vert)

        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_02(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.2",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_single_result(gs, max_subgraphs)

        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C e 0 1 x e 0 2 z e 1 2 y "
        solution_num_vert = "3"
        solution_1 = (solution_support, solution_description, solution_num_vert)

        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_03(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.3",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_single_result(gs, max_subgraphs)

        solution_support = "2"
        solution_description = "v 0 A v 1 B v 2 C v 3 D v 4 E e 0 1 w e 0 2 x e 0 3 y e 0 4 z "
        solution_num_vert = "5"
        solution_1 = (solution_support, solution_description, solution_num_vert)

        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_04(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.4",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_single_result(gs, max_subgraphs)

        solution_support = "2"
        solution_description = "v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 1 2 v e 2 3 w "
        solution_num_vert = "4"
        solution_1 = (solution_support, solution_description, solution_num_vert)

        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_05(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.5",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_single_result(gs, max_subgraphs)

        solution_support = "2"
        solution_description = "v 0 A v 1 D v 2 E v 3 B v 4 C e 0 1 y e 0 3 z e 1 2 w e 3 4 x "
        solution_num_vert = "5"
        solution_1 = (solution_support, solution_description, solution_num_vert)

        solutions = [solution_1]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_06(self):
        #Placeholder test for repeat of testcase 1 with a third graph added
        self.assertEqual(True,True)

    def test_testcase_07(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.7",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 B v 2 C e 0 1 x e 1 2 y '
        solution_num_vert_1 = "3"
        solution_1 = (solution_support_1, solution_description_1, solution_num_vert_1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 B v 2 C e 0 1 x e 0 2 z e 1 2 y '
        solution_num_vert_2 = "3"
        solution_2 = (solution_support_2, solution_description_2, solution_num_vert_2)

        solutions = [solution_1, solution_2]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_08(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.8",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 B v 2 C v 3 D e 0 1 w e 0 2 x e 0 3 y '
        solution_num_vert_1 = "4"
        solution_1 = (solution_support_1, solution_description_1, solution_num_vert_1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 B v 2 C v 3 D v 4 E e 0 1 w e 0 2 x e 0 3 y e 0 4 z '
        solution_num_vert_2 = "5"
        solution_2 = (solution_support_2, solution_description_2, solution_num_vert_2)

        solutions = [solution_1, solution_2]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_09(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.9",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 2 3 w '
        solution_num_vert_1 = "4"
        solution_1 = (solution_support_1, solution_description_1, solution_num_vert_1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 D v 2 C v 3 B e 0 1 x e 0 2 y e 0 3 z e 1 2 v e 2 3 w '
        solution_num_vert_2 = "4"
        solution_2 = (solution_support_2, solution_description_2, solution_num_vert_2)

        solutions = [solution_1, solution_2]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_10(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.10",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)

        solution_support_1 = "3"
        solution_description_1 = 'v 0 A v 1 D v 2 B v 3 C e 0 1 y e 0 2 z e 2 3 x '
        solution_num_vert_1 = "4"
        solution_1 = (solution_support_1, solution_description_1, solution_num_vert_1)

        solution_support_2 = "2"
        solution_description_2 = 'v 0 A v 1 D v 2 E v 3 B v 4 C e 0 1 y e 0 3 z e 1 2 w e 3 4 x '
        solution_num_vert_2 = "5"
        solution_2 = (solution_support_2, solution_description_2, solution_num_vert_2)

        solutions = [solution_1, solution_2]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

    def test_testcase_11(self):
        gs = gSpan(
            database_file_name="../graphdata/graph.data.testcase.11",
            min_support=2
        )
        gs.run()
        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)

        solution_1 = ('2','v 0 A v 1 AA v 2 B v 3 C v 4 D v 5 E v 6 F v 7 G e 0 1 m e 1 2 n e 1 5 q e 2 3 o e 3 4 p e 5 6 r e 6 7 s ','8')
        solution_2 = ('3','v 0 A v 1 AA v 2 B v 3 E e 0 1 m e 1 2 n e 1 3 q ','4')
        solutions = [solution_1, solution_2]

        self.updateOutput(results)
        self.assertEqual(sorted(solutions), sorted(results))

if __name__ == '__main__':
    unittest.main()
