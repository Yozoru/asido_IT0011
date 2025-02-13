def is_palindrome(num):
    return str(num) == str(num)[::-1]

def open_file(filename):
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                numbers = [int(n) for n in line.strip().split(',')]
                total_sum = sum(numbers)
                result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
                print(f"Line {i}: {line.strip()} (sum {total_sum}) - {result}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Ensure the file contains only comma-separated numbers.")

open_file("TME/numbers.txt")