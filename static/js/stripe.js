// stripe.js

document.addEventListener('DOMContentLoaded', function () {
    var stripe = Stripe('pk_test_51OGvLoBfoLOjTuhJWWx8cnFFSDuJNXTaymUEe8fBWLcjZNbYtGDCw400Sf76gmKHQzeqlrGVYfyHW0lc82jy5BJ100VIfvEmBc');
    var elements = stripe.elements();

    var card = elements.create('card');
    card.mount('#card-element');

    card.addEventListener('change', function (event) {
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    });

    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        document.getElementById('submit-button').disabled = true;

        stripe.confirmCardPayment(form.client_secret.value, {
            payment_method: {
                card: card,
            }
        }).then(function (result) {
            if (result.error) {
                // Show error to your customer.
                displayError.textContent = result.error.message;
                // Enable the submit button.
                document.getElementById('submit-button').disabled = false;
            } else {
                // The payment succeeded!
                if (result.paymentIntent.status === 'succeeded') {
                    // Handle successful payment and order completion logic.
                    // For example, you might redirect the user to an order confirmation page.
                    window.location.href = '/order_confirmation/';
                }
            }
        });
    });
});
