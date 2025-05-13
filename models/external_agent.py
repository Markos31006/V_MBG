from odoo import fields, models

class ExternalAgent(models.Model):
	_name = "external.agent"
	_description = "External Agents"
	_order = "propietari"

	propietari = fields.Char('Propietari', required=True, translate=True)
	matricula = fields.Char('Matricula', required=True)
	kilometres = fields.Integer('Kilòmetres actuals')

	