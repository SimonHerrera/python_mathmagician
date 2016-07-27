## Below are the instructions for our exercise - 7/26/2016

### The program will print a list of integers, fibonacci or primes.
#### The user will select which one to run and how many it will output.

## To Run:
### To Run Program: python mathmagician.py
### To Run Tests: python mathmagician_tests.py -v

Mathmagician

Setup

mkdir -p ~/workspace/python/exercises/cli && cd $_
touch mathmagician.py
Instructions

Step 1

Write your unit tests to reflect what classes, methods, and I/O is expected for each feature.

Step 2

Your program will have one class with a minimum of three methods on it. Each method should also accept an argument that determines how many times the function should output a number.

print_integers(self, number_to_output)
print_fibonacci(self, number_to_output)
print_primes(self, number_to_output)
Write unit tests that will verify the output of each method. Do not write any implementation code until you have a unit test for each method that fails.

Step 3

Build the menu first with options to execute the three methods above. Make the last option 4. Quit program. When the user selects that option, make sure the program terminates (i.e. don't show the list of options again).

Step 4

Now you'll write the implementation code for your three methods, and the operation of the program itself.

You want it to do one of three mathematical operations. Update your prompt to be I am the Math Magician. What would you like me to do? The options will be Fibonacci, Primes, or Integers.

user_choice = input('I am the Math Magician. What would you like me to do? ')
The goal here is that once the user tells the program what operation to perform, it will spit out the numbers forever until you “ctrl+c”. print(“Ok. I’m going to help produce " + user_choice);
Use time.sleep(seconds) when you output each number to the console to make each number legible (otherwise it goes too fast).
Make sure that your code validates user input. As a software developer, part of your job will be to handle edge cases. Think about possible things that the user can do that don't match what you expect of them, because they will. For example, at the prompt, they could type in the string Integers.
Step 5

Document your implementation code with docstrings.
