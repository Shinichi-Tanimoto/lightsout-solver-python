#coding: utf-8

import unittest
import f2matrixanalyzer

class TestF2MatrixAnalyzer(unittest.TestCase):
    """ F2MatrixAnalyzerのテストコード"""

    def test_analyze1(self):
        input_matrix_array = [1, 1, 0, 0, 1, 1, 1, 1, 1]
        input_size = 3

        analyzer = f2matrixanalyzer.F2MatrixAnalyzer(input_matrix_array, input_size)
        analyzer.analyze()

        self.assertTrue(analyzer.has_inverse())

if __name__ == "__main__":
    unittest.main()
