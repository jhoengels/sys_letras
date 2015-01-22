#!/usr/bin/python
# -*- encoding: utf-8 -*-

import time
from openerp.osv import fields, osv
from tools.translate import _

TIPO_DIRECCION = [('factura','Facturación'),
	('entrega', 'Entrega'),
	('otro', 'Otro')
]

class sys_direccion(osv.Model):
	_name = 'sys.direccion'
	_columns = {
		'name': fields.char('Nombre', size=64, required=True, Translate=True),
		'tipo': fields.selection(TIPO_DIRECCION, 'Tipo Dirección'),
		'direccion': fields.char('Dirección', size=225),
		'telefono': fields.char('Teléfono', size=11),
		#'tercero_ids': fields.one2many('sys.tercero', 'direccion_ids', 'Tercero de la Dirección'),
		#'tercero_id': fields.many2one('sys.tercero', 'Tercero', required=True,
        #   ondelete='cascade', select=True),
		'direccion_tercero_ids': fields.one2many('sys.direccion.tercero', 'direccion_id', 'Direccion_tercero'),
	}

class sys_tercero(osv.Model):
	_name = 'sys.tercero'
	_columns = {
		'name': fields.char('Nombre', size=64, required=True, Translate=True),
		'doc_numero': fields.char('N° Documento', size=11),
		'empresa': fields.boolean('Es empresa', help="Marque si se trata de una empresa"),
		'cliente': fields.boolean('Cliente', help="Marque si se trata de un cliente"),
		'proveedor': fields.boolean('Proveedor', help="Marque si se trata de un proveedor"),
		'active': fields.boolean('Activo'),
		'telefono': fields.char('Teléfono', size=11),
		'correo': fields.char('Correo', size=240),
		'web': fields.char('Sitio Web', size=64),
		'puesto': fields.char('Puesto de trabajo', size=64),
		'parent_id': fields.many2one('sys.tercero', 'Related Company', select=True),
        'child_ids': fields.one2many('sys.tercero', 'parent_id', 'Contactos', domain=[('active','=',True)]),
        #'direccion_ids': fields.one2many('sys.direccion', 'tercero_id', 'Direcciones'),
        'direccion_tercero_ids': fields.one2many('sys.direccion.tercero', 'tercero_id', 'Direccion_tercero'),
	}

	_defaults = {
			'active':1,
		}
		
class sys_direccion_tercero(osv.Model):
	_name = 'sys.direccion.tercero'
	_columns = {
		'name': fields.char('Nombre', size=64, required=True, Translate=True),
		'direccion_id': fields.many2one('sys.direccion', 'Dirección', select=True),
		'tercero_id': fields.many2one('sys.tercero', 'Tercero', required=True,
           ondelete='cascade', select=True),
	}