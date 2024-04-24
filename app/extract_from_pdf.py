import streamlit as st
from PyPDF2 import PdfReader

def Extract_From_PDF(): 
    print('Upload the PDF file to extract the text from it.')
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
    if uploaded_file is not None:
        pdf = PdfReader(uploaded_file)
        extracted_text = ''
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            extracted_text += page.extract_text()
            st.write(page.extract_text())
    # in future increase the file size
        print()
if __name__ == "__main__":
    Extract_From_PDF()