function builRow(dats) {
    var row = '';
    row += '<tr>';
    $.each(dats, function (idx, dat) {
        row += '<td id="dat' + idx + '">' + dat + '</td>';
    });
    row += '<td id="dat4">' + parseInt(dats[2], 10) * parseInt(dats[3], 10) + '</td>';
    row = row + '<td> <button type="button" class="btn fa fa-times-circle" style="color: red;"  value=""> </button> </td>';
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

    $('#tmom').html(":$" + dat);
    $('#ta').html(":$" + (dat * 0.11));
    $('#ti').html(":$" + (dat * 0.05));
    $('#tu').html(":$" + (dat * 0.05));
    $('#tiu').html(":$" + (dat * 0.19));
    $('#tdi').html(":$" + (dat + (dat * 0.11) + (dat * 0.05) + (dat * 0.05) + (dat * 0.19)));

}

$(document).ready(function () {
    $('.tAdd').toast({delay: 1000});
    $('.tRem').toast({delay: 1000});
    new FroalaEditor("#editText", {
        fullPage: true,
    });

});

$(document).on('click', '#tableuno button', function (e) {
    var buttonVal = $(this).val();
    //alert("add buttom:" );

    dats = [
        $("#d" + buttonVal).html(),
        $("#u" + buttonVal).html(),
        $("#c" + buttonVal).val(),
        $("#v" + buttonVal).val()
    ];
    if (!$.isNumeric(dats[2]) || !$.isNumeric(dats[3])) {
        $('#modalAlert').modal();
    }
    else {
        appendRow(builRow(dats));
        changeValueCot();
        $('.tAdd p').html('Actividad <strong>'+ buttonVal + '</strong> Añadida');
        $('.tAdd').toast('show');
    }
});

$(document).on('click', '.tabledos button', function () {
    $('.tRem').toast('show');
    $(this).parent().parent().remove();
    changeValueCot();
});


