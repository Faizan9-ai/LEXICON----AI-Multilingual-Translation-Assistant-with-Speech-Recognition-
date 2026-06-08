
from pypdf import PdfReader
from docx import Document


def read_txt(file):
    return file.read().decode("utf-8")


def read_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def read_docx(file):
    document = Document(file)
    return "\n".join([para.text for para in document.paragraphs])


def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return read_txt(uploaded_file)

    elif file_name.endswith(".pdf"):
        return read_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return read_docx(uploaded_file)

    else:
        raise ValueError("Unsupported file type")