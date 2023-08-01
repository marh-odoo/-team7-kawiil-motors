{
    'name':'Automatic Warehouse Assignment',
    'summary':""" Assign Automatic Warehouse depending the customer location.""",
    'description':""" 
        When setting up the sale order if the customer has an US address a warehouse will be automatically assigned depending 
        on its location.
    """,
    'license':'OPL-1',
    'author':'team7',
    'website':'www.odoo.com',
    'category':'Kawiil/Admin',
    'depends':['sale_stock','sale'],
    'data':[],
    'demo':[],
    'application': False,
    'auto_install': True,
}