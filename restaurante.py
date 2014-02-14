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
	def __init__(self,descricao,codigo,preco,itens=[],categorias=[]):
		self.descricao = descricao
		self.codigo = codigo
		self.preco = preco
		self.itens = itens
		self.categorias = categorias
		
class ItemConta:
	def __init__(self,quantidade,produto,conta):
		self.quantidade = quantidade
		self.produto = produto
		self.conta = conta
