{
    "name": "Manufacturing Enhancements",
    
    "summary": "On delivery confirmed it creates a new motorcycle registry",
    
    "description": """
        Each time we confirm a delivery order we will create a new motorcyle registry entry. It relates the lot_id with
        the vin
    """,
    
    "version": "0.1",
    
    "category": "Kawiil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["stock", "sale","motorcycle_registry"],
    
    "data": [
        'views/stock_lot_views.xml',
        'views/motorcycle_registry_views.xml',
    ],
    
    "demo": [],
    
    "author": "team7",
    
    "website": "www.odoo.com",
    
    "application": False,

    "auto_install": True,
    
}