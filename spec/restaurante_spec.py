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
		produto = Produto('descricao','codigo','preco')
		produto.descricao |should| equal_to('descricao')
		produto.codigo |should| equal_to('codigo')
		produto.preco |should| equal_to('preco')
		produto.itens |should| equal_to([])
		produto.categorias |should| equal_to([])

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
