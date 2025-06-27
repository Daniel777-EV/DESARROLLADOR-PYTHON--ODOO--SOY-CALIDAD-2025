odoo.define('pos_custom_features.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var PosDb = require('point_of_sale.PosDb'); // Para asegurar que el idioma se cargue en la base de datos del POS

    // Extender el modelo de cliente para asegurar que el campo 'lang' se cargue
    models.load_fields('res.partner', ['lang']);

    // Puede que necesites extender PosDb para asegurar que el campo 'lang' se indexe si no lo hace automáticamente
    // Esto es más avanzado y podría no ser necesario si solo se muestra.
    // var _partner_search_string = PosDb.prototype._partner_search_string;
    // PosDb.prototype._partner_search_string = function(partner){
    //     var str = _partner_search_string.apply(this, arguments);
    //     if (partner.lang) {
    //         str += '|' + partner.lang;
    //     }
    //     return str;
    // };

});