import os
import  PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfReader(file)  # Updated for modern PyPDF2
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""  # Handle None
            return text
        except Exception as e:
            raise Exception(f"Error reading the PDF file: {str(e)}")

    elif file.name.endswith(".txt"):
        try:
            return file.read().decode("utf-8")
        except Exception as e:
            raise Exception(f"Error reading the TXT file: {str(e)}")

    else:
        raise Exception("Unsupported file format. Only .pdf and .txt are supported.")
    

    import json

def get_table_data(quiz_str):
    try:
        # Convert the quiz from a string to a dictionary
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        # Iterate over the quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join([f"{option} -> {option_value}" for option, option_value in value["options"].items()])
            correct = value["correct"]

            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        return False