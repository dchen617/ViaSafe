$(document).ready(function(){
    $(":button").css("top", "10px");
    $("#map").css("transform", "scale(1)");
    $("#map").css("opacity", "1");
    
    $("#searchbutton").click(function() {
        $(":button").css("top", "-64px");
        $("#searchbar").css("top", "0px");
        $("#searchbar").select();
    });
});

$(document).on("keyup", "#searchbar", function(e) {
     if (e.which == 13) {
        doSearch();
     }
     if (e.which == 27) {
        closeSearch();
        $("#searchbar").blur();
    }
});


function closeSearch() {
    jQuery(function($) {
        $(":button").css("top", "10px");
        $("#searchbar").css("top", "-64px");
    });
}

function doSearch() {
    alert($("#searchbar").val())
}