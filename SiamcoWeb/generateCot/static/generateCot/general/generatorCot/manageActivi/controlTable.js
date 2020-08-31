$(document).ready(function () {
    $('.tUno').toast({ delay: 1500 });
    $('.tDos').toast({ delay: 1500 });
    $('.tTres').toast({ delay: 1500 });
});

$(document).on('click', '.btnSave', function (e) {
    e.preventDefault(e);

    var descrip = $('#description').val();
    var und = $('#lunds').val();
    var value = $('#valorund').val();

    if (descrip != '' && und != '' && value != '') {
        if ($.isNumeric(value)) {
            $.ajax({
                url: $(this).attr('url'),
                data: {
                    dats: JSON.stringify({
                        descrip: descrip,
                        und: und,
                        value: value
                    }),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
                type: 'POST',
                dataType: 'json',
                success: function (data) {
                    if (data.save) {
                        $('.tTres').toast('show');
                        setTimeout(function () {
                            location.reload();
                        }, 1000);
                    }
                    else {
                        alert('no se pudo guardar la actividad');
                    }
                },
                error: function () {
                    alert("no paso nada con el ajax!!");
                }
            });
        }
        else {
            $('.tDos').toast('show');
        }
    }
    else {
        $('.tUno').toast('show');
    }

});

$('.btnAdd').on('click', function (e) {
    $('#modalAdd').modal();
});
