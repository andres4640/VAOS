from . import *


@routes.route("/registro_reg")
def registrar_us():
    try:
        if "iduser" in session:
            return redirect("/principal")
        else:
            nacionalidades = db.session.query(Nacionalidad).all()
            
            return render_template("signup_client.html", nacionalidades=nacionalidades)
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/registro_emp")
def registrar_emp():
    try:
        if "iduser" in session:
            return redirect("/principal")
        else:
            return render_template("signup_empresa.html")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/registrar_regular", methods=["POST"])
def registrar_regular():
    try: 
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        nacimiento = request.form["nacimiento"]
        nacionalidad = request.form["nacionalidad"]
        genero = int(request.form["genero"])
        correo = request.form["correo"]
        nombre_usuario = request.form["nombre_usuario"]
        contraseña = request.form["contraseña"]

        if db.session.query(Usuario_reg).filter(Usuario_reg.correo == correo).count() == 0 : 

            if db.session.query(Usuario_reg).filter(Usuario_reg.nombre_usuario == nombre_usuario).count() == 0:

                usuario = Usuario_reg(
                    correo=correo, 
                    nombre=nombres, 
                    apellido=apellidos,
                    genero=genero,
                    nombre_usuario=nombre_usuario,
                    fecha_nacimiento = nacimiento,
                    contraseña = contraseña,
                    id_nacionalidad = nacionalidad
                    )
                
                db.session.add(usuario)
                db.session.commit()

                print("Usuario registado")

                return redirect("/")
                
                
            else:
                print("Nombre de usuario ya registrado")
                return redirect(url_for("routes.registro_reg"))
        else:
            print("Correo ya registrado")
            return redirect(url_for("routes.registro_reg"))
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/registrar_empresa", methods=["POST"])
def registrar_empresa():
    try:

        nombre = request.form["nombre"]
        ruc = request.form["ruc"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]

        if db.session.query(Usuario_emp).filter(Usuario_emp.correo == correo).count() == 0 :
            if db.session.query(Usuario_emp).filter(Usuario_emp.ruc == ruc).count() == 0 :

                empresa = Usuario_emp(
                    correo=correo,
                    ruc=ruc,
                    contraseña=contraseña,
                    nombre=nombre,
                    telefono=telefono
                )
                
                db.session.add(empresa)
                db.session.commit()

                print("Empresa registada")
                return redirect("/") 
            else:

                print("RUC ya registrado")
                return redirect(url_for("routes.registrar_emp")) 

        else:
            print("Correo ya registrado")
            return redirect(url_for("routes.registrar_emp"))
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise



