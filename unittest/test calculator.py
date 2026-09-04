import unittest
import calculator

class TestCalculator(unittest.TestCase):

  def test_add(self):
    result = calculator.add(10,20)
    self.assertEqual(result, 30)

  def test_sub(self):
    result = calculator.sub(20,10)
    self.assertEqual(result, 10)

  def test_mul(self):
    result = calculator.mul(10,2)
    self.assertEqual(result, 20)

  def test_div(self):
    result = calculator.div(10, 2)
    self.assertEqual(result, 5)

if __name__ == "__main__":
  unittest.main()