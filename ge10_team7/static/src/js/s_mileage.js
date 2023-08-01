odoo.define('ge10_team7.mileage', ['web.ajax'], (require) => {
        "use strict";
        let ajax = require('web.ajax');
        $(document).ready(() => {
            let container = document.getElementById('odometer');
            if(container){
                container.innerHTML = '';
                container.innerHTML = '<div class="col text-center">Loading...</div>';
                ajax.jsonRpc( '/get_mileage_count', 'call', {}).then(data => {
                    container.innerHTML = `${String(data).padStart(7,'0')}`;
                })
            }
        })
    } 
);


