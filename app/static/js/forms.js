function printInDiv(id, input_html) {
    document.getElementById(id).innerHTML= input_html;
}

function submitForm() {
    form = $('form')
    
    $.ajax({
        url: '/result',
        data: form.serialize(),
        type: 'POST',
        success: function(response) {
            printInDiv("result", "result: " + response)
        },
        error: function(error) {
            console.log(error);
            $.ajax({
                url: '/result',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    printInDiv("result", "result: " + response)

                    return true;
                },
                error: function(error) {
                    console.log(error);

                    return false;
                }
            });
        }
    }); 
}

// userInputForm
$(document).ready(function() {
    console.log('total');
    $(document).on("keydown", "form", function(event) { 
        if (event.key == "Enter") {
            i = 0
            result = false;
            while(!result & i < 20) {
                result = submitForm();
                i++;
            }
            event.preventDefault();
        }
    });
    $('#submit').click(function() {
        form = $('form')
        input_guess = form.find("#input-guess #field_data_input").val()

        if(input_guess.length > 2) {
            $.ajax({
                url: '/result',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    document.getElementById("result").innerHTML= "result: " + response;
                },
                error: function(error) {
                    console.log(error);
                    i = 0
                    result = false;
                    while(!result & i < 20) {
                        result = submitForm();
                        i++;
                    }
                }
            })
        } else {
            printInDiv("result", "please, type a lengther word (>2)")
        }
    })
})