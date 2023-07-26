{
    'name':'Motorcycle Filter',
    'summary':""" Add filter to see by default motorcycles in the product section""",
    'description':""" Kawiil motor TG01
    This Module is used to add a 'motorcycle' filter to the products tab and set it to be a default filter. 
       """,
    'license':'OPL-1',
    'author':'team7',
    'website':'www.odoo.com',
    'category':'Kawiil/Admin',
    'depends':['website','stock','sale'],
    'data':[
        'views/ge01_team7_filter_view.xml',
    ],
    'demo':[],
    'application': False,
}