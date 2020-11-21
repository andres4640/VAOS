$(document).ready(function () {
    var autocomplete;
    autocomplete = new google.maps.places.Autocomplete((document.getElementById('ubicacion')), {
        types: ['geocode'],
        componentRestrictions: {
            country: "PER"
        }
    });
	
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        var near_place = autocomplete.getPlace();
        console.log(near_place.geometry.location.lng());
        console.log(near_place.geometry.location.lat());
    });
});


