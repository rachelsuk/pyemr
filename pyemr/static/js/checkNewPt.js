'use strict';

$("#new-pt-form").on("submit", function(evt) {

    evt.preventDefault();

    let url = "/ptchart/check-new-pt/";
    let formData = $(this).serialize();

    console.log(formData);

    $.post(url, formData, (response) => {
        console.log(response);
        // if (response) {
        //     alert('Pt already exists.');
        // };
    });

});