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

    
print("AFTER IF STATEMENT")
print("This is a test file for AST parsing.")
# Did this for a reason, Wanted to ensure that the output from AST parsion was ordered by top to bottom just for confirmaation sake