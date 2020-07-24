$("#g-recaptcha-response").change(function () {
    var captcha = $(this).val();
    $.ajax({

        url: "{% url 'mainCot' %}",
        data :{'captcha' : captcha},
        dataType: 'json',
        
        success: function (data) {

            if(!data["valid"]){
                alert("Please check the captcha box!!");
            }
            else {
                alert("Biennnn!! caremonda!!")
            }
        },
        error: function (data) {
            console.log(" alv 404 !! ")
            alert("error!!! 404!")
        }
    })
})