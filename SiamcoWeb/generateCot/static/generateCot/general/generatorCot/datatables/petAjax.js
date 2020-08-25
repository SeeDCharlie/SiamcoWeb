//send data to server
$(function () {

    $(document).on('click', '#bGenerate', function (e) {
        e.preventDefault(e);
        var date = new Date();
        date = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDay();
        durationW = $("#dProject").val();
        if (!$.isNumeric(durationW)) {
            durationW = 0;
        }
        var al = getListActivities();
        var totalCot = [
            $('#tmom').text().substr(2),
            $('#ta').text().substr(2),
            $('#ti').text().substr(2),
            $('#tu').text().substr(2),
            $('#tiu').text().substr(2),
            $('#tdi').text().substr(2)
        ];
        
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
                    dateToday: date,
                    actiList: al,
                    totals : totalCot,
                    //otherStyle: $('iframe').contents().find('head').find('style').html()
                    textCot: getTextCot(),
                    textNote: $('#textNote').val()

                }),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.isRender) {

                    $('#f_generateCot').append('<input type="hidden" name="username" value="' + data.username + '" />');
                    $('#f_generateCot').submit();

                }
            },
            error: function () {
                alert("no paso nada con el ajax!!");
            }

        });

    });

    function getListActivities() {
        var dataStore = [];
        $('#tabledos tbody tr').each(function (idx,dat) {
            var td = [$(this).find("#dat0").text(),
            $(this).find("#dat1").text(),
            $(this).find("#dat2").text(),
            $(this).find("#dat3").text(),
            $(this).find("#dat4").text(),
            ];
            
            dataStore.push(td);
        });
        return dataStore;

    }
    function getTextCot(){
        $('iframe').contents().find('table').addClass("tableDos");
        return $('iframe').contents().find('body').html();
    }

});