import PySimpleGUI as sg
import easygui
import pyttsx3
import PyPDF2
sg.theme('BluePurple')
pagenum = "null"
cop= 'currently on page :' + pagenum
layout = [[sg.Text('currently on page :'), sg.Text(size=(15,1), key='-PAGENUM-')],
          [sg.Text("enter page num to read from :")],[sg.InputText(key='-IN-')],
          [sg.Button('select pdf file'), sg.Button('start reading')],]

window = sg.Window('pdf reader', layout)
def read_page(myfile,pagenum):
    book = open(myfile, "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print("there are ",pages," pages")
    for num in range(int(pagenum),pages):
        window['-PAGENUM-'].update(num)
        window.refresh()
        speaker = pyttsx3.init()
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
        print("page read")
while True:  # Event Loop
    event , values = window.read()

    if values['-IN-'] == "":
        pagenum=0
    else:
        pagenum=values['-IN-']
    if event == sg.WIN_CLOSED:
        break 
    if event == 'select pdf file':
        myfile= easygui.fileopenbox(msg="Choose a file", default=r"C:\Users\user\.atom")
        print(myfile)

        
    if event == 'start reading':
        read_page(myfile,pagenum)

            
        

window.close()
