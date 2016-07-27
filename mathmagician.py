# also look at generators
import time
import sys

class Mathmagician:

  def generate_integers(self, int_count): #0 +
    #if True:
      # this is another option to the else block
    #  return [number for number in range(int_count)]
    #else:
    list_of_ints = list()
    for number in range(int_count):
      list_of_ints.append(number)
    self.print_results(list_of_ints)
    return list_of_ints


  def generate_fibonacci(self, fib_count): # numbers add to each other 112358
    list_of_fibs = list()

    def fib():
      i, j = 0, 1
      yield i
      yield j

      while True:
        i, j = j, i + j
        yield j
    f = fib()
    for i in range(fib_count):
      list_of_fibs.append(f.__next__())
    # Call Print
    self.print_results(list_of_fibs)
    return list_of_fibs


  def generate_primes(self, primes_count): # can divide by 1 or itself only w no remainder
    list_of_primes = list()

    num = 2
    while len(list_of_primes) < primes_count:
      for i in range(2, num):
        if num % i == 0:
          break
      else:
        list_of_primes.append(num)
      num +=1
    self.print_results(list_of_primes)
    return list_of_primes


  def invalid_input(self): # not valid input
    print('Please enter a valid selection')
    time.sleep(3)


  def print_results(self, iterable):
    for item in iterable:
      print(item)
      time.sleep(.01)


  def show_menu(self):
    while True:
      # Main loop, for use in getting function we want to run, must be 1-4
      print("""I am the Math Magician. What would you like me to do?

      1. List prime numbers
      2. Show fibonacci sequence
      3. List integers
      4. Quit""")
      choice = input("> ")

      option_to_run = self.validate_menu_option_choices(choice)
      # if this option_to_run variable returned as anything valid other than False, then the
      # user has selected a valid option ( 1-4)

      if option_to_run != False:
        # at this point we know we have a valid option (1-4)
        # lets find out how many iterations to run.
        while True:
          print("How many of these should I calculate??  Or press 'b' to return to Main Menu")
          choice = input("> ")

          try:
            number_of_iterations = int(choice) # number of iterations passed into generate
          except Exception:
            print("Please Enter a Valid Integer OR 'b' to return to the Main Menu")
            # choice = choice.lower()
            if choice in ('b', 'B'):
              break
            else:
              continue
          if option_to_run == 1:
            self.generate_primes(number_of_iterations)
          elif option_to_run == 2:
            self.generate_fibonacci(number_of_iterations)
          elif option_to_run == 3:
            self.generate_integers(number_of_iterations)
          else:
            # option to run not 1-3 then it must be 4, as we have validated that
            # above.
            sys.exit()

  def validate_menu_option_choices(self, choice):
      try:
        choice = int(choice)
      except Exception:
        self.invalid_input()
        return False
      if choice in (1,2,3):
        return choice
      elif choice == 4:
        sys.exit()
      else:
        return False


if __name__=="__main__":
  pass
  m = Mathmagician()
  m.show_menu()

# To Run
# python mathmagician.py