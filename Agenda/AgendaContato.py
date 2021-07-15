#import library
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import ImageTk,Image

root = tkinter.Tk()
root.geometry('1150x720')
root.config(bg = 'SlateGray3')
root.title('Agenda')
root.resizable(0,0)

C = tkinter.Canvas(root, height=90, width=3000)

coord = 1, 1, 3000, 3000
arc = C.create_rectangle(coord, fill="blue")

img = ImageTk.PhotoImage(Image.open("foto.png"))  # PIL solution
C.create_image(20, 20, anchor=NW, image=img)

C.pack()



#Cadastro Alunos
contactlist = [
    ['Contato3',  'Email@email.com1', 'Rua A','12345678', "Cidade A", "601239"],
    ['Contato2',  'Email@email.com2', 'Rua B','12345678', "Cidade B", "601421"],
    ['Contato1',   'Email@email.com3', 'Rua C','12345678', "Cidade C", "601459"],
    ]
Name = StringVar()
Email = StringVar()
Endereco = StringVar()
Telefone = StringVar()
Cidade = StringVar()
Cep = StringVar()
#create frame

frame = Frame(root)
frame.pack(side = LEFT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=20)
scroll.config (command=select.yview)
scroll.pack(side=LEFT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)



########### function to get select value

def Selected():
    return int(select.curselection()[0])

##fun to add new contact
def AddContact():
    contactlist.append([Name.get(), Email.get(),Endereco.get(),Telefone.get(), Cidade.get, Cep.get])
    Select_set()

# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Email.get(),Endereco.get(),Telefone.get(), Cidade.get, Cep.get]
    Select_set()
    
#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
# to view selected contact(first select then click on view button)
def VIEW():
    NAME, EMAIL, ENDERECO, TELEFONE, CIDADE, CEP = contactlist[Selected()]
    Name.set(NAME)
    Email.set(EMAIL)
    Endereco.set(ENDERECO)
    Telefone.set(TELEFONE)
    Cidade.set(CIDADE)
    Cep.set(CEP)



###exit game window   
def EXIT():
    root.destroy()

#empty name and Email field

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,Endereco,Telefone,Cidade,Cep in contactlist :
        select.insert (END, name)
Select_set()



######define buttons #####labels and entry wEmailget
Label(root, text = 'AGENDA', font='arial 24 bold', bg = 'blue').place(x= 500, y=25)

Label(root, text = 'NOME', font='arial 12 bold', bg = 'SlateGray3').place(x= 200, y=160)
Entry(root, textvariable = Name).place(x= 170, y=190)
Label(root, text = 'EMAIL', font='arial 12 bold',bg = 'SlateGray3').place(x= 340, y=160)
Entry(root, textvariable = Email).place(x= 310, y=190)
Label(root, text = 'ENDEREÇO', font='arial 12 bold',bg = 'SlateGray3').place(x= 465, y=160)
Entry(root, textvariable = Endereco).place(x= 450, y=190)
Label(root, text = 'TELEFONE', font='arial 12 bold',bg = 'SlateGray3').place(x= 450+160, y=160)
Entry(root, textvariable = Telefone).place(x= 450+140, y=190)
Label(root, text = 'CIDADADE', font='arial 12 bold',bg = 'SlateGray3').place(x= 450+290, y=160)
Entry(root, textvariable = Cidade).place(x= 450+280, y=190)
Label(root, text = 'CEP', font='arial 12 bold',bg = 'SlateGray3').place(x= 450+460, y=160)
Entry(root, textvariable = Cep).place(x= 450+420, y=190)

Button(root,text=" ADD", font='arial 12 bold',bg='SlateGray4', command = AddContact).place(x= 170, y=100)
Button(root,text="EDIT", font='arial 12 bold',bg='SlateGray4',command = EDIT).place(x= 250, y=100)
Button(root,text="DELETE", font='arial 12 bold',bg='SlateGray4',command = DELETE).place(x= 330, y=100)
Button(root,text="VER", font='arial 12 bold',bg='SlateGray4', command = VIEW).place(x= 430, y=100)


Button(root,text="SAIR", font='arial 12 bold',bg='tomato', command = EXIT).place(x= 550, y=630)


root.mainloop()
  
