"""THe Most basic Test File
YOU HAVE FUNCTIONS YOU HAVE A MAIN
You have a comparision and parameters but nothing fancy
"""
def main():
    print("Hello, World!")
    print(calculate_sum(2, 3))
    someval = 10
    otherval = "Number"

def calculate_sum(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    main()
    result = calculate_sum(5, 7)
    print(f"The sum is: {result}")
    greeting = greet("Alice")
    print(greeting)
