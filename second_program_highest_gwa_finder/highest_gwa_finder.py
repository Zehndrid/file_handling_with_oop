# Find student with the highest GWA
class StudentGwaEvaluator:
    
    # Setting a target file
    def __init__(self, file_path):
        self.file_path = file_path

    # Find and print the top student with the highest GWA
    def find_highest_gwa(self):
        highest_gwa = -1.0
        top_student = ""

        try:
            # Read student file
            with open(self.file_path, 'r') as file:
                

     