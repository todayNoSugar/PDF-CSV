import csv
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_csv(pdf_path, csv_path):
    rsrcmgr = PDFResourceManager()
    output_string = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, output_string, laparams=laparams)
    with open(pdf_path, 'rb') as pdf_file:
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            interpreter.process_page(page)
        text = output_string.getvalue()
    device.close()
    output_string.close()

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in text.split('\n'):
            writer.writerow(line.split(','))

# 示例用法
pdf_path = 'jxgy9stock3p.pdf'
csv_path = 'jxgy9stock3p.csv'
convert_pdf_to_csv(pdf_path, csv_path)