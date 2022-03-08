from datetime import date
import requests
from tkinter import*

interf = Tk()
atual = date.today()

def cotacoes():
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        requisicao_dic = requisicao.json()
        cot_dolar = requisicao_dic['USDBRL']['bid']
        cot_euro = requisicao_dic['EURBRL']['bid']
        cot_btc = requisicao_dic['BTCBRL']['bid']
        texto = f'''
        Dólar: R${cot_dolar:.4}
        Euro: R${cot_euro:.4}
        BTC: R${cot_btc}'''
        text_cot['text'] = texto

# Tamanho e proporção da interface.
interf.title('Cotação')
interf.geometry('285x350')
interf.configure(background='gray')
interf.resizable(False, False)
interf.maxsize(width= 285, height=350)
interf.minsize(width= 285, height=350)

# Imagem de fundo.
frame_1 = Frame( bd=3, bg='white')
frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.95)

# Texto para auxiliar na descrição da função do botao1.
orientacao = Label(interf,text='Clique no botão para ver cotações das moedas',bg='white',fg='black')
orientacao.grid(column=0, row=0, padx=10, pady=10)

# Botão irá gerar o text_cot da API.
botao1 = Button(interf,text='Cotar', bd='3', bg='white', fg='black', activebackground='#108ecb', activeforeground="white",font=('verdana', 8, 'bold'), command=cotacoes)
botao1.place(relx=0.28, rely=0.3, relwidth=0.4, relheight=0.07)

# Informações da API com espaçamento.
text_cot = Label(interf, text='', bg='white')
text_cot.place(relx=0.19, rely=0.38, relwidth=0.5, relheight=0.18)

# Atribui a interface uma data atual para referência da cotação.
atual = Label(interf, text=atual,bg='white')
atual.place(relx=0.32, rely=0.55, relwidth=0.3, relheight=0.18)


interf.mainloop()
