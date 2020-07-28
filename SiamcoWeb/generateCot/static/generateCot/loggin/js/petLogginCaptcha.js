$(function(){

    $('.boton_entrar').click( function(){
      val dats
      $.ajax({
        url : "{% url 'mainCot' %}",
        type : 'POST',
        data : {success : false},
        dataType : 'json',
        success : (function(data){

          if (!data['success']){
            alert("Marque el cuadro captcha!!!");
          }else{
            alert("si marco el captcha!!")
          }
  
        }).fail(function(){
          alert("todo esta mal!!")
        })

      })

    });

});

