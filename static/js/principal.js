/* Configuracion del mapa */

x = navigator.geolocation;

x.getCurrentPosition(success, failure);

function success(position) {
  var myLat = position.coords.latitude;
  var myLong = position.coords.longitude;

  var coords = new google.maps.LatLng(myLat,myLong);

  var myStyles =[
    {
        featureType: "poi",
        elementType: "labels",
        stylers: [
              { visibility: "off" }
        ]
    }
  ];

  var mapOptions = {
    zoom: 16,
    center: coords,
    styles: myStyles

  }

  var map = new google.maps.Map(document.getElementById("map"), mapOptions);

  var market = new google.maps.Marker({
    map:map,
    position:coords,
    //icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
  });


}

function failure() {
}

/* Fin de Configuracion del mapa */


/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.getElementById("head-logo").style.marginLeft = "250px";
}
  
/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("head-logo").style.marginLeft = "0";
}
