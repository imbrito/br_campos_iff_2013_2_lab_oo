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
