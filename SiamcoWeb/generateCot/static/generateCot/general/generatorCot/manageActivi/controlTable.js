$(document).on('click', '#bGenerate', function (e) {
    e.preventDefault(e);

    $.ajax({
        url: $("#bGenerate").attr('urlDestinity'),
        data: {

            datsCot: JSON.stringify({

            }),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
         
        },
        error: function () {
            alert("no paso nada con el ajax!!");
        }

    });

});
