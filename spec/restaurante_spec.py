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
		del mesa

	def it_insert_contas(self):
		mesa = Mesa('numero','status',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,None,None,None,56.75,0.1,[])
		mesa.insert_contas(conta)
		(conta in mesa.contas) |should| equal_to(True)
		del mesa, conta

	def it_verify_contas(self):
		mesa = Mesa('numero','status',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,None)
		mesa.verify_contas(conta) |should| equal_to(False)
		mesa.insert_contas(conta)
		mesa.verify_contas(conta) |should| equal_to(True)
		del mesa, conta

class CategoriaSpec(unittest.TestCase):

	def it_creates_a_categoria_object(self):
		categoria = Categoria('descricao')
		categoria.descricao |should| equal_to('descricao')
		categoria.produtos |should| equal_to([])
		del categoria

	def it_insert_produtos(self):
		categoria = Categoria('descricao',[])
		produto = Produto('nome','descricao','codigo','preco',[],[])
		categoria.insert_produtos(produto)
		(produto in categoria.produtos) |should| equal_to(True)
		del categoria, produto

	def it_verify_produtos(self):
		categoria = Categoria('descricao',[])
		produto = Produto('nome','descricao','codigo','preco',[],[])
		categoria.verify_produtos(produto) |should| equal_to(False)
		categoria.insert_produtos(produto)
		categoria.verify_produtos(produto) |should| equal_to(True)
		del categoria, produto

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
		del garcom
		
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
		del mesa, garcom, conta

	def it_insert_itens(self):
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,None,None,None,56.75,0.1,[])
		itemconta = ItemConta('quantidade',None,conta)
		conta.insert_itens(itemconta)
		(itemconta in conta.itens) |should| equal_to(True)
		del conta, itemconta

	def it_verify_itens(self):
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,None,None,None,56.75,0.1,[])
		itemconta = ItemConta('quantidade',None,conta)
		conta.verify_itens(itemconta) |should| equal_to(False)
		conta.insert_itens(itemconta)
		conta.verify_itens(itemconta) |should| equal_to(True)
		del conta, itemconta

	def it_close_count(self):
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,None)
		conta.close_count('dd/mm/aaaa','hh:mm:ss') |should| equal_to('Conta encerrada! Imprima e-NF!')
		conta.status |should| equal_to('encerrada')
		del conta

	def it_calculate_total_value_count(self):
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',None,None,None,None,0.0,0.1,[])
		produto_one = Produto('Refrigerante','descricao','codigo',5.25,[],[])
		produto_two = Produto('Parmegiana','descricao','codigo',25.75,[],[])
		produto_three = Produto('Sorvete','descricao','codigo',9,[],[])
		itemconta_one = ItemConta(1,produto_one,conta)
		itemconta_two = ItemConta(3,produto_two,conta)
		itemconta_three = ItemConta(2.5,produto_three,conta)
		conta.calculate_total_value_count() |should| equal_to(False)
		conta.insert_itens(itemconta_one)
		conta.insert_itens(itemconta_two)
		conta.insert_itens(itemconta_three)
		conta.calculate_total_value_count() |should| equal_to(105)
		del conta, produto_three, produto_two, produto_one, itemconta_one, itemconta_two, itemconta_three

	def it_print_nota_fiscal(self):
		conta = Conta('25/02/2014','19:10:00','aberta',None,None,None,None,0.0,0.1,[])
		produto_one = Produto('Refrigerante','descricao','codigo',5.25,[],[])
		produto_two = Produto('Parmegiana','descricao','codigo',25.75,[],[])
		produto_three = Produto('Sorvete','descricao','codigo',9,[],[])
		itemconta_one = ItemConta(6,produto_one,conta)
		itemconta_two = ItemConta(3,produto_two,conta)
		itemconta_three = ItemConta(3,produto_three,conta)
		conta.print_nota_fiscal() |should| equal_to(False)
		conta.close_count('25/02/2014','22:00:00') |should| equal_to('Conta encerrada! Imprima e-NF!')
		conta.insert_itens(itemconta_one)
		conta.insert_itens(itemconta_two)
		conta.insert_itens(itemconta_three)
		nota_fiscal = "Data Abertura: 25/02/2014 - Hora Abertura: 19:10:00\n"
		nota_fiscal += "Qtd Produto - Valor\n"
		nota_fiscal += "06 Refrigerante X 5.25\n"
		nota_fiscal += "03 Parmegiana X 25.75\n"
		nota_fiscal += "03 Sorvete X 9.00\n"
		nota_fiscal += "Valor final: 135.75\n"
		nota_fiscal += "Data Fechamento: 25/02/2014 - Hora Fechamento: 22:00:00"
		conta.calculate_total_value_count()
		conta.print_nota_fiscal() |should| equal_to(nota_fiscal)
		del conta, produto_three, produto_two, produto_one, itemconta_one, itemconta_two, itemconta_three

class ProdutoSpec(unittest.TestCase):

	def it_creates_a_produto_object(self):
		produto = Produto('nome','descricao','codigo','preco')
		produto.nome |should| equal_to('nome')
		produto.descricao |should| equal_to('descricao')
		produto.codigo |should| equal_to('codigo')
		produto.preco |should| equal_to('preco')
		produto.itens |should| equal_to([])
		produto.categorias |should| equal_to([])
		del produto
		
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
		del mesa, produto, garcom, conta, itemconta
		
	def it_calculate_value_itemconta(self):
		produto = Produto('nome','descricao','codigo',5)
		mesa = Mesa('numero','status',[])
		garcom = Garcom('nome','endereco','telefone','cpf','identidade','matricula',[])
		conta = Conta('dd/mm/aaaa','hh:mm:ss','status',mesa,garcom,None,None,0.0,0.1,[])
		itemconta = ItemConta(1.5,produto,conta)
		itemconta.calculate_value_itemconta() |should| equal_to(7.50)
		del produto, mesa, garcom, conta, itemconta
