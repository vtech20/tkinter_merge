import os
import tkinter
from PyPDF2 import PdfFileMerger
import logging

#logging.basicConfig(filename="newfile.log",
#                    format='%(asctime)s %(message)s',
#                    filemode='w')
logger = logging.getLogger()

def merge_pdf_files(inputValue):
    try:
        os.chdir(inputValue)
        merger = PdfFileMerger()
        for item in os.listdir(inputValue):
            if item.endswith('pdf'):
                merger.append(item)
        merger.write("final_pdf.pdf")
        merger.close()
        logger.info("Merged PDFs successfully with name final_pdf.pdf")
        tkinter.messagebox.showinfo("msg","Merge Completed")
    except Exception as e:
        logger.exception(e)