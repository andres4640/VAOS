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

let map, infoWindow;

function initMap() {

  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -12.106374, lng: -77.042852 },
    zoom: 13,
    styles: [{
        featureType: "poi",
        elementType: "labels",
        stylers: [{ visibility: "off" }]
      }
    ],
  });

  createMarkers();

  /* Configure current location */
  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");
  locationButton.setAttribute("class","btn btn-light mt-2 shadow bg-white rounded")
  locationButton.textContent = "Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);

  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          /*infoWindow.setPosition(pos);
          infoWindow.setContent("Location found");
          infoWindow.open(map);*/

          map.setCenter(pos);
          map.setZoom(17);

          var marker = new google.maps.Marker({
            map:map,
            position:pos,
            icon: "/static/img/location.png",
            animation: google.maps.Animation.DROP,
          });

        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

async function fillData(){
  try
  {

    const res = await axios.get("/principal/lista-locales")
    lista_locales = res.data;
    console.log("LOCALES: ")
    console.log(lista_locales)
    console.log("========")
    return lista_locales;
  }
  catch (error)
  {

    console.log(error)

  }
  //return lista_locales;

}
var currWindow =false;
var locales = [];
async function createMarkers() {

  let locales = await fillData();
  console.log(locales)
  var ubicacion;

  for(let i = 0; i < locales.length; i++) 
  {
    console.log("GAAA2");
    ubicacion = {location: { lat: parseFloat(locales[i].latitud),  lng: parseFloat(locales[i].longitud)} }
    console.log(ubicacion);
    var marker = new google.maps.Marker({
      // position: locales[i].location,
      position: ubicacion.location ,
      map: map,
      animation: google.maps.Animation.DROP,
    })


    const contentString = '<h3 id="firstHeading" class="firstHeading">' + locales[i].nombre + '</h1>' +
    '<p><a href="/profile_local?localid='+locales[i].id + '">Ingresar a local</a></p>'

    infoWindow = new google.maps.InfoWindow();

    google.maps.event.addListener(marker, "click",(function(marker, contentString, infoWindow) {
      return function(evt) 
      {
        if( currWindow ) {
          currWindow.close();
        } 
        currWindow = infoWindow;

        console.log("Evento Click InfoWindow")
        infoWindow.setContent(contentString)
        infoWindow.open(map, marker);

      }
    })(marker, contentString, infoWindow))

  }
}


$("#boton_seguir").on('click',function(){
  $('#formulario-seguir').submit();
})
$("#boton-no-seguir").on('click',function(){
  $('#formulario-no-seguir').submit();
})