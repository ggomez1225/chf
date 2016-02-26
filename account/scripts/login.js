/**
 * Created by Jason on 2/3/2016.
 */
$(function() {
    // bind form using ajaxForm
    //console.log($('#Loginform'));
    $('#Loginform').ajaxForm({
        // target identifies the element(s) to update with the server response
        target: '#jquery-loadmodal-js-body',

        // success identifies the function to invoke when the server response
        // has been received; here we apply a fade-in effect to the new content
        success: function() {
            $('#Loginform').fadeIn('slow');
        }
    });//
});//Ready Function