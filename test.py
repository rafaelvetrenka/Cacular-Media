import tkinter as tk

janela = tk.Tk()
janela.title = ("Média")
janela.geometry("300x220")
janela.configure(bg='gray')

titulo = tk.Label(janela, text="Calcular Média")
titulo.pack()

nota1 = tk.Entry(janela)
nota1.pack(pady=10)
nota2 = tk.Entry(janela)
nota2.pack(pady=10)
nota3 = tk.Entry(janela)
nota3.pack(pady=10)

lista = []
lista.append(nota1)
lista.append(nota2)
lista.append(nota3)

def mediar():
    somar = sum(float(nota.get()) for nota in lista)
    media = somar / len(lista)
    resultado['text'] = "Média: " + str(media)

botao = tk.Button(janela, text="Execute", command=mediar)
botao.pack(pady=10)

resultado = tk.Label(janela, text="", bg="gray")
resultado.pack()

janela.mainloop()

