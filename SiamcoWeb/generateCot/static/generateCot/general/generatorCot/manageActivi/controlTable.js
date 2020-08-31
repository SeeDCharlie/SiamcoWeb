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


$('.btnDelete').on('click', function () {
    var actis = getChecked();
    if (actis.length == 0) {
        showModalError('Ninguna Actividad Seleccionada!');
    }
    else {
        $.ajax({
            url: $(this).attr('url'),
            data: {
                dats: JSON.stringify(actis),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.echo) {
                    showModalSucces('Se Eliminaron ' + data.cant + 'Registros');
                    setTimeout(function () {
                        location.reload();
                    }, 1000);
                }
                else {
                    alert("no se elimino nada");
                }
            },
            error: function () {
                alert("no paso nada con el ajax!!");
            }
        });
    }

});

function getChecked() {
    var checkeds = [];
    $('#tableuno input:checked').each(function () {
        checkeds.push($(this).val());
    });
    return checkeds;
}

function showModalSucces(msj) {
    $('#modalSucces p').html(msj);
    $('#modalSucces').modal();
}

function showModalError(msj) {
    $('#modalAlert p').html(msj);
    $('#modalAlert').modal();
}