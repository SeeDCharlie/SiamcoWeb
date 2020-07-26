$(function(){

    $('.boton_entrar').on('click', function(){
      alert("alv!!");
      $.ajax({
        url : "{% url 'homeLoggin' %}",
        type : 'POST',
        data : {success : false},
        dataType : 'json',
        success : (function(data){

          console.log(data)
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

