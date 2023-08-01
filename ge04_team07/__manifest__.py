{
    "name": "Discount for new motorcycle clients",
    
    "summary": "Add discount to new motorcycle clients",
    
    "description": """
    This Module is used to add a new field to indicate if some costumer has some motorcycle purchase to offer a discount in case they doesn't have.
    """,
    
    "version": "0.1",
    
    "category": "Kawiil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["motorcycle_registry", "sale"],
    
    "data": [
        'views/sale.view_order_form_inherit.xml',
        'data/new_customer_discount.xml',
    ],
    
    "demo": [
       
    ],
    
    "author": "kawiil-motors",
    
    "website": "www.odoo.com",
    
    "application": False,

    "auto_install": True,
    
}