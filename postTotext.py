import fitz # pip install --upgrade pymupdf or pip install PyMuPDF
import re

def postTotext():
    # global doc

    book_path = 'paper_list/001.pdf'

    doc = fitz.open(book_path)

    text = doc.get_page_text(pno=0)

    text = re.sub(r"\s+", " ", text)
    # print(text,"++++++++++++++++++++++++++++ 3")
    text = text.replace('THIRD CONCEPT, NOVEMBER 2020', '').strip()
    text = ' '.join(text.split(' ')[1:])

    print(text)

    return text

postTotext()

