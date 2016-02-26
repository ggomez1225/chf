/**
 * Created by Jason on 2/16/2016.
 */
$('.delete_button').click(function(stop){
    stop.preventDefault();
    var Nhref = $(this).attr('href');

    $('#confirm_delete_button').attr('href', Nhref);
    $('#delete_modal').modal({show: true});
    return false;
});

$('.refresh_button').click(function(e) {
    e.preventDefault();
    var href = $(this).attr("href");//getting id
      $(this).siblings('.quantity').load(href);
 });
