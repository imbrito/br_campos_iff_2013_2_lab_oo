#!/usr/bin/env python
#coding: utf-8

import unittest
from should_dsl import should
from restaurante import *

class MesaSpec(unittest.TestCase):
	
	def it_creates_a_mesa_object(self):
		mesa = Mesa('numero','status')
		mesa.numero |should| equal_to('numero')
		mesa.status |should| equal_to('status')
		mesa.contas |should| equal_to([])

class CategoriaSpec(unittest.TestCase):

	def it_creates_a_categoria_object(self):
		categoria = Categoria('descricao')
		categoria.descricao |should| equal_to('descricao')
		categoria.produtos |should| equal_to([])

class GarcomSpec(unittest.TestCase):

	def it_creates_a_garcom_object(self):
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula')
		garcom.nome |should| equal_to('nome')
		garcom.endereco |should| equal_to('endereco')
		garcom.telefone |should| equal_to('telefone')
		garcom.cpf |should| equal_to('cpf')
		garcom.identidade |should| equal_to('identidade')
		garcom.matricula |should| equal_to('matricula')
		garcom.contas |should| equal_to([])
		
	def it_insert_contas(self):
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,garcom,None,None,56.75,0.1,[])
		garcom.insert_contas(conta)
		(conta in garcom.contas) |should| equal_to(True)
		del garcom, conta

	def it_verify_contas(self):
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,garcom,None,None,56.75,0.1,[])
		garcom.verify_contas(conta) |should| equal_to(False)
		garcom.insert_contas(conta)
		garcom.verify_contas(conta) |should| equal_to(True)
		del garcom, conta

	def it_calculate_commission_of_waiters(self):
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta_one = Conta('dd/mm/aaaa','hh:mm:ss','status',None,garcom,None,None,56.75,0.1,[])
		conta_two = Conta('dd/mm/aaaa','hh:mm:ss','status',None,garcom,None,None,65,0.05,[])
		conta_three = Conta('dd/mm/aaaa','hh:mm:ss','status',None,garcom,None,None,80,0.1,[])
		garcom.insert_contas(conta_one)
		garcom.insert_contas(conta_two)
		garcom.insert_contas(conta_three)
		garcom.calculate_commission_of_waiters() |should| equal_to(16.925)
		del garcom, conta_one, conta_two, conta_three
		
class ContaSpec(unittest.TestCase):

	def it_creates_a_conta_object(self):
		mesa = Mesa('numero','status',[])
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,garcom)
		conta.data_abertura |should| equal_to('dd/mm/aaaa')
		conta.hora_abertura |should| equal_to('hh:mm:ss')
		conta.status |should| equal_to('status')
		conta.mesa |should| equal_to(mesa)
		conta.garcom |should| equal_to(garcom)
		conta.hora_fechamento |should| equal_to(None)
		conta.data_fechamento |should| equal_to(None)
		conta.valor_final |should| equal_to(0.0)
		conta.comissao |should| equal_to(0.1)
		conta.itens |should| equal_to([])

class ProdutoSpec(unittest.TestCase):

	def it_creates_a_produto_object(self):
		produto = Produto('nome','descricao','codigo','preco')
		produto.nome |should| equal_to('nome')
		produto.descricao |should| equal_to('descricao')
		produto.codigo |should| equal_to('codigo')
		produto.preco |should| equal_to('preco')
		produto.itens |should| equal_to([])
		produto.categorias |should| equal_to([])
		
	def it_insert_itens(self):
		produto = Produto('nome','descricao','codigo','preco')
		itemconta = ItemConta('quantidade',produto,None)
		produto.insert_itens(itemconta)
		(itemconta in produto.itens) |should| equal_to(True)
		del produto, itemconta

	def it_verify_itens(self):
		produto = Produto('nome','descricao','codigo','preco')
		itemconta = ItemConta('quantidade',produto,None)
		produto.verify_itens(itemconta) |should| equal_to(False)
		produto.insert_itens(itemconta)
		produto.verify_itens(itemconta) |should| equal_to(True)
		del produto, itemconta

	def it_insert_categorias(self):
		categoria = Categoria('descricao',[])
		produto = Produto('nome','descricao','codigo','preco')
		produto.insert_categorias(categoria)
		(categoria in produto.categorias) |should| equal_to(True)
		del categoria, produto

	def it_verify_categorias(self):
		categoria = Categoria('descricao',[])
		produto = Produto('nome','descricao','codigo','preco')
		produto.verify_categorias(categoria) |should| equal_to(False)
		produto.insert_categorias(categoria)
		produto.verify_categorias(categoria) |should| equal_to(True)
		del categoria, produto

class ItemContaSpec(unittest.TestCase):

	def it_creates_a_item_conta_object(self):
		produto = Produto('descricao','codigo','preco',[],[])
		mesa = Mesa('numero','status',[])
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,garcom,None,None,0.0,0.1,[])
		itemconta = ItemConta('quantidade',produto,conta)
		itemconta.quantidade |should| equal_to('quantidade')
		itemconta.produto |should| equal_to(produto)
		itemconta.conta |should| equal_to(conta)
		
	def it_calculate_value_itemconta(self):
		produto = Produto('nome','descricao','codigo',5)
		mesa = Mesa('numero','status',[])
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,garcom,None,None,0.0,0.1,[])
		itemconta = ItemConta(1.5,produto,conta)
		itemconta.calculate_value_itemconta() |should| equal_to(7.50)
		del produto, mesa, garcom, conta, itemconta
