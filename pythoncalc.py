import numpy as np

def matrix_calculator():
  # Prompt the user to enter a matrix
  matrix = input("Enter a matrix in the form [[a, b, c], [d, e, f], [g, h, i]]: ")
  
  # Convert the input to a numpy array
  matrix = np.array(matrix)
  
  # Print the matrix
  print("Matrix:")
  print(matrix)
  
  # Calculate and print the determinant
  determinant = np.linalg.det(matrix)
  print("Determinant:", determinant)
  
  # Calculate and print the inverse
  inverse = np.linalg.inv(matrix)
  print("Inverse:")
  print(inverse)
  
  # Calculate and print the transpose
  transpose = np.transpose(matrix)
  print("Transpose:")
  print(transpose)
  
  # Calculate and print the mean
  mean = np.mean(matrix)
  print("Mean:", mean)
  
  # Calculate and print the median
  median = np.median(matrix)
  print("Median:", median)
  
  # Calculate and print the standard deviation
  std = np.std(matrix)
  print("Standard deviation:", std)

# Call the matrix calculator function
matrix_calculator()

import numpy as np

def solve_system(coefficients, constants):
  # Convert the input to numpy arrays
  coefficients = np.array(coefficients)
  constants = np.array(constants)
  
  # Check if the number of equations is equal to the number of variables
  if coefficients.shape[0] != constants.shape[0]:
    print("Error: The number of equations must be equal to the number of variables.")
    return
  
  # Solve the system of equations
  solution = np.linalg.solve(coefficients, constants)
  
  # Print the solution
  print("Solution:", solution)
  
# Example usage
coefficients = [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
constants = [8, 9, 10]
solve_system(coefficients, constants)

import math

def calculator():
  # Prompt the user to enter an expression
  expression = input("Enter an expression (e.g. 2 + 3, 4 * 5, 6 ** 2): ")
  
  # Evaluate the expression and print the result
  result = eval(expression)
  print("Result:", result)

# Call the calculator function
calculator()

###

import numpy as np
import math

def main():
  print("1. Matrix calculator")
  print("2. Linear equation solver")
  print("3. Calculator")
  print("4. Quit")
  choice = input("Enter your choice: ")
  if choice == "1":
    matrix_calculator()
  elif choice == "2":
    solve_system(input("Enter the coefficient matrix: "), input("Enter the constant vector: "))
  elif choice == "3":
    calculator()
  elif choice == "4":
    return
  else:
    print("Invalid choice. Please try again.")

def matrix_calculator():
  matrix = np.array(input("Enter a matrix in the form [[a, b, c], [d, e, f], [g, h, i]]: "))
  print("Matrix:")
  print(matrix)
  print("Determinant:", np.linalg.det(matrix))
  print("Inverse:")
  print(np.linalg.inv(matrix))
  print("Transpose:")
  print(np.transpose(matrix))
  print("Mean:", np.mean(matrix))
  print("Median:", np.median(matrix))
  print("Standard deviation:", np.std(matrix))

def solve_system(coefficients, constants):
  coefficients = np.array(coefficients)
  constants = np.array(constants)
  if coefficients.shape[0] != constants.shape[0]:
    print("Error: The number of equations must be equal to the number of variables.")
    return
  print("Solution:", np.linalg.solve(coefficients, constants))

def calculator():
  print("Result:", eval(input("Enter an expression (e.g. 2 + 3, 4 * 5, 6 ** 2): ")))

main()
