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
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showPosition);
                } else {
                    alert("Geolocation is not supported by this browser.");
                }
            }
            function showPosition(position) {
                console.log(position.coords.latitude);
                console.log(position.coords.longitude);
                $.post("http://127.0.0.1:8000/index",
                        {'lat' : position.coords.latitude, 'lng': position.coords.longitude},
                        function(data, status){
                            alert("Status: " + status);
                        }
                    );
            }
            getLocation();
            addMarker();
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
<<<<<<< HEAD
    $.post("http://127.0.0.1:8000/index",
            {'address' : data, 'area': 'bar'},
            function(data, status){
                alert("Status: " + status);
            }
        );
        console.log(data);

=======
    console.log(data);
    $.post("/index",
            {'address' : data},
            function(data, status){
                alert("Data: " + data + "\nStatus: " + status);
            }
        )
>>>>>>> 8a6f923c3536a2549784f617128e6cfe56b4aa1f


}

function doLogin() {
    alert($("#username").val());
    closeAll();
}

function doSubmit() {
    alert($("#title").val());
    alert(getMarker());
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
