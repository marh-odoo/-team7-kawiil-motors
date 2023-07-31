{
    "name": "ge10_team7",
    
    "summary": "Adds a widget to display total motorcycle mileage on a web view.",
    
    "description": """
    Total Mileage Count
====================
This Module is used to keep track of the current mileage of each motorcycle on the registry.
    """,
    
    "version": "0.1",
    
    "category": "Kawiil/Registry",
    
    "license": "OPL-1",
    
    "depends": ["motorcycle_registry", "website"],
    
    "data": [
        "views/mileage_snippet.xml",
    ],
    
    "demo": [
        "demo/motorcycle_registry_demo.xml",
        "demo/product_demo.xml",
    ],

    "assets":{
        "web.assets_frontend_2":[
            "ge10_team7/static/src/js/odometer.js",
            "ge10_team7/static/styles/odometer_theme_car.css",
            #"ge10_team7/static/styles/generic.css",
        ],
    },
    
    "author": "kawiil-motors",
    
    "website": "www.odoo.com",
    
    "application": True,
    
}