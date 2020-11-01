window.onload = init;

function init() {
    const map = new ol.Map({
        view: new ol.View({
            center: [-8574833.568028785, -1359643.0389284105],
            zoom: 10,
            maxZoom: 10,
            minZoom: 4
        }),
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        target: 'mapa'
    })

    map.on('click', function(evt) {
        console.log(evt.coordinate);
    })
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
