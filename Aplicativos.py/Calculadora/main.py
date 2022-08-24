from tkinter import *
from tkinter import ttk

################# cores ###############
co1 = "#feffff"  # white/branca
co2 = "#6f9fbd"  # blue/azul
co3 = "#38576b"  # valor

fundo = "#3b3b3b"
co10 ="#ECEFF1"

cor1='#FFAB40'
cor2='#ff333a'
cor3='#6bd66f'
cor4="#ab8918"

janela = Tk()
janela.title('')
janela.geometry('235x318')
janela.configure(bg=co1)


style = ttk.Style(janela)
style.theme_use("clam")

################# Frames ####################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(janela, width=300, height=56,bg=co3, pady=0, padx=0, relief="flat",)
frame_score.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)


################# Funções ####################

def entrar_valores(event):
	global todos_valores
	todos_valores +=  str(event)
	valor_texto.set(todos_valores)

def calculate():
	global todos_valores
	resultado = str(eval(todos_valores))
	valor_texto.set(resultado)
	todos_valores = ""

def limpar_tela(): 
    global todos_valores
    todos_valores = "" 
    valor_texto.set("")

#para armazenar todas as expressões que serão avaliadas
todos_valores = "" 
# para entrada de valor único
valor_texto = StringVar()

################# Label ####################

app_scream = Label(frame_score,width=16,height=2,textvariable = valor_texto , padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

################# Buttons ####################

b_1 = Button(frame_quadros, text="C", width=11, height=2, bg=co1, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: limpar_tela())
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros, text="%", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('%'))
b_2.place(x=119, y=0)
b_3 = Button(frame_quadros, text="/", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('/'))
b_3.place(x=178, y=0)

b_4 = Button(frame_quadros, text="7", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(7))
b_4.place(x=0, y=52)
b_5 = Button(frame_quadros, text="8", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(8))
b_5.place(x=60, y=52)
b_6 = Button(frame_quadros, text="9", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(9))
b_6.place(x=119, y=52)
b_7 = Button(frame_quadros, text="*", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('*'))
b_7.place(x=179, y=52)

b_8 = Button(frame_quadros, text="4", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(4))
b_8.place(x=0, y=104)
b_9 = Button(frame_quadros, text="5", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(5))
b_9.place(x=60, y=104)
b_10 = Button(frame_quadros, text="6", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(6))
b_10.place(x=119, y=104)
b_11 = Button(frame_quadros, text="-", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('-'))
b_11.place(x=179, y=104)

b_12 = Button(frame_quadros, text="1", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(1))
b_12.place(x=0, y=156)
b_13 = Button(frame_quadros, text="2", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(2))
b_13.place(x=60, y=156)
b_14 = Button(frame_quadros, text="3", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(3))
b_14.place(x=119, y=156)
b_15 = Button(frame_quadros, text="+", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('+'))
b_15.place(x=179, y=156)

b_16 = Button(frame_quadros, text="0", width=11, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores(0))
b_16.place(x=0, y=208)
b_17 = Button(frame_quadros, text=".", width=5, height=2, bg=co10, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: entrar_valores('.'))
b_17.place(x=119, y=208)
b_18 = Button(frame_quadros, text="=", width=5, height=2, bg=cor1, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE,command = lambda: calculate())
b_18.place(x=178, y=208)

janela.mainloop()
