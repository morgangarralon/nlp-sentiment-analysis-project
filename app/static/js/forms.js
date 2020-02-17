// userInputForm
$(document).ready(function() {
    console.log('total');
    $('#submit').click(function() {
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
    });
});