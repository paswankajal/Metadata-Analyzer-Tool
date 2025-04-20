import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import exifread
import PyPDF2
import docx
import os

def extract_metadata(filepath):
    metadata = {}
    ext = os.path.splitext(filepath)[1].lower()

    if ext in ['.jpg', '.jpeg', '.png']:
        try:
            with open(filepath, 'rb') as f:
                tags = exifread.process_file(f)
                metadata = {tag: str(value) for tag, value in tags.items()}
        except Exception as e:
            metadata = {"Error": str(e)}

    elif ext == '.pdf':
        try:
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                metadata = {key: str(value) for key, value in reader.metadata.items()}
        except Exception as e:
            metadata = {"Error": str(e)}

    elif ext == '.docx':
        try:
            doc = docx.Document(filepath)
            props = doc.core_properties
            metadata = {
                "Title": props.title,
                "Author": props.author,
                "Created": str(props.created),
                "Last Modified By": props.last_modified_by
            }
        except Exception as e:
            metadata = {"Error": str(e)}
    else:
        metadata = {"Error": "Unsupported file type"}

    return metadata

def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[
        ("Supported files", "*.jpg *.jpeg *.png *.pdf *.docx"),
        ("All files", "*.*")
    ])
    result_area.delete(1.0, tk.END)
    for path in file_paths:
        result_area.insert(tk.END, f"Metadata for: {os.path.basename(path)}\n")
        data = extract_metadata(path)
        for k, v in data.items():
            result_area.insert(tk.END, f"{k}: {v}\n")
        result_area.insert(tk.END, "\n" + "-"*50 + "\n\n")

def export_report():
    metadata_text = result_area.get("1.0", tk.END)
    if metadata_text.strip():
        save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if save_path:
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(metadata_text)
            messagebox.showinfo("Export", "Report exported successfully.")
    else:
        messagebox.showwarning("Export", "No metadata to export.")

# GUI
root = tk.Tk()
root.title("Metadata Analyzer Tool")
root.geometry("700x600")

tk.Label(root, text="📸 Metadata Analyzer Tool", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Button(root, text="📂 Browse Files", command=browse_files, width=30, bg="#4CAF50", fg="white").pack(pady=10)

result_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
result_area.pack(pady=10)

tk.Button(root, text="💾 Export Report", command=export_report, width=30, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
