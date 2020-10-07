$(document).ready(function () {
    var ahora = new Date();
    var dd = ahora.getDate();
    var mm = ahora.getMonth()+1;
    var yyyy = ahora.getFullYear()-18;
    if(dd<10){
        dd='0'+dd;
    }
    if(mm<10){
        mm='0'+mm;
    }

    ahora = yyyy+"-"+mm+"-"+dd;
    $("#fnacimiento").attr('max',ahora);
}); 

var validNombre = false;
var validApe = false;
var validUsername = false;
var validEmail = false;
var validPass = false;
var validFecha = false;

$("#nombres").on('blur', function(){
    var nombres=$("#nombres").val();
    if(nombres=="" || nombres==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validNombre=false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validNombre=true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#apellidos").on('blur', function(){
    var apellidos=$("#apellidos").val();
    if(apellidos=="" || apellidos==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validApe=false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validApe=true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#correo").on('blur', function(){
    var correo=$("#correo").val();
    emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i
    if(emailRegex.test(correo)){
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid")
        validEmail=true;
    }
    else{
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validEmail=false;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#username").on('blur', function(){
    var username=$("#username").val();
    if(username=="" || username==null || username.length < 8){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validUsername=false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validUsername=true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#password").on('blur', function(){
    var password=$("#password").val();
    if(password=="" || password==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid")
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#rpassword").on('blur', function(){
    var password=$("#password").val();
    var rpassword=$("#rpassword").val();
    if(rpassword=="" || rpassword==null || rpassword!=password){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validPass=false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validPass=true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})



$("#fnacimiento").on('blur', function()
{
    var fecha = new Date($("#fnacimiento").val());
    fecha.setDate(fecha.getDate()+1);
    console.log(fecha);
    if($("#fnacimiento").val()==null || $("#fnacimiento").val()=="")
    {
        validFecha=false;
    }
    else{
        validFecha=true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

function validarTodo()
{
    if(validEmail && validNombre && validPass && validApe && validUsername && validFecha)
    {
        return true;
    }
    return false;
}

$("#terminos").on("click", function(){
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$('#terminos-modal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })