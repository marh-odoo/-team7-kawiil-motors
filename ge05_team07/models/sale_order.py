from odoo import api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.depends('user_id', 'company_id','partner_shipping_id')
    def _compute_warehouse_id(self):
        state_distances = {
            'Alabama': 3,          
            'Alaska': 4,            
            'Arizona': 4,           
            'Arkansas': 3,         
            'California': 4,        
            'Colorado': 4,          
            'Connecticut': 3,      
            'Delaware': 3,         
            'Florida': 4,           
            'Georgia': 3,          
            'Hawaii': 4,            
            'Idaho': 4,             
            'Illinois': 3,         
            'Indiana': 3,          
            'Iowa': 3,              
            'Kansas': 3,            
            'Kentucky': 3,          
            'Louisiana': 3,         
            'Maine': 3,             
            'Maryland': 3,          
            'Massachusetts': 3,     
            'Michigan': 3,          
            'Minnesota': 3,         
            'Mississippi': 3,       
            'Missouri': 3,          
            'Montana': 4,           
            'Nebraska': 3,         
            'Nevada': 4,            
            'New Hampshire': 3,     
            'New Jersey': 3,        
            'New Mexico': 4,        
            'New York': 3,          
            'North Carolina': 3,    
            'North Dakota': 3,      
            'Ohio': 3,        
            'Oklahoma': 3,    
            'Oregon': 4,            
            'Pennsylvania': 3,
            'Rhode Island': 3,
            'South Carolina':4, 
            'South Dakota': 3,
            'Tennessee': 3,   
            'Texas': 3,       
            'Utah': 4,              
            'Vermont': 3,          
            'Virginia': 3,    
            'Washington': 4,        
            'West Virginia': 3,
            'Wisconsin': 3,   
            'Wyoming': 4,           
        }
        for order in self:
            if order.state in ['draft', 'sent'] or not order.ids:
                if order.partner_shipping_id.state_id.name in state_distances:
                    order.warehouse_id = state_distances[order.partner_shipping_id.state_id.name]
                else:
                    super()._compute_warehouse_id()