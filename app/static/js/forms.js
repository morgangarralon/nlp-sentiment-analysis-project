function submitForm() { 
    $.ajax({
        url: '/result',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response) {
            document.getElementById("result").innerHTML= "result: " + response;
        },
        error: function(error) {
            console.log(error);
            $.ajax({
                url: '/result',
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    console.log(response);
                    document.getElementById("result").innerHTML= "result: " + response;
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    });
 };

// userInputForm

$(document).ready(function() {
    console.log('total');
    $('#submit').click(function() {
        $.ajax({
            url: '/result',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                document.getElementById("result").innerHTML= "result: " + response;
            },
            error: function(error) {
                console.log(error);
                for(i=0; i<5; i++) {
                    submitForm()
                }
            }
        })
    })
})