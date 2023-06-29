from tkinter import *
from tkinter import ttk

# Cores
cor1 = "#1a1a1a"  # preto
cor2 = "#feffff"  # branco
cor3 = "#38576b"  # azul
cor4 = "#ECEFF1"  # cinza
cor5 = "#FFAB40"  # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


# Criando função
def entrada_valores(event):
  todos_valores = event
  resultado = eval('9*2')

  # Passando valor para tela
  valor_texto.set(todos_valores)


# Criando label
valor_texto = StringVar()

app_label = Label(
    frame_tela,
    textvariable=valor_texto,
    width=16,
    height=2,
    padx=7,
    relief=FLAT,
    anchor="e",
    justify=RIGHT,
    font=('Ivy 18'),
    fg=cor2,
    bg=cor3
)
app_label.place(x=0, y=0)

# Criando botões
b_clean = Button(
    frame_corpo,
    text="C",
    width=12,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_clean.place(x=0, y=0)

b_porc = Button(
    frame_corpo,
    command=lambda: entrada_valores('%'),
    text="%",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_porc.place(x=115, y=0)

b_barra = Button(
    frame_corpo,
    text="/",
    width=6,
    height=2,
    bg=cor5,
    font=('Ivy 13 bold'),
    fg=cor2,
    relief=RAISED,
    overrelief=RIDGE
)
b_barra.place(x=177, y=0)

b_7 = Button(
    frame_corpo,
    text="7",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_7.place(x=0, y=52)

b_8 = Button(
    frame_corpo,
    text="8",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_8.place(x=59, y=52)

b_9 = Button(
    frame_corpo,
    text="9",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_9.place(x=118, y=52)

b_mult = Button(
    frame_corpo,
    text="*",
    width=6,
    height=2,
    bg=cor5,
    font=('Ivy 13 bold'),
    fg=cor2,
    relief=RAISED,
    overrelief=RIDGE
)
b_mult.place(x=177, y=52)

b_4 = Button(
    frame_corpo,
    text="4",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_4.place(x=0, y=104)

b_5 = Button(
    frame_corpo,
    text="5",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_5.place(x=59, y=104)

b_6 = Button(
    frame_corpo,
    text="6",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_6.place(x=118, y=104)

b_sub = Button(
    frame_corpo,
    text="-",
    width=6,
    height=2,
    bg=cor5,
    font=('Ivy 13 bold'),
    fg=cor2,
    relief=RAISED,
    overrelief=RIDGE
)
b_sub.place(x=177, y=104)

b_1 = Button(
    frame_corpo,
    text="1",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_1.place(x=0, y=156)

b_2 = Button(
    frame_corpo,
    text="2",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_2.place(x=59, y=156)

b_3 = Button(
    frame_corpo,
    text="3",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_3.place(x=118, y=156)

b_soma = Button(
    frame_corpo,
    text="+",
    width=6,
    height=2,
    bg=cor5,
    font=('Ivy 13 bold'),
    fg=cor2,
    relief=RAISED,
    overrelief=RIDGE
)
b_soma.place(x=177, y=156)

b_0 = Button(
    frame_corpo,
    text="0",
    width=12,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_0.place(x=0, y=208)

b_vir = Button(
    frame_corpo,
    text="%",
    width=6,
    height=2,
    bg=cor4,
    font=('Ivy 13 bold'),
    fg=cor1,
    relief=RAISED,
    overrelief=RIDGE
)
b_vir.place(x=115, y=208)

b_igual = Button(
    frame_corpo,
    text="/",
    width=6,
    height=2,
    bg=cor5,
    font=('Ivy 13 bold'),
    fg=cor2,
    relief=RAISED,
    overrelief=RIDGE
)
b_igual.place(x=177, y=208)


entrada_valores()

janela.mainloop()
