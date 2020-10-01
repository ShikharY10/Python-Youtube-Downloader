from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def startdownload():
    global file_size
    
    try:     
        url = urlField.get()
        #changing button text
        dBtn.config(text = "PLease Wait...")
        dBtn.config(state =DISABLED)

        path_video = askdirectory()
        if path_video is None:
            return
        
        # creating youtube object with url...
        ob = YouTube(url,on_progress_callback=progress)
        strm = ob.streams.first()
        file_size = strm.filesize
        title_n_size.config(text = f"{strm.title}  |  {file_size/1000000:{10}} MB")
        title_n_size.pack(side = TOP)
        
        # now downloading the video
        
        strm.download(path_video)
        print("done...")
        dBtn.config(text = "Start Download")
        dBtn.config(state = NORMAL)
        showinfo("Download Finished","Downloaded Successfully")
        urlField.delete(0,END)
        title_n_size.pack_forget()

    except Exception as e:
        print(e)

#this function is called for updating percentage
def progress(chunk=None, file_handle=None, bytes_remaining=None):

    #get the percentage of the file that has been downloading
    file_downloaded = (file_size-bytes_remaining)
    per = ((file_downloaded / file_size) *100)
    dBtn.config(text = "{:00.0f} % Downloaded".format(per))

#setting up the thread
def startdownloadThread():
    thread = Thread(target=startdownload)
    thread.start()
        
#start building gui
main = Tk()

#setting the title
main.title("Youtube Downloader")

#setting the icon
main.iconbitmap("\\Images\\icon.ico")

#Setting the hight abd width of the window
main.geometry("500x600")

#C:\Users\acer\Python\Projects\Youtube_Downloader

#heading icon
file = PhotoImage(file = "\\Images\\download.png")
headingIcon = Label(main,image = file)
headingIcon.pack(side = TOP)

#url textfield
urlField = Entry(main,font = ("verdana",16),justify = CENTER)
urlField.pack(side = TOP, fill = X, padx = 10)

#DOWNLOAD BUTTON
dBtn = Button(main,text = "Start Download", font = ("verdana", 16),relief = "ridge",command = startdownloadThread)
dBtn.pack(side = TOP,pady = 10)

#video title and size
title_n_size = Label(main, text = "")

main.mainloop()
#on_progress_callback=progress