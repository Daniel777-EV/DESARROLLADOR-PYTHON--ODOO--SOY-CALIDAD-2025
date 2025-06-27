odoo.define('pos_custom_features.screens', function (require) {
    "use strict";


    const PaymentScreen = require('point_of_sale.PaymentScreen');

    const PaymentScreenInheritBoleta = (PaymentScreen) => class extends PaymentScreen {
        async _onClickBoleta() {
            const currentOrder = this.env.pos.get_order();
            const totalAmount = currentOrder.get_total_with_tax();

            await Gui.showPopup('ConfirmPopup', {
                title: 'Confirmar Boleta',
                body: `El monto total a pagar para la boleta es S/ ${totalAmount.toFixed(2)}. ¿Desea continuar?`,
                confirmText: 'Aceptar',
                cancelText: 'Cancelar',
            });
            // Aquí podrías añadir lógica para marcar la orden como "Boleta"
            // o cambiar el tipo de documento antes de la validación final.
            // Por ejemplo, currentOrder.set_doc_type('boleta');
        }
    };
    PaymentScreen.add_mixin(PaymentScreenInheritBoleta);




    

    var PosComponent = require('point_of_sale.PosComponent');
    var ProductScreen = require('point_of_sale.ProductScreen');
    var { useListener } = require('@web/core/utils/hooks');
    const { Gui } = require('point_of_sale.Gui'); // Para usar popups

    const ProductScreenInherit = (ProductScreen) => class extends ProductScreen {
        setup() {
            super.setup();
            // Hook para escuchar el evento de añadir producto
            useListener('click', '.product-card', this._onClickProduct);
        }

        async _onClickProduct(event) {
            const product = event.detail; // El producto que se intentó añadir
            if (product.price === 0.0) { // O product.lst_price si es el precio de venta configurado
                await Gui.showPopup('ErrorPopup', {
                    title: 'Advertencia de Precio',
                    body: `El producto "${product.display_name}" tiene un precio de S/ 0.00.`,
                });
                // Opcional: podrías prevenir la adición o pedir confirmación
                // return; // Si quieres detener la adición
            }
            // Continuar con la lógica original de añadir producto
            super._onClickProduct(event);
        }
    };

    ProductScreen.add_mixin(ProductScreenInherit);

});





/*

Nota:
Si estás usando una versión de Odoo más antigua (anterior a Odoo 14/15),
la forma de extender componentes de JS podría ser diferente
(usando PosWidget.extend y screens.ScreenWidget).

*/