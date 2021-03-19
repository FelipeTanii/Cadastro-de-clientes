from modulos import *
from validEntry import Validadores
from frameGrad import GradientFrame
from reports import Relatorios
from funcionalidades import Funcs
from placeHolder import EntPlaceHold
import pycep_correios
root = tix.Tk()
class Application(Funcs, Relatorios, Validadores):
	def __init__(self):
		self.root = root
		self.validaEntradas()
		self.tela()
		self.frames_da_tela()
		self.widgets_frame1()
		self.lista_frame2()
		self.montaTabelas()
		self.select_lista()
		self.Menus()
		self.calendario()
		self.print_cal()
		root.mainloop()
	def cepCorreios(self):
		try:
			self.cidade_entry.delete(0, END)
			self.lograd_entry.delete(0, END)
			self.bairro_entry.delete(0, END)
			zipcode = self.cep_entry.get()
			dadosCep = pycep_correios.get_address_from_cep(zipcode)
			self.cidade_entry.insert(END, dadosCep["cidade"])
			self.lograd_entry.insert(END, dadosCep["logradouro"])
			self.bairro_entry.insert(END, dadosCep["bairro"])
		except:
			messagebox.showinfo("info", "CEP inválido")
	def tela(self):
		self.root.title("Cadastro de Clientes") 
		self.root.configure(background= '#1e3743')
		self.root.geometry("600x500+0+0")
		self.root.resizable(True, True)
		self.root.maxsize(width= 900, height= 700)
		self.root.minsize(width= 500, height= 500)
	def frames_da_tela(self):
		self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee', highlightbackground= '#bcc8d8', highlightthickness= 3)
		self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46) 
		self.frame_2 = Frame(self.root, bd = 4, bg= '#dfe3ee', highlightbackground= '#bcc8d8', highlightthickness= 3)
		self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
	def widgets_frame1(self):
		self.abas = ttk.Notebook(self.frame_1)
		self.aba1 = GradientFrame(self.abas, "gray", "#1e3743")
		self.aba2 = Frame(self.abas)
		self.aba1.configure(background= "#dfe3ee")
		self.aba2.configure(background= "lightgray")
		self.abas.add(self.aba1, text = "Aba 1")
		self.abas.add(self.aba2, text = "Aba 2")
		self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
		self.bt_limpar = Button(self.aba1, text= 'Limpar', bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.limpa_cliente)
		self.bt_limpar.place(relx= 0.15, rely= 0.1, relwidth= 0.1, relheight= 0.15)
		self.bt_buscar = Button(self.aba1, text= 'Buscar', bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command = self.busca_cliente)
		self.bt_buscar.place(relx= 0.25, rely= 0.1, relwidth= 0.1, relheight= 0.15)
		texto_balao_buscar = "Digite o nome do cliente que deseja pesquisar."
		self.balao_buscar = tix.Balloon(self.aba1)
		self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = texto_balao_buscar)
		self.bt_novo = Button(self.aba1, text="Novo", bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.add_cliente)
		self.bt_novo.place(relx= 0.36, rely= 0.07, width= 70, height= 40)
		self.bt_alterar = Button(self.aba1, text= 'Alterar', bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.altera_cliente)
		self.bt_alterar.place(relx= 0.5, rely= 0.1, relwidth= 0.1, relheight= 0.15)
		self.bt_apagar = Button(self.aba1, text= 'Apagar', bd= 2, bg= '#e4e4e4', fg= '#024c2c', activebackground= '#bcc8d8', activeforeground='green', font = ('times', 10, 'bold'), command= self.deleta_cliente)
		self.bt_apagar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
		self.bt_janela2Ajuda = Button(self.aba1, text= '?', bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.janela2)
		self.bt_janela2Ajuda.place(relx= 0.7, rely= 0.1, relwidth= 0.05, relheight= 0.15)
		self.lb_codigo = Label(self.aba1, text= 'Codigo', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_codigo.place(relx= 0.04, rely= 0.04)
		self.codigo_entry = Entry(self.aba1, fg= '#024c2c', validate="key", validatecommand= self.vcmd2)
		self.codigo_entry.place(relx= 0.04, rely= 0.15, relwidth= 0.09)
		self.lb_nome = Label(self.aba1, text= 'Nome', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_nome.place(relx= 0.02, rely= 0.3)
		self.nome_entry = Entry(self.aba1, fg= '#024c2c', validate="key", validatecommand= self.valid60)
		self.nome_entry.place(relx= 0.02, rely= 0.40, relwidth= 0.66)
		self.lb_fone = Label(self.aba1, text= 'Telefone', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_fone.place(relx= 0.02, rely= 0.57)
		self.fone_entry = Entry(self.aba1, fg= '#024c2c', validate="key", validatecommand= self.valid20)
		self.fone_entry.place(relx= 0.135, rely= 0.57, relwidth= 0.255)
		self.lb_cidade = Label(self.aba1, text= 'Cidade', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_cidade.place(relx= 0.4, rely= 0.57)
		self.cidade_entry = Entry(self.aba1, fg='#024c2c', validate="key", validatecommand= self.valid60)
		self.cidade_entry.place(relx= 0.493, rely=0.57, relwidth= 0.486)
		self.bt_cep = Button(self.aba1, text= 'CEP', bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.cepCorreios)
		self.bt_cep.place(relx= 0.72, rely= 0.38, relwidth= 0.1, relheight= 0.15)
		self.cep_entry = Entry(self.aba1, fg='#024c2c', validate="key", validatecommand= self.valid20)
		self.cep_entry.place(relx=0.82, rely=0.39, relwidth= 0.15)
		self.lb_lograd = Label(self.aba1, text= 'Endereço', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_lograd.place(relx= 0.02, rely= 0.71)
		self.lograd_entry = Entry(self.aba1, fg= '#024c2c', validate="key", validatecommand= self.valid100)
		self.lograd_entry.place(relx= 0.14, rely= 0.71, relwidth= 0.50)
		self.lb_bairro = Label(self.aba1, text= 'Bairro', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_bairro.place(relx= 0.649, rely= 0.71)
		self.bairro_entry = Entry(self.aba1, fg='#024c2c', validate="key", validatecommand= self.valid60)
		self.bairro_entry.place(relx= 0.73, rely=0.71, relwidth= 0.25)
		self.lb_notas = Label(self.aba1, text= 'Notas', bg= '#dfe3ee', fg= '#024c2c')
		self.lb_notas.place(relx= 0.02, rely= 0.85)
		self.notas_entry = Entry(self.aba1, fg='#024c2c', validate="key", validatecommand= self.valid100)
		self.notas_entry.place(relx= 0.10, rely=0.85, relwidth= 0.88)
		self.Tipvar = StringVar()
		self.TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
		self.Tipvar.set("Solteiro(a)")
		self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
		self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2)
		self.estado_civil = self.Tipvar.get()
		self.bt_calendario = Button(self.aba1, text= "Data", bd= 2, bg= '#e4e4e4', fg= '#024c2c', font = ('times', 10, 'bold'), command= self.calendario)
		self.bt_calendario.place(relx=0.80, rely=0.07)
		self.data_entry = Entry(self.aba1, width= 10, fg= '#024c2c', validate="key", validatecommand= self.valid10)
		self.data_entry.place(relx= 0.78, rely= 0.21)
	def lista_frame2(self):
		self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=('col1, col2, col3, col4'))
		self.listaCli.heading('#0', text= '')
		self.listaCli.heading('#1', text= 'Codigo')
		self.listaCli.heading('#2', text= 'Nome')
		self.listaCli.heading('#3', text= 'Telefone')
		self.listaCli.heading('#4', text= 'Cidade')
		self.listaCli.column('#0', width=1)
		self.listaCli.column('#1', width=50)
		self.listaCli.column('#2', width=200)
		self.listaCli.column('#3', width=125)
		self.listaCli.column('#4', width=125)
		self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
		self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
		self.listaCli.configure(yscroll=self.scroolLista.set)
		self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
		self.listaCli.bind("<Double-1>", self.OnDoubleClick)
	def Menus(self):
		menubar = Menu(self.root)
		self.root.config(menu=menubar)
		filemenu = Menu(menubar)
		filemenu2 = Menu(menubar)
		def Quit(): self.root.destroy()
		menubar.add_cascade(label="Opções", menu= filemenu)
		menubar.add_cascade(label="Sobre", menu= filemenu2)
		filemenu.add_command(label="Sair", command= Quit)
		filemenu2.add_command(label="Limpa Cliente", command= self.limpa_cliente)
		filemenu2.add_command(label="Ficha do Cliente", command= self.geraRelatCliente)
	def janela2(self):
		self.root2 = Toplevel()
		self.root2.title("Janela 2")
		self.root2.configure(background="lightblue")
		self.root2.geometry("400x200")
		self.root2.resizable(False, False)
		self.root2.transient(self.root)
		self.root2.focus_force()
		self.root2.grab_set()
		label = Label(self.root2, text="Duvidas acesse:  http://marocero2016.blogspot.com/")
		label.place(x=13, y=13)
	def validaEntradas(self):
		self.vcmd2 = (self.root.register(self.validateCod), "%P")
		self.valid60 = (self.root.register(self.validate60), "%P")
		self.valid20 = (self.root.register(self.validate20), "%P")
		self.valid100 = (self.root.register(self.validate100), "%P")
		self.valid10 = (self.root.register(self.validate10), "%P")
Application()
''' 2021 03 13
https://www.youtube.com/watch?v=24ko20BEd7U&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-&index=35
'''













