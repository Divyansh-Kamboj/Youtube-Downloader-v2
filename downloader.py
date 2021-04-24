import tkinter
from pytube import YouTube
 
root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Downloader v2")
 
 
tkinter.Label(root, text ='Youtube Video Downloader', font ='Comic 20 bold').pack()
 
link = tkinter.StringVar()
 
tkinter.Label(root, text ='Paste Your Link Below:', font ='Comic 15 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)


def Downloader():
    
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='DOWNLOADED!!', font ='Comic 15').place(x= 180, y = 210)
 
 
tkinter.Button(root, text ='DOWNLOAD HERE', font ='Comic 20 bold', bg ='purple', padx = 2, command = Downloader).place(x=120, y = 150)
 
 
 
root.mainloop()