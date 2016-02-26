$("#id_ptype").on('load', function() {
    var ptype = $('#id_ptype').val();
    $('#id_creator').closest('p').toggle(ptype == 'IndividualProduct');
    $('label[for="id_creator"]').toggle(ptype == 'IndividualProduct');
    $('#id_quantity').closest('p').toggle(ptype == 'BulkProduct');
    $('label[for="id_quantity"]').toggle(ptype == 'BulkProduct');
    $('#id_status').closest('p').toggle(ptype == 'RentalProduct');
    $('label[for="id_status"]').toggle(ptype == 'RentalProduct');
});
