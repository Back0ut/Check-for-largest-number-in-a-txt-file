import os
import tkinter as tk
from tkinter import filedialog, messagebox

def find_largest_number(filename):
    error_count = 0
    largest_number = None

    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    number = float(line.strip())
                    
                    if largest_number is None or number > largest_number:
                        largest_number = number
                
                except ValueError:
                    error_count += 1
                    print(f'Error occurred while processing line "{line.strip()}" at line {line_number}: Invalid number format')
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as err:
        print(f"An error occurred: {err}")

    if largest_number is not None:
        return largest_number

    print(f"No valid numbers found in the file '{filename}'.")
    
    if error_count > 0:
        print(f"Total number of errors: {error_count}")

def find_smallest_number(filename):
    error_count = 0
    smallest_number = None

    try:
        with open(filename, 'r') as file:
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

    print(f"No valid numbers found in the file '{filename}'.")
    
    if error_count > 0:
        print(f"Total number of errors: {error_count}")

midPoint = lambda x, y: (x + y) / 2
Average = lambda *nums: sum(nums) / len(nums) if nums else 0

def select_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    
    if filename:
        process_file(filename)

def process_file(filename):
    largest, smallest = find_largest_number(filename), find_smallest_number(filename)
    
    if largest is not None and smallest is not None:
        midpoint = midPoint(largest, smallest)
        average = Average(smallest, largest)
        
        result_text = f'Largest Number: {largest}\nSmallest Number: {smallest}\nMidpoint Between Largest and Smallest Number: {midpoint}\nAverage Between Largest and Smallest Number: {average}'
        result_label.config(text=result_text)
    
    else:
        messagebox.showerror("Error", "No valid numbers found in the file.")

root = tk.Tk()
root.title("Number Processor")

frame = tk.Frame(root)
frame.pack(pady=20)

select_button = tk.Button(frame, text="Select File", command=select_file)
select_button.pack()

result_label = tk.Label(frame, text="", justify="left")
result_label.pack(pady=20)

root.mainloop()
