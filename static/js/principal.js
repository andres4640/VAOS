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

const locales = [
  {
    name: "Mia",
    location: {
      lat: -12.111636798137313,
      lng: -77.01464006252493
    },
    music: "latin",
    ambience: "casual"    
  },
  {
    name: "Tumbao",
    location: {
      lat: -12.12359586458485, lng: -77.03075355990035
    },
    music: "indie",
    ambience: "casual" 
  },
  {
    name: "Loki Bar",
    location: {
      lat: -12.119826102509654, lng: -77.02843040478278
    },
    music: "70-80's",
    ambience: "cocktail"
  },
  {
    name: "Dansza",
    location: {
      lat: -12.143180704691417, lng: -77.01571868877515
    },
    music: "latin",
    ambience: "upscale"
  },
  {
    name: "Valetodo Downtown",
    location: {
      lat: -12.112933892142436, lng: -76.99120614459953
    },
    music: "indie",
    ambience: "cocktail"
  },
  {
    name: "Extasis",
    location: {
      lat: -12.090678349724094, lng: -77.00331041239865
    },
    music: "latin",
    ambience: "casual"
  },
  {
    name: "80 Divas",
    location: {
      lat: -12.091046472008946, lng: -77.00009274382735
    },
    music: "latin",
    ambience: "casual"
  },
  {
    name: "La Cachina",
    location: {
      lat: -12.122589386678968, lng: -77.02988058308185
    },
    music: "70-80's",
    ambience: "casual"
  },
  {
    name: "Hooligans",
    location: {
      lat: -12.131945386001902, lng: -77.0300951631236
    },
    music: "latin",
    ambience: "casual"
  },
  {
    name: "VICCIO disco",
    location: {
      lat: -12.104886495253856, lng: -77.01838432301655
    },
    music: "electro",
    ambience: "casual"
  },
]

let map, infoWindow;

function initMap() {

  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -12.106374, lng: -77.042852 },
    zoom: 8,
    styles: [{
        featureType: "poi",
        elementType: "labels"
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
            icon: "location.png",
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

function createMarkers() {
  for(let i = 0; i < locales.length; i++) {
    let marker = new google.maps.Marker({
      position: locales[i].location,
      map: map,
      animation: google.maps.Animation.DROP,
    });

    /*infoWindow = new google.maps.InfoWindow();

    marker.addEventListener("click", function() {
      populateInfoWindow(marker, infoWindow);
      infoWindow.open(map, marker);
    })*/
  }
}

function populateInfoWindow(marker, info) {
  if(info.Marker != marker) {
    info.setContent("");
    info.setContent(marker.content);
  }
}