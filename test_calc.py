################################
"""
Naming convention when writing tests is to start with 'test_'
"""
################################
import unittest
import calc

#creating a test class
class TestCalc(unittest.TestCase):
    
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
# 
if __name__ == '__main__':
    unittest.main