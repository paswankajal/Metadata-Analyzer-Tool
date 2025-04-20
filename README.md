# 📸 Metadata Analyzer Tool

The **Metadata Analyzer Tool** is a Python-based desktop application that extracts and displays metadata from various file types using a simple graphical user interface. Whether you're working in digital forensics, research, or data inspection, this tool can help you uncover hidden file information easily.

---

## 🚀 Features

- ✅ Browse and select multiple files
- 🔍 Extract metadata from:
  - Images (`.jpg`, `.jpeg`, `.png`) – via `exifread`
  - PDF documents (`.pdf`) – via `PyPDF2`
  - Word documents (`.docx`) – via `python-docx`
- 🖥️ Clean, scrollable text area to display extracted metadata
- 💾 Export metadata reports as `.txt` files

---

## 🛠️ Tech Stack

- Python 3
- Tkinter (GUI)
- exifread
- PyPDF2
- python-docx

---

## 📦 Installation

1. **Clone this repository**

```bash
git clone https://github.com/paswankajal/metadata-analyzer-tool.git
cd metadata-analyzer-tool
```

bash
````
pip install exifread PyPDF2 python-docx
````

bash
python app.py
📥 Supported File Types

File Type	Extensions	Metadata Extracted From
Image	.jpg, .jpeg, .png	EXIF tags
PDF	.pdf	PDF metadata
Word Doc	.docx	Core document properties

💡 Future Improvements
Add support for more file formats (e.g., .mp4, .xlsx)

Drag-and-drop functionality

Dark mode theme

Export as .csv or .json

👩‍💻 Author
Kajal Kumari
B.Tech CSE | Sant Baba Bhag Singh University
🌐 Passionate about digital forensics, Python, and clean UI/UX design














