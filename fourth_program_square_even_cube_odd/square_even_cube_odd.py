# Square even numbers and cube odd numbers
class NumberProcessor: 

    # Set input file
    def __init__(self, input_file):
        self.input_file = input_file
    # Calculate and save to files
    def process_and_save(self, double_file, triple_file):
        try: