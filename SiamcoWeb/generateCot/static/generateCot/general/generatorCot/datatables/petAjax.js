//send data to server
$(function () {

    $(document).on('click', '#bGenerate', function (e) {
        e.preventDefault(e);
        var date = new Date();
        date = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDay(); 
        durationW = $("#dProject").val();
        if (!$.isNumeric(durationW)){
            durationW = 0;
        }

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
                    durationWork: durationW,
                    unitDuration: $("#dUnd").val(),
                    autorName: $("#fName").text() + $("#lName").text(),
                    username: $('#UsernameAux').text(),
                    dateToday:  date,
                    //otherStyle: $('iframe').contents().find('head').find('style').html()
                    textCot : $('iframe').contents().find('body').html()

                }),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if(data.isRender){

                    alert("okPdf username : "+ data.username);
                    
                    $('#f_generateCot').append('<input type="hidden" name="username" value="'+data.username+'" />');
                    $('#f_generateCot').submit();

                }
            },
            error: function () {
                alert("no paso nada con el ajax!!");
            }

        });

     


    });

});