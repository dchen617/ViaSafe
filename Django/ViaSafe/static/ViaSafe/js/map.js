var Marlborough = {lat: 42.332776, lng: -71.589868};
var map;
var marker;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    mapTypeControl: false,
    backgroundColor: 'none',
    center: Marlborough,
    styles: [
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#fafafa"
      }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#000000"
      }
    ]
  },
  {
    "featureType": "landscape.man_made",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#769160"
      }
    ]
  },
  {
    "featureType": "landscape.natural",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#4e7223"
      }
    ]
  },
  {
    "featureType": "poi.business",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#88a86d"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#5b8428"
      }
    ]
  },
  {
    "featureType": "poi.school",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#7ca84b"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#274a00"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#382511"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#b07537"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#264b00"
      }
    ]
  },
  {
    "featureType": "transit.station.airport",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "lightness": -20
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#363942"
      }
    ]
  }
]
  });
  // var marker = new google.maps.Marker({
  //   position: uluru,
  //   map: map
  // });
}

function addMarker() {
  marker = new google.maps.Marker({
    position: map.getCenter(),
    draggable: true,
    animation: google.maps.Animation.DROP,
    map: map
  });
}

function deleteMarker() {
  marker.setMap(null);
  marker = null;
}

function getMarker() {
  return marker.getPosition();
}

function moveMap(lng, lat) {
  map.setCenter({lat: lat, lng: lng})
  map.setZoom(12);
}