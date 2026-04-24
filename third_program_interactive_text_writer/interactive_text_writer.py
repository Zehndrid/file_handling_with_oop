# Write user input to a text file
class LifeStoryWriter:

    # seting an output file
    def __init__(self, output_file):
        self.output_file = output_file

    # Get input and write lines
    def write_lines(self):
        print("Write your story. Type 'STOP' to finish.\n")