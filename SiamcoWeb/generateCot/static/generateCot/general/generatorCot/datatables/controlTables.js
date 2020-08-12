

$(document).ready(function () {

    new FroalaEditor("#editText", {
        fullPage: true,
    });
});


function builRow(dats, id) {
    var row = '<tr id ="rcot"+id>';

    $.each(dats, function (idx, dat) {
        row += '<td>' + dat + '</td>';
    });
    row += '<td>' + parseInt(dats[2], 10) * parseInt(dats[3], 10) + '</td>';
    row += '<td> <button type="button" class="btn"  value="' + id + '"><i class="fa fa-times-circle" style="color: red;" aria-hidden="true" i> </button> </td>';

    row += "<tr>";
    return row;
}

function appendRow(row) {
    var table = $("#tabledos tbody");
    table.append(row);
}

$('button').click(function (e) {

    var buttonVal = $(this).val();
    var parent = $(this).parent().get(0).tagName;
    ///alert("valor del boton : " + buttonVal + " parent name : " );

    if (parent == "TD") {


        dats = [
            $("#d" + buttonVal).html(),
            $("#u" + buttonVal).html(),
            $("#c" + buttonVal).val(),
            $("#v" + buttonVal).val()
        ];

        if (!$.isNumeric(dats[2]) || !$.isNumeric(dats[3])) {
            alert("Cantidad o Valor incorrectos : Por favor digite numeros correctos");
        }
        else {
            appendRow(builRow(dats, buttonVal));
        }
    }

});



