#!/usr/bin/env python
#coding: utf-8

class Mesa:
    def __init__(self,numero,status,contas=[]):
        self.numero = numero
        self.status = status
        self.contas = contas
        
class Categoria:
	def __init__(self,descricao,produtos=[]):
		self.descricao = descricao
		self.produtos = produtos
		
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
