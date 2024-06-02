import os

def find_largest_number(filename):
    error_count = 0
    largest_number = None
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    number = float(line.strip())
                    if largest_number is None or number > largest_number: largest_number = number
                    
                except ValueError:
                    error_count += 1
                    print(f'Error occurred while processing line "{line.strip()}" at line {line_number}: Invalid number format')

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as err:
        print(f"An error occurred: {err}")

    if largest_number is not None:
        return largest_number
    
    else:
        print(f"No valid numbers found in the file '{filename}'.")

    if error_count > 0: print(f"Total number of errors: {error_count}")

def find_smallest_number(filename):
    error_count = 0
    smallest_number = None
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    number = float(line.strip())
                    
                    if smallest_number is None or number < smallest_number:
                        smallest_number = number
                
                except ValueError:
                    error_count += 1
                    print(f'Error occurred while processing line "{line.strip()}" at line {line_number}: Invalid number format')

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as err:
        print(f"An error occurred: {err}")

    if smallest_number is not None:
        return smallest_number
    
    else:
        print(f"No valid numbers found in the file '{filename}'.")

    if error_count > 0:
        print(f"Total number of errors: {error_count}")

def midPoint(num1, num2):
    return (num1 + num2) / 2

if __name__ == '__main__':
    largest, smallest = find_largest_number('numbers.txt'), find_smallest_number('numbers.txt')
    midpoint = midPoint(largest, smallest)
    
    if largest is not None and smallest is not None:
        print(f'Largest Number: {largest}\nSmallest Number: {smallest}\nMidpoint Between Largest and Smallest Number: {midpoint}')
