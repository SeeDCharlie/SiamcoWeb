
$(function () {

  $(document).on('click', '#boton_entrar', function (e) {

    e.preventDefault();
    $.ajax({
      url: $("#boton_entrar").attr('urlDestinity'),
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
          location.reload();
        }
        else{
          if(!data.userValidate){
            alert("Usuario o Contraseña Incorrectos");
            location.reload();
          }
          else{
            $('#f_loggin').submit();

          }
        }
        
      },
      error: function () {
        console.log("no paso nada con el ajax!!");
      }

    });

  });

});

