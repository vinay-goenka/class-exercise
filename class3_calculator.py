import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    parser = argparse.ArgumentParser(description='Simple calculator')
    parser.add_argument('--a', '-a', type=float, required=True, help='First number')
    parser.add_argument('--b', '-b', type=float, required=True, help='Second number')
    parser.add_argument(
        "--operation", "-op", choices=["add", "subtract", "multiply"], default="add", help="Operation to perform"
    )
    args = parser.parse_args()
    result = 0.0
    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = multiply(args.a, args.b)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()

