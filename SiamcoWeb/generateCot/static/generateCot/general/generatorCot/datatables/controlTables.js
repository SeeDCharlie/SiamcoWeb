

$(document).ready(function () {

    new FroalaEditor("#editText", {
        fullPage: true,
    });

    function builRow(dats) {
        var row = '';

        row += '<tr>';
        $.each(dats, function (idx, dat) {

            row += '<td id="dat' + idx + '">' + dat + '</td>';
        });
        row += '<td id="dat4">' + parseInt(dats[2], 10) * parseInt(dats[3], 10) + '</td>';
        row += '<td> <button type="button" class="btn"  value=" "><i class="fa fa-times-circle" style="color: red;" aria-hidden="true" i> </button> </td>';

        row += "<tr>";


        return row;
    }

    function appendRow(row) {
        var table = $("#tabledos tbody");
        table.append(row);
    }

    function getSum() {
        var sum = 0;
        $('#tabledos tbody tr').each(function (idx, dat) {
            var vt = $(this).find("#dat4").text();

            if ($.isNumeric(vt)) {
                sum += parseFloat(vt);
            }

        });
        return sum;
    }

    function changeValueCot() {
        var dat = getSum();

        $('#tmom').html(":$"+(dat*1.0))  ;
        $('#ta').html(":$"+(dat*0.11))  ;
        $('#ti').html(":$"+(dat*0.05))  ;
        $('#tu').html(":$"+(dat*0.05))  ;
        $('#tiu').html(":$"+(dat*0.19))  ;
        $('#tdi').html(":$"+((dat + dat*0.05)+(dat*0.11)+(dat*0.05)+(dat*0.05)+(dat*0.19) ))  ;
      

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


                appendRow(builRow(dats));
                changeValueCot();

            }
        }

    });


});


