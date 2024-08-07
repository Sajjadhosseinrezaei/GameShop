document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('payment-form');
    var payButton = document.getElementById('pay-button');
    var payButtonText = document.getElementById('pay-button-text');
    var payButtonSpinner = document.getElementById('pay-button-spinner');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        payButtonText.classList.add('d-none');
        payButtonSpinner.classList.remove('d-none');
        payButton.disabled = true;

        setTimeout(function() {
            var cardNumber = document.getElementById('card-number').value;
            var expiryDate = document.getElementById('expiry-date').value;
            var cvv = document.getElementById('cvv').value;

            if (validateCardNumber(cardNumber) && validateExpiryDate(expiryDate) && validateCVV(cvv)) {
                alert('پرداخت با موفقیت انجام شد!');
                form.reset();
            } else {
                alert('لطفاً اطلاعات را به درستی وارد کنید.');
            }

            payButtonText.classList.remove('d-none');
            payButtonSpinner.classList.add('d-none');
            payButton.disabled = false;
        }, 3000);
    });

    function validateCardNumber(number) {
        var regex = new RegExp("^[0-9]{16}$");
        return regex.test(number);
    }

    function validateExpiryDate(date) {
        var regex = new RegExp("^(0[1-9]|1[0-2])\/?([0-9]{2})$");
        return regex.test(date);
    }

    function validateCVV(cvv) {
        var regex = new RegExp("^[0-9]{3,4}$");
        return regex.test(cvv);
    }
});
