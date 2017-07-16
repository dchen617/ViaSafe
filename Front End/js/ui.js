$(document).ready(function(){
    $(":button").css("top", "10px");
    
    $("#searchbutton").click(function() {
        $(":button").css("top", "-64px");
        $("#searchbar").css("top", "0px");
        $("#searchbar").select();
    });
    
    $("#searchbar").change(function() {
        if ($("#searchbar").is(":focus"))
            doSearch();
    });
});

$(document).keyup(function(e) {
    if (e.keyCode == 27) {
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