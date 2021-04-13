import os
from gtts import gTTS
from googletrans import Translator
import PyPDF2
from pygame import mixer 
from pathlib import Path
import tkinter
from tkinter import *
from tkinter import ttk
import threading

if __name__ == "__main__":
    def startPlay(fileName):
        mixer.music.load(fileName)
        mixer.music.set_volume(0.7)
        mixer.music.play()
        label.place(x = 90, y = 270)
        step()
        strVar.set('Success! Your Audiobook is now available.')

    def conversion(filePath, fileName):
        languageSelection = str(languageDrop.get())
        step()
        audioBook = open(filePath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(audioBook)
        mytext = pageRange(pdfReader)
        if languageSelection == 'Spanish':
            result = translator.translate(mytext, src='en', dest='es')
            tts = gTTS(text=result.text, lang='es')
        else:
            tts = gTTS(text=mytext, lang='en')
        try:
            step()
            tts.save(fileName)
            step()
            startPlay(fileName)
        except:
            label.place(x = 101, y = 270)
            strVar.set('File names can\'t contain < > | / \ ? " * :')
            gui.after(2000, clearEr)
            gui.after(4000, defaultMsg)

    def pageRange(pdfReader):
        mytext = ''
        page1 = int(pageRangeEntry1.get())
        page1Offset = page1 - 1
        page2 = int(pageRangeEntry2.get())
        step()
        for pageNum in range(page1Offset, page2):
            pageObj = pdfReader.getPage(pageNum)
            mytext += pageObj.extractText()
        return mytext

    def blankField():
        label.place(x = 130, y = 270)
        strVar.set('Fields cannot be left empty.')
        gui.after(2000, clearEr)
        gui.after(4000, defaultMsg)

    def testNegative():
        page1Int = int(pageRangeEntry1.get())
        page2Int = int(pageRangeEntry2.get())
        if page1Int <= 0 or page1Int >= page2Int:
            raise ValueError
        elif page2Int <= 0:
            raise ValueError

    def prtException():
        label.place(x = 150, y = 270)
        strVar.set('Invalid page ranges.')
        gui.after(2000, clearEr)
        gui.after(4000, defaultMsg)

    def formatError():
        label.place(x = 128, y = 270)
        strVar.set('PDF not formatted correctly.')
        gui.after(2000, clearEr)
        gui.after(4000, defaultMsg)

    def nonIntPageRange():
        try:
            page1Int = int(pageRangeEntry1.get())
            page2Int = int(pageRangeEntry2.get())
        except:
            prtException()
        
    def start():
        resetBar()
        try:
            if len(bookEntry.get()) == 0:
                blankField()
            elif len(saveAsEntry.get()) == 0:
                blankField()
            elif len(pageRangeEntry1.get()) == 0:
                blankField()
            elif len(pageRangeEntry2.get()) == 0:
                blankField()
            else:
                testNegative()
                var = bookEntry.get() + '.pdf'
                filePath = Path.home()/var
                fileName = saveAsEntry.get() + '.mp3'
                step()
                conversion(filePath, fileName)
        except ValueError:
            prtException()
        except AssertionError:
            formatError()
        except:
            label.place(x = 150, y = 270)
            strVar.set("PDF file not found.")
            nonIntPageRange()
            gui.after(2000, clearEr)
            gui.after(4000, defaultMsg)
    def clearEr():
        label.place(x = 160, y = 270)
        strVar.set("Please try again.")
        resetBar()

    def defaultMsg():
        label.place(x = 40, y = 270)
        strVar.set("Successful conversion will take a few moments to complete.")

    def step():
        progBar['value'] += 20

    def resetBar():
        progBar['value'] = 0

    def pause():
        mixer.music.pause()

    def resume():
        mixer.music.unpause() 

    def exitProgram():
        gui.destroy()

    translator = Translator()
    mixer.init()
    gui = tkinter.Tk()
    gui.title("PDF to Audiobook")
    canvas = Canvas(gui, width=400, height=350, bg = 'gray11')
    canvas.pack(fill=BOTH,expand=YES)

    options = ["English","Spanish"]

    bookLabelTxt = StringVar()
    bookLabelTxt.set("PDF Name: ")
    bookLabel = Label(gui, textvariable = bookLabelTxt, relief = FLAT, fg = 'white', bg = 'gray11')
    bookLabel.place(x = 15, y = 20)
    bookEntry = tkinter.Entry(gui, bg = 'gray31', fg = 'white')
    bookEntry.place(x = 80, y = 20)

    saveAsTxt = StringVar()
    saveAsTxt.set("Save File Name: ")
    saveAsLabel = Label(gui, textvariable=saveAsTxt, relief = FLAT, fg = 'white', bg = 'gray11')
    saveAsLabel.place(x = 15, y = 55)
    saveAsEntry = tkinter.Entry(gui, bg = 'gray31', fg = 'white')
    saveAsEntry.place(x = 105, y = 55)

    pageRangeTxt1 = StringVar()
    pageRangeTxt1.set("Starting Page: ")
    pageRangeLabel1 = Label(gui, textvariable=pageRangeTxt1, relief = FLAT, fg='white', bg='gray11')
    pageRangeLabel1.place(x = 15, y = 90)
    pageRangeEntry1 = tkinter.Entry(gui, bg = 'gray31', fg = 'white')
    pageRangeEntry1.place(x = 95, y = 90, width = 40)

    pageRangeTxt2 = StringVar()
    pageRangeTxt2.set("Ending Page: ")
    pageRangeLabel2 = Label(gui, textvariable=pageRangeTxt2, relief = FLAT, fg='white', bg='gray11')
    pageRangeLabel2.place(x = 15, y = 125)
    pageRangeEntry2 = tkinter.Entry(gui, bg = 'gray31', fg = 'white')
    pageRangeEntry2.place(x = 90, y = 125, width = 40)

    languageTxt = StringVar()
    languageTxt.set("Language: ")
    language = Label(gui, textvariable=languageTxt, relief = FLAT, fg='white', bg='gray11')
    language.place(x = 15, y = 160)
    languageDrop = StringVar()
    languageDrop.set(options[0])
    languageMenu = OptionMenu(gui, languageDrop, *options)
    languageMenu.config(bg='gray31', fg='white')
    languageMenu["menu"].config(bg="gray31", activebackground='gray11')
    languageMenu["highlightthickness"]=0
    languageMenu.place(x = 80, y = 157)

    style = ttk.Style()
    style.theme_use('default')
    style.configure('gray11.Horizontal.TProgressbar', background='gray31', foreground='gray31', troughcolor='gray11')

    progBar = ttk.Progressbar(gui, orient=HORIZONTAL, length=350, mode='determinate', style='gray11.Horizontal.TProgressbar')
    progBar.place(x=27, y=320)
    progBarLabelTxt = StringVar()
    progBarLabelTxt.set("Conversion Progress:")
    progLabel = Label(gui, textvariable = progBarLabelTxt, relief = FLAT, fg = 'white', bg = 'gray11')
    progLabel.place(x = 145, y = 295)

    convertButton = tkinter.Button(gui, text = "Convert", command=lambda:threading.Thread(target=start).start(), fg = 'white', bg = 'gray31', padx = 15)
    convertButton.place(x = 20, y = 235)

    pauseButton = tkinter.Button(gui, text = "Pause", command=pause, fg = 'white', bg = 'gray31', padx = 15)
    pauseButton.place(x = 120, y = 235)

    resumeButton = tkinter.Button(gui, text = "Resume", command=resume, fg = 'white', bg = 'gray31', padx = 15)
    resumeButton.place(x = 210, y = 235)

    exitButton = tkinter.Button(gui, text = "Exit", command=exitProgram, fg = 'white', bg = 'gray31', padx = 25)
    exitButton.place(x = 310, y = 235)

    strVar = StringVar()
    label = Label(gui, textvariable=strVar, relief=RAISED, fg='white', bg='gray11')
    strVar.set("Successful conversion will take a few moments to complete.")
    label.place(x = 40, y = 270)

    gui.mainloop()