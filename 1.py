import openpyxl

# Function to read conversation from a file and write to Excel
def extract_from_file_and_write_to_excel(file_path):
    # Initialize Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write headers to Excel sheet
    sheet["A1"] = "User"
    sheet["B1"] = "Employee ID"
    sheet["C1"] = "Name"
    sheet["D1"] = "Tech Stack"

    # Read conversation from file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        user_response = lines[1].strip().split(": ")[1]
        employee_id = lines[3].strip().split(": ")[1]
        user_name = lines[5].strip().split(": ")[1]
        tech_stack = lines[7].strip().split(": ")[1]

        # Write responses to Excel sheet
        sheet.append([user_response, employee_id, user_name, tech_stack])

    # Save Excel file
    workbook.save("interview_responses.xlsx")
    print("Interview responses saved to interview_responses.xlsx")

# Specify the path to your text file (user_input.txt)
file_path = "user_input.txt"

# Run the extraction and write to Excel
extract_from_file_and_write_to_excel(file_path)
