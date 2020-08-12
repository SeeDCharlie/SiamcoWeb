
$(function () {

  $(document).on('submit', '#f_loggin', function (e) {
    e.preventDefault();
    $.ajax({
      url: $(".boton_entrar").attr('urlDestinity'),
      data: {
        captchaCheck: grecaptcha.getResponse(),
        username: $("#username").val(),
        userpass: $("#userpass").val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        action: 'post'
      },
      type: 'POST',
      dataType: 'json',
      success: function (data) {

        if(!data.success){
          alert("Por Favor Marque la Caja Captha!");
        }
        else{
          if(!data.userValidate){
            alert("Usuario o Contraseña Incorrectos");
          }
        }
        
      },
      error: function () {
        console.log("no paso nada con el ajax!!");
      }

    });

  });

});

