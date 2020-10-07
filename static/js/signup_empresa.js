var validNombre = false;
var validRuc = false;
var validTel = false;
var validEmail = false;
var validPass = false;


$("#nombre-empresa").on('blur', function(){
    var nombre=$("#nombre-empresa").val();
    if(nombre=="" || nombre==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validNombre = false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validNombre = true;
    }
    if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#ruc").on('blur', function(){
    var ruc=$("#ruc").val();
    if(ruc=="" || ruc==null || ruc.length < 11){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validRuc = false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validRuc = true;
     }
     if($("#terminos").prop("checked") && validarTodo()){
        $("#signup").removeAttr("disabled");
    }
    else{
        $("#signup").attr("disabled",true);
    }
})

$("#telefono").on('blur', function(){
    var telefono=$("#telefono").val();
    if(telefono=="" || telefono==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
        validTel = false;
    }
    else{
        $(this).removeClass("is-invalid");
        $(this).addClass("is-valid");
        validTel = true;
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

$("#password").on('blur', function(){
    var password=$("#password").val();
    if(password=="" || password==null){
        $(this).removeClass("is-valid");
        $(this).addClass("is-invalid");
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
        $(this).addClass("is-invalid")
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

function validarTodo()
{
    if(validEmail && validNombre && validPass && validRuc && validTel)
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