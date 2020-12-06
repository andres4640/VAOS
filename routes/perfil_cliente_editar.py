from . import * 

@routes.route("/regular_editar")
def regular_editar():
    try:
        if "iduser" in session:
            if session["esEmp"] == 0:
                usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]

                #Editar direccion HTML
                return render_template("profile_company.html", usuario=usuario) 
            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/usuario_editar_confirmar")
def usuario_editar_confirmar():
    try:
        if "iduser" in session:
            if session["esEmp"] == 0:
                telefono = request.form["telefono"]
                correo = request.form["correo"]

                usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
                usuario.correo = correo
                usuario.telefono = telefono


                db.session.flush()
                db.session.commit()
                
                flash("Perfil editado exitosamente", "exito_editar_regular")
                return redirect("/profile_empresa")

            else:
                print("Usuario no es regular")
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise
