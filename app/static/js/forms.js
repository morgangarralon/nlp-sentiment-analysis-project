function printInDiv(id, input_html) {
    document.getElementById(id).innerHTML = input_html;
}

function submitForm() {
    form = $('form')
    
    $.ajax({
        url: '/result',
        data: form.serialize(),
        type: 'POST',
        success: function(response) {
            printInDiv("result-content", response)
            printInDiv('loader-container', '')
            if($('#result-negative').length) {
                guess_result = 'negative';
            } else if ($('#result-positive').length) {
                guess_result = 'positive';
            } else {
                guess_result = 'error';
            }
        },
        error: function(error) {
            guess_result = null;
        }
    }); 
}

function validateForm() {
    form = $('form')
    input_guess = form.find("#input-guess #field_data_input").val()

    if(input_guess.length > 2) {
        $.ajax({
            url: '/result',
            data: form.serialize(),
            type: 'POST',
            beforeSend: function() {
                printInDiv('loader-container', '<span id="loader"></span>');
            },
            success: function(response) {
                printInDiv("result-content", response)
                printInDiv('loader-container', '')
                if($('#result-negative').length) {
                    guess_result = 'negative';
                } else if ($('#result-positive').length) {
                    guess_result = 'positive';
                } else {
                    guess_result = 'error';
                }
            },
            error: function(error) {
                i = 0
                result = false;
                while(!result & i < 20) {
                    result = submitForm();
                    i++;
                }
                guess_result = null;
            }
        })
    } else {
        guess_result = null;
        printInDiv("result-content", '<div id="error-input">Please, type a lengther word (>2)</div>')
    }
}

// userInputForm
$(document).ready(function() {
    $(document).on("keydown", "form", function(event) { 
        if (event.key == "Enter") {
            validateForm();
            event.preventDefault();
        }
    });
    $('#submit').click(function() {
        validateForm();
    })
})