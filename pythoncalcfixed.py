import numpy as np
import ast

def matrix_calculator():
    try:
        matrix_str = input("Enter a matrix (e.g. [[1,2,3],[4,5,6],[7,8,9]]): ")
        matrix_list = ast.literal_eval(matrix_str)  # safely parse input
        matrix = np.array(matrix_list)
    except:
        print("Invalid input! Please enter a proper 2D matrix.")
        return

    if matrix.ndim != 2:
        print("Error: The input must be a 2D matrix!")
        return

    print("\nMatrix:")
    print(matrix)

    try:
        det = np.linalg.det(matrix)
        print("\nDeterminant:", det)
    except np.linalg.LinAlgError:
        print("\nCannot compute determinant.")

    if np.linalg.det(matrix) != 0:
        print("\nInverse:")
        print(np.linalg.inv(matrix))
    else:
        print("\nMatrix is singular, inverse does not exist.")

    print("\nTranspose:")
    print(matrix.T)

    print("\nMean:", np.mean(matrix))
    print("Median:", np.median(matrix))
    print("Standard deviation:", np.std(matrix))


def solve_system():
    try:
        coeff_str = input("Enter the coefficient matrix (e.g. [[2,3,4],[3,4,5],[4,5,6]]): ")
        const_str = input("Enter the constant vector (e.g. [8,9,10]): ")
        coefficients = np.array(ast.literal_eval(coeff_str))
        constants = np.array(ast.literal_eval(const_str))
    except:
        print("Invalid input!")
        return

    if coefficients.shape[0] != constants.shape[0]:
        print("Error: Number of equations must match number of variables.")
        return

    try:
        solution = np.linalg.solve(coefficients, constants)
        print("\nSolution:", solution)
    except np.linalg.LinAlgError as e:
        print("Cannot solve system:", e)


def calculator():
    try:
        expr = input("Enter an expression (e.g. 2 + 3, 4 * 5, 6 ** 2): ")
        result = eval(expr)
        print("Result:", result)
    except:
        print("Invalid expression!")


def main():
    while True:
        print("\nMenu:")
        print("1. Matrix calculator")
        print("2. Linear equation solver")
        print("3. Calculator")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            matrix_calculator()
        elif choice == "2":
            solve_system()
        elif choice == "3":
            calculator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
