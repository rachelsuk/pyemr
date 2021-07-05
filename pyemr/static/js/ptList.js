'use strict';

$("#search-pt").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#pt-table tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });