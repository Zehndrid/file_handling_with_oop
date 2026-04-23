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
                # Check each student 
                for line in file:
                    parts = line.strip().split(',')
                    
                    if len(parts) == 2:
                        student_name = parts[0].strip()
                        current_gwa = float(parts[1].strip())

                        # Update top student if current GWA is higher
                        if current_gwa > highest_gwa:
                            highest_gwa = current_gwa
                            top_student = student_name
            # Print the result
            print(f"Top Student: {top_student} with GWA: {highest_gwa}")

        except FileNotFoundError:
            # Handle missing file error
            print("Error: Student file not found.")

if __name__ == "__main__":
    # Run the GWA evaluator
    evaluator = StudentGwaEvaluator("student_and_gwa.txt")
    evaluator.find_highest_gwa()

 
     