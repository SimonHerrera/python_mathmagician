import unittest
from mathmagician import Mathmagician


class TestMathmagician (unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.magician = Mathmagician()


  def test_integers(self):
    integers = self.magician.generate_integers(8)
    self.assertEqual([0,1,2,3,4,5,6,7], integers)

  def test_fibonacci(self):
    fib = self.magician.generate_fibonacci(8)
    self.assertEqual([0,1,1,2,3,5,8,13], fib)

  def test_primes(self):
    primes = self.magician.generate_primes(8)
    self.assertEqual([2,3,5,7,11,13,17,19], primes)

  def test_menu_option_choices(self):
    option = self.magician.validate_menu_option_choices(1)
    self.assertEqual(1, option)
    option = self.magician.validate_menu_option_choices(2)
    self.assertEqual(2, option)
    option = self.magician.validate_menu_option_choices(3)
    self.assertEqual(3, option)
    option = self.magician.validate_menu_option_choices(5)
    self.assertEqual(False, option)

    # self.assertEqual(option, range(1,4))

    # range 1-3
    # fail i

    # self.assertEqual(validate_menu_option_choices(choice, range(1,5)))
    # self.assertEqual([1, 2, 3, 4], range(1,5))
    # self.assertEqual(self.magician.validate_menu_option_choices()(range, type(range(4)))

# To Run Tests
# python mathmagician_tests.py -v

if __name__ == '__main__':
    unittest.main()
    print('Running')













# python mathmagician_tests.py -v

if __name__ == '__main__':
    unittest.main()