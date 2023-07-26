{
    'name':'ge06_team07',
    'summary':""" Create automatic Serial Number based on Motorcycles attributes """,
    'description':""" Kawiil motorcycle TG06 - Automatic Serial Numbers""",
    'license':'OPL-1',
    'author':'team7',
    'website':'www.odoo.com',
    'category':'Kawiil/Admin',
    'depends':['sale_stock','sale','mrp','motorcycle_registry'],
    'data':[
        'data/serial_number_data.xml',
    ],
    'demo':[],
    'application': True,
}