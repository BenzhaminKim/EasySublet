
$('#park-yes').click(function () {
    $('#id_is_parking').prop('checked', true);
    $('#park-yes').removeClass('btn-outline-primary').addClass('btn-primary');
    $('#park-no').removeClass('btn-primary').addClass('btn-outline-primary');
});
$('#park-no').click(function () {
    $('#id_is_parking').prop('checked', false);
    $('#park-yes').removeClass('btn-primary').addClass('btn-outline-primary');
    $('#park-no').removeClass('btn-outline-primary').addClass('btn-primary');
});
$('#pet-yes').click(function () {
    $('#id_is_pet').prop('checked', true);
    $('#pet-yes').removeClass('btn-outline-primary').addClass('btn-primary');
    $('#pet-no').removeClass('btn-primary').addClass('btn-outline-primary');
});
$('#pet-no').click(function () {
    $('#id_is_pet').prop('checked', false);
    $('#pet-yes').removeClass('btn-primary').addClass('btn-outline-primary');
    $('#pet-no').removeClass('btn-outline-primary').addClass('btn-primary');
});
$('#smoking-yes').click(function () {
    $('#id_is_smoking').prop('checked', true);
    $('#smoking-yes').removeClass('btn-outline-primary').addClass('btn-primary');
    $('#smoking-no').removeClass('btn-primary').addClass('btn-outline-primary');
});
$('#smoking-no').click(function () {
    $('#id_is_smoking').prop('checked', false);
    $('#smoking-yes').removeClass('btn-primary').addClass('btn-outline-primary');
    $('#smoking-no').removeClass('btn-outline-primary').addClass('btn-primary');
});

$('#Hydro').click(function () {
    if ($('#id_has_hydro').prop("checked") == true) {
        $('#id_has_hydro').prop('checked', false);
        $('#Hydro').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_hydro').prop('checked', true);
        $('#Hydro').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Airconditioning').click(function () {
    if ($('#id_has_aircondition').prop("checked") == true) {
        $('#id_has_aircondition').prop('checked', false);
        $('#Airconditioning').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_aircondition').prop('checked', true);
        $('#Airconditioning').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Water').click(function () {
    if ($('#id_has_water').prop("checked") == true) {
        $('#id_has_water').prop('checked', false);
        $('#Water').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_water').prop('checked', true);
        $('#Water').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Heat').click(function () {
    if ($('#id_has_heat').prop("checked") == true) {
        $('#id_has_heat').prop('checked', false);
        $('#Heat').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_heat').prop('checked', true);
        $('#Heat').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Wifi').click(function () {
    if ($('#id_has_wifi').prop("checked") == true) {
        $('#id_has_wifi').prop('checked', false);
        $('#Wifi').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_wifi').prop('checked', true);
        $('#Wifi').toggleClass('btn-outline-primary btn-primary');
}
});
$('#TV').click(function () {
    if ($('#id_has_tv').prop("checked") == true) {
        $('#id_has_tv').prop('checked', false);
        $('#TV').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_tv').prop('checked', true);
        $('#TV').toggleClass('btn-outline-primary btn-primary');
}
});

$('#Landuary').click(function () {
    if ($('#id_has_laundry').prop("checked") == true) {
        $('#id_has_laundry').prop('checked', false);
        $('#Landuary').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_laundry').prop('checked', true);
        $('#Landuary').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Dryer').click(function () {
    if ($('#id_has_dryer').prop("checked") == true) {
        $('#id_has_dryer').prop('checked', false);
        $('#Dryer').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_dryer').prop('checked', true);
        $('#Dryer').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Dishwasher').click(function () {
    if ($('#id_has_dishwasher').prop("checked") == true) {
        $('#id_has_dishwasher').prop('checked', false);
        $('#Dishwasher').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_dishwasher').prop('checked', true);
        $('#Dishwasher').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Fridge').click(function () {
    if ($('#id_has_fridge').prop("checked") == true) {
        $('#id_has_fridge').prop('checked', false);
        $('#Fridge').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_fridge').prop('checked', true);
        $('#Fridge').toggleClass('btn-outline-primary btn-primary');
}
});
$('#Microwave').click(function () {
    if ($('#id_has_microwave').prop("checked") == true) {
        $('#id_has_microwave').prop('checked', false);
        $('#Microwave').toggleClass('btn-primary btn-outline-primary');
    } else {
        $('#id_has_microwave').prop('checked', true);
        $('#Microwave').toggleClass('btn-outline-primary btn-primary');
}
});