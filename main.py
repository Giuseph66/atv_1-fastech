import tkinter as tk
from tkinter import *
from tkinter import messagebox

class cinema():
    def __init__(self) :
        self.tela=tk.Tk()
        self.tela.geometry("800x500+500+50")
        self.tela.title("Pesquisa...")
        self.tela.iconbitmap("atv_1-fastech/lupa.ico")
        self.tela.resizable(0,0)
        self.guarda=[]
        self.gra_nomes,self.gra_valores=[],[]
        self.total=0
        self.princ()
        self.tela.mainloop()
    def princ(self):
        self.ideia=StringVar()
        self.total=len(self.guarda)
        self.fundo=LabelFrame(self.tela,width=800,height=500,bg="green")
        self.fundo.place(x=0,y=0)
        self.chat_1=Label(self.fundo,text="Atendente:\n Estou fazendo uma pesquisa e gostaria da sua participação! \n Será apenas algumas perguntas..",font="Arial 12 bold",bg="white",bd=5,fg="black",height=5,width=75)
        self.chat_1.place(x=25,y=25)
        self.chat_2=Label(self.fundo,text=f"{self.total} entrevistados",font="Arial 12 bold",bg="white",bd=5,fg="black",height=1,width=12)
        self.chat_2.place(x=650,y=100)
        self.text_nome=Label(self.fundo,font="Arial 12 bold",text="Nome:",bg="green",bd=1,fg="black",width=5)
        self.text_nome.place(x=25,y=150)
        self.nome=Entry(self.fundo,font="Arial 12 bold",bg="white",bd=1,fg="black")
        self.nome.bind("<Return>",lambda event:self.idade.focus())
        self.nome.place(x=25,y=180,height=25,width=200)
        self.text_idade=Label(self.fundo,font="Arial 12 bold",text="Idade:",bg="green",bd=1,fg="black",width=5)
        self.text_idade.place(x=400,y=150)
        self.idade=Entry(self.fundo,font="Arial 12 bold",bg="white",bd=1,fg="black")
        self.idade.bind("<Return>",lambda event:self.anotacao())
        self.idade.place(x=400,y=180,height=25,width=100)
        self.reacao=Label(self.fundo,font="Arial 12 bold",text="Oque voce achou do nosso atendimento?",bg="green",bd=1,fg="black",width=75)
        self.reacao.place(x=25,y=250)
        self.otimo=Radiobutton(self.fundo,font="Arial 12 bold",variable=self.ideia,value="Otimo",text="Otimo",bg="green",bd=1,fg="black",height=1,width=5)
        self.otimo.place(x=50,y=320)
        self.Bom=Radiobutton(self.fundo,font="Arial 12 bold",variable=self.ideia,value="Bom",text="Bom",bg="green",bd=1,fg="black",height=1,width=5)
        self.Bom.place(x=250,y=320)
        self.Regular=Radiobutton(self.fundo,font="Arial 12 bold",variable=self.ideia,value="Regular",text="Regular",bg="green",bd=1,fg="black",height=1,width=5)
        self.Regular.place(x=450,y=320)
        self.Pessimo=Radiobutton(self.fundo,font="Arial 12 bold",variable=self.ideia,value="Pessimo",text="Pessimo",bg="green",bd=1,fg="black",height=1,width=6)
        self.Pessimo.place(x=650,y=320)
        self.confirmar=Button(self.fundo,font="Arial 12 bold",text="Confimar",bg="white",bd=2,fg="black",height=1,width=10,command=self.anotacao)
        self.confirmar.place(x=500,y=430)
        self.final=Button(self.fundo,font="Arial 12 bold",text="Finalizar",bg="white",bd=2,fg="black",height=1,width=10,command=self.resumo)
        self.final.place(x=650,y=430)
        self.nome.focus_set()
    def anotacao(self):
        self.name=self.nome.get()
        self.age=self.idade.get()
        self.opniao=self.ideia.get()
        if self.name and self.age and self.opniao not in (""):
            if not self.age.isdigit():
                messagebox.showerror("Erro", "A entrada deve conter apenas números.")
                self.idade.delete(0, tk.END)
                self.idade.focus()
            else:
                if int(self.age) ==0:
                    self.idade.delete(0, tk.END)
                    self.idade.focus()
                    messagebox.showerror("Erro", "Nao é possivel ter 0 anos.")
                else:
                    self.guarda.append([self.name,self.age,self.opniao])
                    self.novos_dados()
        else:
            messagebox.showinfo("Error","Responda corretamente!")
            self.nome.focus()
    def resumo(self):
        if messagebox.askyesno("Certeza","Deseja mesmo finalizar?"):
            self.x=-150
            self.fundo.destroy()
            self.fundo=LabelFrame(self.tela,width=800,height=500,bg="green")
            self.fundo.place(x=0,y=0)
            self.chat_1=Label(self.fundo,text=f"A pesquisa foi realizada com {self.total} pessoas, dentre tudo essas foram as respostas:",font="Arial 12 bold",bg="green",bd=5,fg="black",height=1,width=75)
            self.chat_1.place(x=25,y=25)
            self.finaliza("Otimo")
            self.finaliza("Bom")
            self.finaliza("Regular")
            self.finaliza("Pessimo")
            idade_mais_velha = None
            idade_mais_nova = None
            nome_mais_velha = None
            nome_mais_nova = None
            ideia_mais_velha = None
            ideia_mais_nova = None

            for pessoa in self.guarda:
                nome, idade, avaliacao = pessoa
                if idade_mais_velha is None or idade > idade_mais_velha:
                    idade_mais_velha = idade
                    nome_mais_velha = nome
                    ideia_mais_velha=avaliacao

                if idade !="00":    
                    if idade_mais_nova is None or idade < idade_mais_nova:
                        idade_mais_nova = idade
                        nome_mais_nova = nome
                        ideia_mais_nova=avaliacao

            if nome_mais_velha is not None:
                velho=(f"A pessoa mais velha a responder foi o(a) {nome_mais_velha}, com {idade_mais_velha} anos que achou {ideia_mais_velha} o atendimento.")
            else:
                velho=("Nenhum dado encontrado para a pessoa mais velha.")

            if nome_mais_nova is not None:
                novo=(f"A pessoa mais nova a responder foi o(a) {nome_mais_nova}, com {idade_mais_nova} anos que achou {ideia_mais_nova} o atendimento.")
            else:
                novo=("Nenhum dado encontrado para a pessoa mais nova.")
            
            self.chat_3=Label(self.fundo,text=velho,font="Arial 12 bold",bg="green",bd=5,fg="black",height=1,width=75)
            self.chat_3.place(x=25,y=120)
            self.chat_4=Label(self.fundo,text=novo,font="Arial 12 bold",bg="green",bd=5,fg="black",height=1,width=75)
            self.chat_4.place(x=25,y=150)
            self.dnv=Button(self.fundo,font="Arial 12 bold",text="Nova Pesquisa",bg="white",bd=2,fg="black",height=1,width=15,command=self.dnv_)
            self.dnv.place(x=630,y=350)
            self.sair=Button(self.fundo,font="Arial 12 bold",text="Sair",bg="white",bd=2,fg="black",height=1,width=15,command=exit)
            self.sair.place(x=630,y=450)
            self.desenha_gra=Button(self.fundo,font="Arial 12 bold",text="Desenhar Gráfico",bg="white",bd=2,fg="black",height=1,width=15,command=self.desenhar_grafico)
            self.desenha_gra.place(x=630,y=400)
    def dnv_(self):
        self.guarda=[]
        self.gra_nomes,self.gra_valores=[],[]
        self.total=0
        self.novos_dados()
    def finaliza(self,avaliação):
        cont=0
        for pega in self.guarda:
            if pega[2]==avaliação:
                cont+=1
        self.x+=200
        self.chat_2=Label(self.fundo,text=f"{avaliação}: {cont}",font="Arial 12 bold",bg="green",bd=5,fg="black",height=1,width=10)
        self.chat_2.place(x=self.x,y=70)
        self.gra_nomes.append(avaliação)
        self.gra_valores.append(cont)
    def novos_dados(self):
        self.fundo.destroy()
        self.princ()

    def desenhar_grafico(self):
        self.grafico = Canvas(self.fundo, width=500, height=250)
        self.grafico.place(x=50,y=200)
        self.grafico.create_text(250, 7, text="Grafico das votações",font="Arial 10 bold", tag="grafico")
        largura = 40
        x = 50
        multiplique=5
        maior=max(self.gra_valores)
        if maior>30:
            multiplique=4
        if maior>50:
            multiplique=3
        if maior>65:
            multiplique=2
        if maior>100:
            multiplique=1
        for nome, valor in zip(self.gra_nomes, self.gra_valores):
            altura = valor * multiplique 
            self.grafico.create_rectangle(x, 220, x + largura, 220 - altura, fill="blue", tag="grafico")
            self.grafico.create_text(x + largura // 2, 230, text=nome, tag="grafico")
            self.grafico.create_text(x + largura // 2, 220 - altura - 10, text=str(valor), tag="grafico")
            x += 3 * largura
    
cinema()
        