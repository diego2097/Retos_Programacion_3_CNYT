from os.path import dirname, join, abspath
import sys 
sys.path.insert(0, abspath(join(dirname(__file__), '..')) + "\main")
import unittest
import math 
import BooleanMarbles as boolean
import ProbaMarbles as proba
import ComplexMarbles as complx

class TestMarbles(unittest.TestCase):

    def test_BooleanMarbles(self):
        matriz = [[0,0,0,0,0,0],
              [0,0,0,0,0,0],
              [0,1,0,0,0,1],
              [0,0,0,1,0,0],
              [0,0,1,0,0,0],
              [1,0,0,0,1,0]]
        vInicial = [6,2,1,5,3,10]
        clicks=1
        rta = boolean.marbles(matriz,vInicial,clicks)
        vrta = [0,0,12,5,1,9]
        self.assertEqual(rta,vrta)

    def test_ProbabilisticMarbles(self): 
        matriz = [[0,1/6,5/6],
                  [1/3,1/2,1/6],
                  [2/3,1/3,0]]
        vInicial = [1/6,1/6,2/3]
        clicks=1
        rta = proba.marbles(matriz,vInicial,clicks)
        vrta = [21/36,9/36,6/36]
        self.assertEqual(rta,vrta)

    def test_ComplexMarbles(self): 
        matriz = [[[0,0],[1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,0]],
                  [[1/math.sqrt(2),0],[0,0],[0,0],[-1/math.sqrt(2),0]], 
                  [[1/math.sqrt(2),0],[0,0],[0,0],[1/math.sqrt(2),0]],
                  [[0,0],[-1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,0]]
                            ]     
        v = [[1,0],[0,0],[0,0],[0,0]]
        clicks=1
        rta = complx.marbles(matriz,v,clicks)
        vrta = [[0,0],[1/math.sqrt(2),0],[1/math.sqrt(2),0],[0,0]]

        self.assertEqual(rta,vrta)


if __name__ == "__main__":
    unittest.main()