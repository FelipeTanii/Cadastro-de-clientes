from modulos import *
class Funcs():
	def limpa_cliente(self):
		self.codigo_entry.delete(0, END)
		self.nome_entry.delete(0, END)
		self.fone_entry.delete(0, END)
		self.cidade_entry.delete(0, END)
		self.cep_entry.delete(0, END)
		self.lograd_entry.delete(0, END)
		self.bairro_entry.delete(0, END)
		self.notas_entry.delete(0, END)
	def conecta_bd(self):
		self.conn = sqlite3.connect("clientes.bd")
		self.cursor = self.conn.cursor(); print("Conectando banco de dados")
	def desconecta_bd(self):
		self.conn.close(); print("Desconectando banco de dados")
	def montaTabelas(self):
		self.conecta_bd()
		### Criar tabela
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes (
				cod INTEGER PRIMARY KEY,
				nome_cliente CHAR(40) NOT NULL,
				telefone INTEGER(20),
				cidade CHAR(40),cep CHAR(10),logradouro CHAR(50), 
				bairro CHAR(40), notas CHAR(100), data CHAR(10)
			);
		""")
		self.conn.commit(); print("Banco de dados criado")
		self.desconecta_bd()
	def var(self):
		self.codigo = self.codigo_entry.get()
		self.nome = self.nome_entry.get()
		self.fone = self.fone_entry.get()
		self.cidade = self.cidade_entry.get()
		self.cep = self.cep_entry.get()
		self.logradouro = self.lograd_entry.get()
		self.bairro = self.bairro_entry.get()
		self.notas = self.notas_entry.get()
		self.data = self.data_entry.get()
	def add_cliente(self):
		self.var()
		if self.nome_entry.get() == "" or self.fone_entry.get() == "" or self.data_entry.get() == "":
			msg = "Para cadastrar um novo cliente é necessário que seja digitado um nome, telefone e data. \n"
			msg += "Campo vazio."
			messagebox.showinfo("Cadastro de clientes - Aviso!", msg)
		else:
			self.conecta_bd()
			self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade, cep, logradouro, bairro, notas, data)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.fone, self.cidade, self.cep, self.logradouro, self.bairro, self.notas, self.data))
			self.conn.commit()
			self.desconecta_bd()
			self.select_lista()
			self.limpa_cliente()
	def select_lista(self):
		self.listaCli.delete(*self.listaCli.get_children())
		self.conecta_bd()
		lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade, cep, logradouro, bairro, notas, data FROM clientes
			ORDER BY nome_cliente ASC; """)
		for i in lista:
			self.listaCli.insert("", END, values=i)
		self.desconecta_bd()
	def OnDoubleClick(self, event):
		self.limpa_cliente()
		self.listaCli.selection()
		for n in self.listaCli.selection():
			col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaCli.item(n, 'values')
			self.codigo_entry.insert(END, col1)
			self.nome_entry.insert(END, col2)
			self.fone_entry.insert(END, col3)
			self.cidade_entry.insert(END, col4)
			self.cep_entry.insert(END, col5)
			self.lograd_entry.insert(END, col6)
			self.bairro_entry.insert(END, col7)
			self.notas_entry.insert(END, col8)
			self.data_entry.insert(END, col9)
	def deleta_cliente(self):
		self.var()
		self.conecta_bd()
		self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
		self.conn.commit()
		self.desconecta_bd()
		self.limpa_cliente()
		self.select_lista()
	def altera_cliente(self):
		self.var()
		self.conecta_bd()
		self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?, cep = ?, logradouro = ?, bairro = ?, notas = ?
			WHERE cod = ? """, (self.nome, self.fone, self.cidade, self.cep, self.logradouro, self.bairro, self.notas, self.codigo))
		self.conn.commit()
		self.desconecta_bd()
		self.select_lista()
		self.limpa_cliente()
	def busca_cliente(self):
		self.conecta_bd()
		self.listaCli.delete(*self.listaCli.get_children())
		self.nome_entry.insert(END, '%')
		nome = self.nome_entry.get()
		self.cursor.execute(
			""" SELECT cod, nome_cliente, telefone, cidade, cep, logradouro, bairro, notas, data FROM clientes
			WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
		buscanomeCli = self.cursor.fetchall()
		for i in buscanomeCli:
			self.listaCli.insert("", END, values=i)
		self.limpa_cliente()
		self.desconecta_bd()
	def calendario(self):
		self.calendario1 = Calendar(self.aba1, fg="gray75", bg= "blue", font=("Times", "9", "bold"), locate= "pt-br")
		self.calendario1.place(relx=0.4, rely=0.1)
		self.calData = Button(self.aba1, text= "Inserir Data", bg= "gray75", command= self.print_cal)
		self.calData.place(relx=0.77, rely=0.82, height=25, width=100)
		
		self.closeData = Button(self.aba1, text= "Fechar", bg= "gray75", command=self.fechaCal)
		self.closeData.place(relx=0.77, rely=0.72, height=25, width=100)
		
	def print_cal(self):
		dataIni = self.calendario1.get_date()
		self.data_entry.delete(0, END)
		self.data_entry.insert(END, dataIni)
		self.calData.destroy()
		self.calendario1.destroy()
		self.closeData.destroy()
	def fechaCal(self):
		self.calData.destroy()
		self.calendario1.destroy()
		self.closeData.destroy()
		
