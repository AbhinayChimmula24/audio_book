# import streamlit as st
import sys
from PyPDF2 import PdfReader
import re
from pdfminer.high_level import extract_text


def Extract_From_PDF(pdf_path, start_text, end_text):
    pdf_path = pdf_path.strip("'\"")
    if pdf_path:
        from_pdfMiner = extract_text(pdf_path)
        if start_text and start_text in from_pdfMiner:
            start_index = from_pdfMiner.index(start_text)
        else:
            start_index = 0
        if end_text and end_text in from_pdfMiner:
            end_index = from_pdfMiner.index(end_text) + len(end_text)
        else:
            end_index = len(from_pdfMiner)
        return from_pdfMiner[start_index:end_index]
    return ""
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


# if __name__ == "__main__":
#     text_processing("LESSON 1: THE RICH DON’T",
#                     "LESSON 2: WHY TEACH FINANCIAL LITERACY?")
if __name__ == "__main__":
    pdf_path = input("Please enter the path to the PDF file: ")
    start_text = input("Please enter the starting text: ")
    end_text = input("Please enter the ending text: ")
    extracted_text = Extract_From_PDF(pdf_path, start_text, end_text)
    print(extracted_text)