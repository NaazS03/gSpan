import unittest
import itertools
from gspan import gSpan

class CompoundBenchmarkTests(unittest.TestCase):
    """
    Before running a benchmark test
    make sure that @profile is not commented out in gSpan if memory usage info is desired
    @profile lets the memory profiler work
    """

    # The test below took longer than 12 hours to complete. Results unknown
    # def test_compound_min_graph_size_2_support_3_percent(self):
    #     graph_dataset_size = 422
    #
    #     file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
    #     supp = graph_dataset_size * 0.03
    #     min_size_graph = 2
    #     gs = gSpan(
    #         database_file_name=file_name,
    #         min_support=supp,
    #         min_num_vertices=min_size_graph
    #     )
    #     gs.run()

    def test_compound_min_graph_size_2_support_4_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.04
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_6_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.06
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_7_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.07
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_8_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.08
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_9_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.09
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_2_support_10_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.1
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_7_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 7
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_12_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 12
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_17_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 17
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_22_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 22
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_27_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 27
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_32_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 32
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_37_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 37
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_compound_min_graph_size_42_support_5_percent(self):
        graph_dataset_size = 422

        file_name = "../graphdata/benchmark_tests/Coumpound_422.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 42
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

class ChemicalBenchmarkTests(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.f = open("benchmarkNaiveOutput.txt", "w")

    @classmethod
    def tearDownClass(self) -> None:
        self.f.close()

    def get_info(self, max_subgraphs):
        # max_subgraphs[-1] gets the largest bin of frequent subgraphs
        # max_subgraphs[1][0] gets the tuple of DFS code and projection of the largest frequent subgraph
        # max_subgraphs[-1][0][0] gets the DFS code of the largest frequent subgraph

        largest_bin = max_subgraphs[-1]
        dfscode_and_projection = largest_bin[0]
        dfs_code = dfscode_and_projection[0]
        projection = dfscode_and_projection[1]
        counter = itertools.count()
        g = dfs_code.to_graph(gid=next(counter), is_undirected=True)

        return dfs_code, projection, g

    def get_single_result(self, gs, max_subgraphs):
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

    def updateOutput(self, results):
        self.f.write(str(sorted(results)) + "\n")

    def test_chemical_min_graph_size_2_support_3_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.03
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_4_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.04
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_6_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.06
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_7_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.07
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_8_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.08
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_9_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.09
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_2_support_10_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.1
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()
    #End of min support tests

    def test_chemical_min_graph_size_2(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.45
        min_size_graph = 2
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

        max_subgraphs = gs._max_subgraphs
        results = self.get_multiple_results(gs,max_subgraphs)
        self.updateOutput(results)

    #Start of min graph size tests
    def test_chemical_min_graph_size_7_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 7
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_12_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 12
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_17_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 17
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_22_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 22
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_27_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 27
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

    def test_chemical_min_graph_size_32_support_5_percent(self):
        graph_dataset_size = 340

        file_name = "../graphdata/benchmark_tests/Chemical_340.txt"
        supp = graph_dataset_size * 0.05
        min_size_graph = 32
        gs = gSpan(
            database_file_name=file_name,
            min_support=supp,
            min_num_vertices=min_size_graph
        )
        gs.run()
        gs.time_stats()

if __name__ == '__main__':
    unittest.main()
