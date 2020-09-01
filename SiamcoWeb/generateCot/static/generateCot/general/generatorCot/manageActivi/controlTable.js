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
                    showModalSucces('Se Eliminaron ' + data.cant + ' Registros');
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

function showErrorUpdate(msj) {
    $('.teUno p').html(msj);
    $('.teUno').toast('show');
}

$('.btnUpdate').on('click', function (e) {
    e.preventDefault(e);

    var descrip = $('#eDescription').val();
    var und = $('#eLunds').val();
    var value = $('#eValorund').val();

    if (descrip == '' || und == '' || value == '') {
        showErrorUpdate('Hay Campos Vacios!');
    }
    else {
        if ($.isNumeric(value)) {
            var dats = [descrip, und, value, $('.btnUpdate').val()];
            $.ajax({
                url: $(this).attr('url'),
                data: {
                    dats: JSON.stringify(dats),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
                type: 'POST',
                dataType: 'json',
                success: function (data) {
                    if (data.echo) {
                        $('.teDos').toast('show');
                        setTimeout(function () {
                            location.reload();
                        }, 1000);
                    }else{
                        alert('No se pudo actualizar el Registro!');
                    }
                },
                error: function () {
                    alert("no paso nada con el ajax!!");
                }
            });
        }
        else {
            showErrorUpdate('Valor Unitario Incorrecto<br>Por Favor Digite Numeros Validos!');
        }
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

$('.btnAdd').on('click', function (e) {
    $('#modalAdd').modal();
});

$('.btnEdit').on('click', function (e) {
    var actis = getChecked();
    if (actis.length == 0 || actis.length > 1) {
        showModalError('Por Favor Seleccione Solo Una Actividad!');
    } else {
        var dats = []
        $('#tableuno input:checked').parents('tr').find('td').each(function () {
            dats.push(this.innerHTML);
        });
        $('#modalEdit h5').html('Actividad <strong>' + dats[1] + '</strong>')
        $('.btnUpdate').val(dats[1]);
        $('#eDescription').val(dats[2]);
        $('#eLunds').val(dats[3]);
        $('#eValorund').val(dats[4]);
        $('#modalEdit').modal();
    }
});