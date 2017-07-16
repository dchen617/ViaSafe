$(document).ready(function(){
    $(".navbutton").css("top", "10px");
    $("#map").css("transform", "scale(1)");
    $("#map").css("opacity", "1");

    $("#searchbutton").click(function() {
        $(".navbutton").css("top", "-64px");
        $("#searchbar").css("top", "0px");
        $("#searchbar").select();
    });

    $("#markbutton").click(function() {
        if (false) { // TODO: CHANGE THIS TO CHECK IF LOGGED IN
            $(".navbutton").css("top", "-64px");
            $("#loginscreen").css("top", "10px");
            $("#username").select();
        } else {
            $(".navbutton").css("top", "-64px");
            $("#reportscreen").css("top", "10px");
            $("#title").select();
            function getLocation() {
                addMarker();
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else {
                    alert("Geolocation is not supported by this browser.");
                }
            }
            function showPosition(position) {
                console.log(position.coords.latitude);
                console.log(position.coords.longitude);
                $.post("/index",
                        {'lat' : position.coords.latitude, 'lng': position.coords.longitude},
                        function(data, status){
                            // alert("Status: " + status);
                            moveMap(position.coords.longitude, position.coords.latitude, 15);
                            deleteMarker();
                            addMarker();
                        }
                    );
            }
            getLocation();
        }
    });
});


// Functions for handling getting in and out of the various menus
$(document).on("keyup", "#searchbar", function(e) {
    if (e.which == 13) {
        doSearch();
    }
    if (e.which == 27) {
        closeAll();
        $("#searchbar").blur();
    }
});

$(document).on("keyup", "#username", function(e) {
    if (e.which == 13) {
        $("#password").select();
    }
    if (e.which == 27) {
        closeAll();
        $("#username").blur();
    }
});

$(document).on("keyup", "#password", function(e) {
    if (e.which == 13) {
        doLogin();
    }
    if (e.which == 27) {
        closeAll();
        $("#password").blur();
    }
});

function closeAll() {
    jQuery(function($) {
        $(".navbutton").css("top", "10px");
        $("#searchbar").css("top", "-64px");
        $("#loginscreen").css("top", "-230px");
        $("#reportscreen").css("top", "-320px");
        $(".actionbutton").blur();
    });
    try {
        deleteMarker();
    } catch (err) {
    }
}

function doSearch() {
    data = document.getElementById('searchbar').value
    $.post("/index",
            {'address' : data, 'area': 'bar'},
            function(data, status){
                moveMap(data.lng, data.lat, 12);
                closeAll();
            }
        );
}

function doLogin() {
    alert($("#username").val());
    closeAll();
}

function doSubmit() {
    markerLocation = getMarker();
    $.post("/index",
            {'title': $("#title").val(), 'description': $("#description").val(),
            'lat': markerLocation.lat(), 'lng': markerLocation.lng()},
            function (data, status) {
                alert(status);
            }
        );

    closeAll();
}



// Functions for getting slow animations
$(document).on("keydown", function(e) {
    if (e.shiftKey == true) {
        $(".navbutton").css("transition", "all 2.5s");
        $("#searchbar").css("transition", "all 2.5s");
        $(".screen").css("transition", "all 2.5s");
    }
});

$(document).on("keyup", function(e) {
    if (e.which == 16) {
        $(".navbutton").css("transition", "all 0.5s");
        $("#searchbar").css("transition", "all 0.5s");
        $(".screen").css("transition", "all 0.5s");
    }
});