from odoo import fields, models

class ExternalAgent(models.Model):
	_name = "external.agent"
	_description = "External Agents"
	_order = "propietari"

	matricula = fields.Char('Matrícula', required=True)
	marca = fields.Char('Marca', required=True)
	model = fields.Char('Model', required=True)
	any = fields.Integer('Any de matriculació', required=True)
	kilometres = fields.Float('Quilòmetres actuals', required=True)
	ITV = fields.Boolean('ITV passada', required=True)
	propietari = fields.Char('Propietari', required=True, translate=True)
	DNI = fields.Char('DNI del propietari', required=True)
	