# 🧾 PDF Text Extractor with OCR

This is a Python script that extracts **text from scanned or image-based PDF files** using OCR (Optical Character Recognition). Perfect for digitizing PDFs that contain images instead of selectable text.

---

## 📦 Features

- Extracts text from scanned/image PDFs
- Uses Tesseract OCR via `pytesseract`
- Converts PDF pages to images with `pdf2image`
- Saves output to a `.txt` file readable in Notepad

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
https://github.com/UrboyG/textExtractor.git
cd textExtractor
```
2. Create & Activate a Virtual Environment (Recommended)
```bash
python -m venv .venv
.\.venv\Scripts\activate   # For Windows
````
3. Install Dependencies
```bash
pip install -r pytesseract pdf2image Pillow
```
🛠️ Additional Setup
📌 Install Tesseract OCR
Download from: https://github.com/tesseract-ocr/tesseract

Install it (Default path: C:\Program Files\Tesseract-OCR\tesseract.exe)

Make sure to note the installation path

📌 Install Poppler for Windows
Download from: https://github.com/oschwartz10612/poppler-windows/releases

Extract to a folder (e.g., C:\poppler)

Note the path to the bin directory (e.g., C:\poppler\bin)

🧠 How to Use
```bash
python textExtractor.py <your_pdf_file.pdf>
```



