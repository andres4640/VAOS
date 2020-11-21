window.onload = initMap;

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("mapa"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}
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
