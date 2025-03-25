🧾 PDF Text Extractor with OCR

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
git clone https://github.com/your-username/pdf-text-extractor.git
cd pdf-text-extractor
2. Create & Activate a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv .venv
.\.venv\Scripts\activate   # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt yet, create one with:

nginx
Copy
Edit
pytesseract
pdf2image
Pillow
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
bash
Copy
Edit
python textExtractor.py <your_pdf_file.pdf>
Example:

bash
Copy
Edit
python textExtractor.py p4_test5.pdf
Output will be saved as:

Copy
Edit
p4_test5_ocr.txt
You can also modify the script to automatically open the .txt in Notepad.

📁 Folder Structure
bash
Copy
Edit
pdf-text-extractor/
│
├── textExtractor.py       # Main script
├── README.md              # This file
├── p4_test5.pdf           # Example PDF (add your own)
└── .venv/                 # Virtual environment (optional)
🧯 Troubleshooting
❓ pdfinfo not found or poppler not installed
Make sure you've downloaded Poppler and updated the script with:

python
Copy
Edit
poppler_path = r"C:\path\to\poppler\bin"
❓ tesseract not found
Make sure Tesseract is installed and the path is set:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
📃 License
This project is open-source and free to use. MIT License or add your own license here.

✨ Contributions Welcome
Feel free to submit pull requests or open issues if you want to improve the tool. Happy OCR'ing! 😄
