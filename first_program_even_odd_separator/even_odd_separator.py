# seperate even and odd numbers from a file 
class NumberSeparator:
    # set input file as an instance variable
    def __init__(self, input_file):
        self.input_file = input_file
        # Read numbers and save to separate files
    def separate_and_save(self, even_file, odd_file):
            try:
                # Read file and convert lines to integers
                with open(self.input_file, 'r') as file:
                     all_numbers = [int(line.strip()) for line in file if line.strip().lstrip('-').isdigit()]
                # Open output files and write even and odd numbers
                with open(even_file, 'w') as file_even, open(odd_file, 'w') as file_odd:
                    # Write evens and odds
                    for number in all_numbers:
                         if number % 2 == 0:
                             file_even.write(f"{number}\n")
                         else:
                             file_odd.write(f"{number}\n")
                        
                print("Success! Numbers separated.")
            # Handle missing file error
            except FileNotFoundError:
           
                print("Error: Input file missing.")

if __name__ == "__main__":
    # Run the separator
    separator = NumberSeparator("even_and_odd_numbers.txt")
    separator.separate_and_save("even_numbers.txt", "odd_numbers.txt")