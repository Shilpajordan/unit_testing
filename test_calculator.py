import unittest
from calc import Calculator



class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create calculator object
        # run once before the execution of all tests in the test class
        cls.calcu = Calculator()
        print('setUpClass was executed')
   # setUp prepares a test fixture .
    # this is called immediately before calling each test method.
    def setUp(self) :
        
    #variables for use with calculator
        self.a = 20
        self.b = 10

    #ADD
    def test_add(self):
        result = self.calcu.add(self.a,self.b)
        self.assertTrue(result == 30)
        self.assertEqual(type(result),type(30))


    #Subtract
    def test_subtract(self):
        result = self.calcu.subtract(self.a,self.b)
        self.assertTrue(result == 10)
        self.assertEqual(type(result),type(10))

    #Multiply
    def test_multiply(self):
        result = self.calcu.multiply(self.a,self.b)
        self.assertEqual(result, 200)
        self.assertEqual(type(result),type(200))

    #Divide
    def test_divide(self):
        result = self.calcu.divide(self.a,self.b)
        self.assertEqual(result, 2)
        self.assertEqual(type(result),type(2.0))




if __name__ == '__main__':
    unittest.main