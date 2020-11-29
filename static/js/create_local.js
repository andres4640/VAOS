var autocomplete;
var near_place;
var longitud;
var latitude;
var tipoAmbiente = [];
var tipoMusica = [];

$(document).ready(function () {
    
    autocomplete = new google.maps.places.Autocomplete((document.getElementById('ubicacion')), {
        types: ['geocode'],
        componentRestrictions: {
            country: "PER"
        }
    });
	
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        near_place = autocomplete.getPlace();
        longitud = near_place.geometry.location.lng();
        latitude = near_place.geometry.location.lat();
        console.log(latitude);
        console.log(longitud);
    });
});

$("#form-createLocal").on("submit", async function(e){
    e.preventDefault();
    //$("#enviarClick").html('<i class="fas fa-spinner fa-pulse fa-lg"></i>').attr('disabled', true)
    const nombre = $("#nombre").val()
    const ubicacion = $("#ubicacion").val()
    const tipoLocal = $("#local").val()
    const horaApertura = $("#hapertura").val()
    const horaCierre = $("#hcierre").val()
    // const tipoAmbiente = document.getElementById("casual").val;
    // const tipoMusica = document.getElementById("cocktail").val;
    const descripcion = $("#descripcion").val()
                        
    $.each($("input[name='ambientes']:checked"), function(){
        tipoAmbiente.push($(this).val());
    });
    $.each($("input[name='musicas']:checked"), function(){
        tipoMusica.push($(this).val());
    });

    const data = {nombre,ubicacion,tipoLocal, horaApertura,horaCierre,tipoAmbiente,tipoMusica,descripcion,longitud,latitude}
    try {

        const res = await axios.post("/registrar_local_vista/registrar", data);
        console.log(res)
        if(res.status === 201){
            //$("#form-valoracion").trigger("reset")
            //$("reviewformModal").modal("hide")
            //$("#enviarClick").html('Enviar').attr('disabled', false)
            location.reload();
        }

    } catch (error) {
        //$("#enviarClick").html('Enviar').attr('disabled', false)
        console.log(error)
        
    }

})

$("#save").on('click',function(){
    $('#form-createLocal').submit();
})






