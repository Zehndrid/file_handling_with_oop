# Write user input to a text file
class LifeStoryWriter:

    # seting an output file
    def __init__(self, output_file):
        self.output_file = output_file

    # Get input and write lines
    def write_lines(self):
        print("Write your story. Type 'STOP' to finish.\n")

        # Open file for writing
        with open(self.output_file, 'w') as file:
            # Loop until user types STOP
            while True:
                user_line = input("> ")
                
                if user_line.upper() == "STOP":
                    break
                # Save line to file
                file.write(f"{user_line}\n")
                
        print("Success! File saved.")