import src.solution1 as lesson1
import src.solution2 as lesson2
import src.solution13 as lesson13
import unittest

class TestSolution(unittest.TestCase):
    def test_solution1(self):
        self.assertEqual(lesson1.solution(9), 2)
        self.assertEqual(lesson1.solution(529), 4)
        self.assertEqual(lesson1.solution(20), 1)
        self.assertEqual(lesson1.solution(15), 0)
        self.assertEqual(lesson1.solution(32), 0)
    
    def test_solution1(self):
        self.assertListEqual(lesson2.solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertListEqual(lesson2.solution([0, 0, 0], 1), [0, 0, 0])
        self.assertListEqual(lesson2.solution([1, 2, 3, 4], 4), [1, 2, 3, 4])

    def test_solution13(self):
        S = "CAGCCTA"
        P = [2 ,5 ,0]
        Q = [4, 5, 6]
        self.assertListEqual(lesson13.solution(S, P, Q), [2, 4, 1])

unittest.main()