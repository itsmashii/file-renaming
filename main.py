import os
from PyPDF2 import PdfReader

def extract_filename_from_pdf(pdf_file_path):
    try:
        with open(pdf_file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            if len(pdf_reader.pages) > 0:
                first_page_text = pdf_reader.pages[0].extract_text()
                # Extract the desired filename from the content (assuming it's in a specific format)
                # For example, if the filename is the first line of the PDF content:
                filename = first_page_text.splitlines()[18].strip()
                return filename
    except Exception as e:
        print(f"Error: {e}")
    return None

def rename_and_save_pdf(original_pdf_path, renamed_pdf_folder):
    filename = extract_filename_from_pdf(original_pdf_path)
    if filename:
        renamed_pdf_path = os.path.join(renamed_pdf_folder, f"{filename}.pdf")
        try:
            # Copy the original PDF to the renamed folder with the extracted filename
            with open(original_pdf_path, 'rb') as original_file, open(renamed_pdf_path, 'wb') as renamed_file:
                renamed_file.write(original_file.read())
            print(f"PDF '{original_pdf_path}' renamed and saved as '{filename}.pdf' in 'renamedpdf' folder.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Failed to extract filename from '{original_pdf_path}'.")

# Example usage
if __name__ == "__main__":
    original_pdf_folder = r"C:\Users\Lenovo\Documents\Projects\QMS Certificate\certs\originalpdf"  # Path to the originalpdf folder (relative to the script)
    renamed_pdf_folder = r"C:\Users\Lenovo\Documents\Projects\QMS Certificate\certs\renamedpdf"  # Path to the renamedpdf folder (relative to the script)

    # Iterate through the PDF files in the originalpdf folder
    for filename in os.listdir(original_pdf_folder):
        if filename.endswith(".pdf"):
            original_pdf_path = os.path.join(original_pdf_folder, filename)
            rename_and_save_pdf(original_pdf_path, renamed_pdf_folder)