{
    "name": "Automatic Portal Account Creation",
    
    "summary": "Creating a portal user automatically and sending them an email to set up their credentials",
    
    "description": """
        It creates a new portal user for new customer each time an entry in motorcycle registry is created and sends an email
        to the customer to set up its credentials.
    """,
    
    "version": "0.1",
    
    "category": "Kawiil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["motorcycle_registry"],
    
    "data": [
        'data/mail_template_data.xml',
    ],
    
    "demo": [],
    
    "author": "team7",
    
    "website": "www.odoo.com",
    
    "application": False,

    "auto_install": True,
    
}