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
