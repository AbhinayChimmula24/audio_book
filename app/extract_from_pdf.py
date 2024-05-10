# import streamlit as st
from PyPDF2 import PdfReader

def Extract_From_PDF(): 
    pdf_path = "/Users/achimmula/Desktop/books_to_convert/NIPS-2017-attention-is-all-you-need-Paper.pdf"
    if pdf_path:
        pdf = PdfReader(pdf_path)
        extracted_text = ''
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            extracted_text += page.extract_text()
            with open('/Users/achimmula/Desktop/extracted_text.txt', 'w') as f:
                f.write(extracted_text)
    return extracted_text
    # in future increase the file size
    # take this text and pass it to the ollama api or to the speech generator 

if __name__ == "__main__":
    Extract_From_PDF()