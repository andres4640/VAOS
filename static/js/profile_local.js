var count;

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


function starmark(item) {
    count = item.id[0];
    sessionStorage.starRating = count;
    var subid = item.id.substring(1);
    for(var i = 0; i < 5; i++) {
        if(i < count) {
            document.getElementById((i+1)+subid).style.color="orange";
        }else {
            document.getElementById((i+1)+subid).style.color="black";
        }
    }

}
var rating = {
    'rating': count
}

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
})

$("#form-valoracion").on("submit", async function(e){
    e.preventDefault();
    $("#enviarClick").html('<i class="fas fa-spinner fa-pulse fa-lg"></i>').attr('disabled', true)
    const comentario = $("#new-review").val()
    const estrellas = sessionStorage.getItem("starRating");
    const data = {comentario,estrellas}
    try {

        const res = await axios.post("/valorar", data);
        console.log(res)
        if(res.status === 201){
            alert("Comenatio publicado");
            $("#form-valoracion").trigger("reset")
            $("reviewformModal").modal("hide")
            $("#enviarClick").html('Enviar').attr('disabled', false)
            location.reload();
        }

    } catch (error) {
        $("#enviarClick").html('Enviar').attr('disabled', false)
        console.log(error)
        
    }

})

$("#submit-btn").on('click',function(){
    $('#formulario').submit();
})

$("#enviarClick").on('click',function(){
    $('#form-valoracion').submit();
})