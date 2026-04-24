# Square even numbers and cube odd numbers
class NumberProcessor: 

    # Set input file
    def __init__(self, input_file):
        self.input_file = input_file
    # Calculate and save to files
    def process_and_save(self, double_file, triple_file):
        try:
            # Read integers from file
            with open(self.input_file, 'r') as file:
                all_numbers = [int(line.strip()) for line in file if line.strip().lstrip('-').isdigit()]

            # Open output files
            with open(double_file, 'w') as file_double, open(triple_file, 'w') as file_triple:
                # Sort and calculate
                for number in all_numbers:
                    if number % 2 == 0:
                        file_double.write(f"{number ** 2}\n")
                    else:
                        file_triple.write(f"{number ** 3}\n")
                        
            print("Success! Math completed and saved.")

        except FileNotFoundError:
            # Handle missing file
            print("Error: Source file missing.")

if __name__ == "__main__":
    # Run the processor
    processor = NumberProcessor("integers.txt")
    processor.process_and_save("double.txt", "triple.txt")