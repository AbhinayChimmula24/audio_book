# import streamlit as st
from PyPDF2 import PdfReader
import re


def Extract_From_PDF():
    pdf_path = "/Users/achimmula/Desktop/books_to_convert/Rich Dad Poor Dad.pdf"
    if pdf_path:
        pdf = PdfReader(pdf_path)
        extracted_text = ''
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            extracted_text += page.extract_text()
    return extracted_text
    # in future increase the file size
    # take this text and pass it to the ollama api or to the speech generator


def text_processing(starting_text, ending_text=None):
    text = Extract_From_PDF()
    text = text.replace('\n', ' ')

    text = re.sub(r'(\.) ', r'\1\n', text)
    text = re.sub(r'(\?) ', r'\1\n', text)
    text = re.sub(r'(\") ', r'\1\n', text)

    parts = text.split(starting_text)

    if len(parts) > 1:

        ending_parts = parts[1].split(ending_text)

        if len(ending_parts) > 1:
            selected_text = starting_text + ending_parts[0]
        else:
            selected_text = starting_text + parts[1]
    else:
        selected_text = text

        with open('/Users/achimmula/Desktop/starting_c1.txt', 'w') as f:
            f.write(selected_text)
        return selected_text


if __name__ == "__main__":
    text_processing("LESSON 1: THE RICH DON’T",
                    "LESSON 2: WHY TEACH FINANCIAL LITERACY?")
