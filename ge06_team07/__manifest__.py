{
    'name':'Automatic Serial Number based on VIN',
    'summary':""" Create automatic Serial Number based on Motorcycles attributes """,
    'description':""" Kawiil motorcycle TG06 - Automatic Serial Numbers""",
    'license':'OPL-1',
    'author':'team7',
    'website':'www.odoo.com',
    'category':'Kawiil/Admin',
    'depends':['sale_stock','sale','mrp','motorcycle_registry'],
    'data':[
        'data/stock_lot_data.xml',
    ],
    'demo':[],
    'application': False,
    'auto_install': True,
}