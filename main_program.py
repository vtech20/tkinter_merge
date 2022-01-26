import tkinter
import logging
from merge_files.merge_pdf import merge_pdf_files
import pdf_util.list_files
import os


logging.basicConfig(level=logging.DEBUG,filename="newfile2.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')




def display_pdf(win1,inputValue):
    try:
        files = pdf_util.list_files.retrieve_pdfs(inputValue)
        label2 = tkinter.Label(win1,text="PDF Files")
        label2.place(x=200, y=100)
        lbox1 = tkinter.Listbox(win1, height=10, width = 30)
        lbox1.place(x=200, y=120)
        for item in files:
            lbox1.insert(tkinter.END, item)
        buttonMerge= tkinter.Button(win1, height=1, width=10, text="Merge Files",
                    command=lambda: merge_pdf_files(inputValue))
        buttonMerge.place(x=100,y=300)
        
    except Exception as e:
        logging.exception(e)


def display_lbox_all(win1):
    try:
        inputvalue = textBox.get("1.0", "end-1c")
        isDirectory = os.path.isdir(inputvalue)
        if isDirectory == True:
            flist = pdf_util.list_files.retrieve_all(inputvalue)
            label1 = tkinter.Label(win1, text="All Files")
            label1.place(x=10, y=100)
            lbox = tkinter.Listbox(win1, height=10, width=30)
            lbox.place(x=10, y=120)
            for item in flist:
                lbox.insert(tkinter.END, item)
            display_pdf(win1, inputvalue)
        else:
            tkinter.messagebox.showinfo("msg","The input provided is not a directory")
    except Exception as e:
        logging.exception(e)

try:
    # WINDOW CREATION
    win = tkinter.Tk()
    geo = win.geometry
    geo("400x400+400+400")

    label_file_explorer = tkinter.Label(win,
                            text = "Enter the path to list the file",
                            width = 100, height = 1,fg = "blue")

    label_file_explorer.pack()
    textBox=tkinter.Text(win, height=2, width=100)
    textBox.pack()
    buttonCommit = tkinter.Button(win, height=1, width=10, text="List",command=lambda: display_lbox_all(win))
    buttonCommit.pack()
    win.mainloop()
    logging.info("Successfully done")
except Exception as e:
    logging.exception(e)