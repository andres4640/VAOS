var count;
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
    if(!estrellas){
        estrellas = 1
    }
    const data = {comentario,estrellas}
    try {

        const res = await axios.post("/valorar", data);
        console.log(res)
        if(res.status === 201){
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

$("#eliminar-local").on('click',function(){
    $('#formulario-eliminar').submit();
})
