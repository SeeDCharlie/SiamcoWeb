//send data to server

$(function () {

    $(document).on('submit', '#f_generateCot', function (e) {
        e.preventDefault();

        $.ajax({
            url: $("#bGenerate").attr('urlDestinity'),
            data: {

                datsCot: JSON.stringify({
                    customerName: $("#nClient").val(),
                    customerEmail: $("#emClient").val(),
                    placeName: $("#nPlace").val(),
                    placeAddress: $("#dPlace").val(),
                    projectName: $("#nProject").val(),
                    proposalNumber: $("#nPropuesta").val(),
                    durationWork: $("#dProject").val(),
                    unitDuration: $("#dUnd").val(),
                    autorName : $("#fName").val() + $("#lName").val(),
                    dateToday : new Date(),
                }),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                alert("hahahhaha se enviaron los datos hpta!!");
            },
            error: function () {
                alert("no paso nada con el ajax!!");
            }

        });

    });

});
