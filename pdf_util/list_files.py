import os
import logging

#logging.basicConfig(filename="newfile1.log",
#                    format='%(asctime)s %(message)s',
#                    filemode='w')
logger = logging.getLogger()

def retrieve_all(inputpath):
    try:
        file_list = os.listdir(inputpath)
    except Exception as e:
        logger.exception(e)
    return file_list

def retrieve_pdfs(inputpath):
    try:
        files_list1 = [f for f in os.listdir(inputpath) if f.endswith('.pdf') or f.endswith('.PDF')]
    except Exception as e:
        logger.exception(e)
    return files_list1