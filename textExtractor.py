import sys
import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Set the Tesseract OCR executable path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"E:\Tessaract_OCR\tesseract.exe"

def ocr_pdf(pdf_path, output_txt_path):
    # Specify the path to the Poppler bin folder
    poppler_path = r"E:\poppler\poppler-24.08.0\Library\bin"  

    # Convert PDF pages to images
    pages = convert_from_path(pdf_path, poppler_path=poppler_path)

    all_text = []

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        all_text.append(text)

    # Save the OCR output to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_text))

    print(f"✅ OCR complete. Text saved to: {output_txt_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python textExtractor.py <file.pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]

    if not os.path.isfile(pdf_file):
        print(f"❌ File not found: {pdf_file}")
        sys.exit(1)

    output_file = os.path.splitext(pdf_file)[0] + "_ocr.txt"
    ocr_pdf(pdf_file, output_file)
