{
    "name": "Motorcyle Repair Enhancements",
    
    "summary": "Able to read the VIN, and have the rest of the information populate from the registry since repairs app",
    
    "description": """
        Read the VIN, and have the rest of the information populate from the registry, keep track of the motorcycle mileage each time the motorcycle is brought in for repairs and maintenance, and update the mileage on the registry with the latest value in repairs app.
    """,
    
    "version": "0.1",
    
    "category": "Kawiil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["stock", "sale","motorcycle_registry", "repair"],
    
    "data": [
        'views/repair_view_repair_order_tree_inherit.xml',
        'views/motorcycle_registry_view_form_inherit.xml'
    ],
    
    "demo": [],
    
    "author": "team7",
    
    "website": "www.odoo.com",
    
    "application": False,

    "auto_install": True,
    
}