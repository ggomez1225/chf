$(function(){
    $('.datetimepicker').datepicker();
});

$('.delete_button').click(function(stop){
    stop.preventDefault();
    var Nhref = $(this).attr('href');

    $('#confirm_delete_button').attr('href', Nhref);
    $('#delete_modal').modal({show: true});
    return false;
});
