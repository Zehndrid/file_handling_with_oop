class NumberSeparator:

    def __init__(self, input_file):
        self.input_file = input_file

        def separate_and_save(self, even_file, odd_file):
            try:
                with open(self.input_file, 'r') as file:
                all_numbers = [int(line.strip()) for line in file if line.strip().lstrip('-').isdigit()]

                with open(even_file, 'w') as file_even, open(odd_file, 'w') as file_odd:
