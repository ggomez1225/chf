/**
 * Created by Jason on 2/3/2016.
 */
$(function () {
    $('#loginbutton').click(function(){
        $.loadmodal({
          url: '/account/login',
          id: 'loginmodal',
          title: 'Login',
          width: '400px',
        });//loadmodal
    });//click function

});//ready function
