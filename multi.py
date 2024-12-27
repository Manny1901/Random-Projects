import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sympy import symbols, Eq, solve
from math import factorial

def main_menu():
    print("\nWelcome to the Multifunction Program!")
    print("Here’s what I can do:")
    print("1. Basic Chatbot")
    print("2. Display Date and Time")
    print("3. Graphing Calculator")
    print("4. Solve Equations (up to cubic)")
    print("5. Permutation and Combination Calculator")
    print("6. Exit")
    print()

# Function for the basic chatbot
def chatbot():
    print("\nChatbot: Hi! I’m your friendly chatbot. Type 'exit' to leave our chat.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Take care!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I’m Chatbot! What’s yours?")
        else:
            print("Chatbot: I’m sorry, I didn’t quite get that. Can you rephrase?")

# Function to display date and time
def show_date_time():
    now = datetime.now()
    print(f"\nThe current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Function for graphing calculator
def graphing_calculator():
    print("\nGraphing Calculator")
    print("Enter a mathematical function of x (e.g., x**2 + 3*x - 5): ")
    func = input("f(x) = ")
    x = np.linspace(-10, 10, 500)  # Create an array of x values
    try:
        y = eval(func)  # Evaluate the function
        plt.plot(x, y, label=f"f(x) = {func}")
        plt.title("Graph of f(x)")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error in graphing: {e}")

# Function to solve equations
def solve_equation():
    print("\nEquation Solver (up to cubic equations)")
    degree = int(input("Enter the degree of the equation (1, 2, or 3): "))
    x = symbols('x')
    if degree == 1:
        print("Enter the coefficients for ax + b = 0:")
        a = float(input("a: "))
        b = float(input("b: "))
        equation = Eq(a*x + b, 0)
    elif degree == 2:
        print("Enter the coefficients for ax^2 + bx + c = 0:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        equation = Eq(a*x**2 + b*x + c, 0)
    elif degree == 3:
        print("Enter the coefficients for ax^3 + bx^2 + cx + d = 0:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = float(input("d: "))
        equation = Eq(a*x**3 + b*x**2 + c*x + d, 0)
    else:
        print("Unsupported degree. Only 1, 2, or 3 are allowed.")
        return
    solutions = solve(equation, x)
    print(f"The solutions are: {solutions}")

# Function for permutation and combination calculator
def permutation_combination():
    print("\nPermutation and Combination Calculator")
    print("Choose an option:")
    print("1. Permutation")
    print("2. Combination")
    choice = int(input("Your choice: "))
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    if choice == 1:
        result = factorial(n) // factorial(n - r)
        print(f"Permutation P({n}, {r}) = {result}")
    elif choice == 2:
        result = factorial(n) // (factorial(r) * factorial(n - r))
        print(f"Combination C({n}, {r}) = {result}")
    else:
        print("Invalid choice. Please select 1 or 2.")

# Main program loop
def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            chatbot()
        elif choice == '2':
            show_date_time()
        elif choice == '3':
            graphing_calculator()
        elif choice == '4':
            solve_equation()
        elif choice == '5':
            permutation_combination()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
