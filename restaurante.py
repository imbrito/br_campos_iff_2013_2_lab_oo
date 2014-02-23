#!/usr/bin/env python
#coding: utf-8

class Mesa:
    def __init__(self,numero,status,contas=[]):
        self.numero = numero
        self.status = status
        self.contas = contas

    def verify_contas(self,conta):
    	return (conta in self.contas)

    def insert_contas(self,conta):
    	if not conta in self.contas:
    		self.contas.append(conta)
        
class Categoria:
	def __init__(self,descricao,produtos=[]):
		self.descricao = descricao
		self.produtos = produtos

	def insert_produtos(self,produto):
		if not produto in self.produtos:
			self.produtos.append(produto)

	def verify_produtos(self,produto):
		return (produto in self.produtos)
		
class Garcom:
	def __init__(self,nome,endereco,telefone,cpf,identidade,matricula,contas=[]):
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone
		self.cpf = cpf
		self.identidade = identidade
		self.matricula = matricula
		self.contas = contas
		
	def insert_contas(self,conta):
		if not conta in self.contas:
			self.contas.append(conta)

	def verify_contas(self,conta):
		return (conta in self.contas)

	def calculate_commission_of_waiters(self):
		valor_da_comissao = 0.0
		for conta in self.contas:
			valor_da_comissao += (conta.comissao * conta.valor_final)
		return valor_da_comissao
		
class Conta:
	def __init__(self,data_abertura,hora_abertura,status,mesa,garcom,hora_fechamento=None,data_fechamento=None,valor_final=0.0,comissao=0.1,itens=[]):
		self.data_abertura = data_abertura
		self.hora_abertura = hora_abertura
		self.status = status
		self.mesa = mesa
		self.garcom = garcom
		self.hora_fechamento = hora_fechamento
		self.data_fechamento = data_fechamento
		self.itens = itens
		self.valor_final = valor_final
		self.comissao = comissao

	def insert_itens(self,item):
		if not item in self.itens:
			self.itens.append(item)

	def verify_itens(self,item):
		return (item in self.itens)

	def close_count(self,data_fechamento,hora_fechamento):
		self.data_fechamento = data_fechamento
		self.hora_fechamento = hora_fechamento
		self.status = 'encerrada'
		return 'Conta encerrada! Imprima e-NF!'

	def calculate_total_value_count(self):
		if 0 < len(self.itens):
			for item in self.itens:
				self.valor_final += item.calculate_value_itemconta()
			return self.valor_final
		return False

	def print_nota_fiscal(self):
		if 0 < len(self.itens):
			nota_fiscal = ''
			nota_fiscal += ('Data Abertura: %s - Hora Abertura: %s\n'%(self.data_abertura,self.hora_abertura))
			nota_fiscal += 'Qtd Produto - Valor\n'
			for item in self.itens:
				nota_fiscal += ('%02.d %s X %.2f\n'%(item.quantidade,item.produto.nome,item.produto.preco))
			nota_fiscal += ('Valor final: %.2f\n'%(self.valor_final))
			nota_fiscal += ('Data Fechamento: %s - Hora Fechamento: %s'%(self.data_fechamento,self.hora_fechamento))
			return nota_fiscal
		return False
		
class Produto:
	def __init__(self,nome,descricao,codigo,preco,itens=[],categorias=[]):
	    self.nome = nome
	    self.descricao = descricao
	    self.codigo = codigo
	    self.preco = preco
	    self.itens = itens
	    self.categorias = categorias
		
	def insert_itens(self,item):
		if not item in self.itens:
			self.itens.append(item)

	def verify_itens(self,item):
		return (item in self.itens)

	def insert_categorias(self,categoria):
		if not categoria in self.categorias:
			self.categorias.append(categoria)

	def verify_categorias(self,categoria):
		return (categoria in self.categorias)
		
class ItemConta:
	def __init__(self,quantidade,produto,conta):
		self.quantidade = quantidade
		self.produto = produto
		self.conta = conta
		
	def calculate_value_itemconta(self):
		return (self.quantidade * self.produto.preco)
