# Must be in the same folder
import PyPDF2

def split_pdf(input_path):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)

        for page_num in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])

            output_path = f'page_{page_num + 1}.pdf'
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf = 'CertOfParticipation.pdf'  # Replace with your input PDF file
    split_pdf(input_pdf)
