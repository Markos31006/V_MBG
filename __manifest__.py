{
	'name': 'Vehicles_MBG',
	'description': "External agents management",
	'category': 'Sales',
	'version': '1.0',
	'depends': ['base'],
	'data': [
		'data/external.agent.csv',
		'security/ir.model.access.csv',
		'views/external_agent_view.xml',
		'views/menu_view.xml',
	],
	'installable': True,
	'application': True,
	'auto_install': False
}