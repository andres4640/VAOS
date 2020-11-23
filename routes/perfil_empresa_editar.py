from . import * 

@routes.route("/empresa_editar")
def empresa_editar():
    if "iduser" in session:
        if session["esEmp"] == 1:

            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            redes_sociales = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"])

            #Editar direccion HTML
            return render_template("profile_company.html", empresa = empresa, redes = redes_sociales)  
        else:
            return redirect("/")
    else:
        return redirect("/")

@routes.route("/empresa_editar_confirmar")
def empresa_editar_confirmar():
    if "iduser" in session:
        if session["esEmp"] == 1:
            nombre = request.form["nombre"]
            telefono = request.form["telefono"]
            correo = request.form["correo"]
            red_fb_url = request.form["facebook"]
            red_insta_url = request.form["instragram"]
            red_twitter_url = request.form["twitter"]

            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            empresa.nombre = nombre
            empresa.telefono = telefono
            empresa.correo = correo

            espacios_red_feb = red_fb_url.replace(" ","")
            if espacios_red_feb != "":
                red_fb = db.session.query(Tipo_red).filter(Tipo_red.id == 1)[0]
                tiene_redes = Tiene_redes(url=espacios_red_feb)
                tiene_redes.red = red_fb
                empresa.redes.append(red_fb)
            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"], Tiene_redes.id_red==1) is None:
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"], Tiene_redes.id_red==1)
                db.session.delete(asociacion)
                db.session.flush()

            espacios_red_insta = red_insta_url.replace(" ","")
            if espacios_red_insta != "":
                red_insta = db.session.query(Tipo_red).filter(Tipo_red.id == 2)[0]
                tiene_redes = Tiene_redes(url=espacios_red_insta)
                tiene_redes.red = red_insta
                empresa.redes.append(red_insta)
            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2) is None:
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2)
                db.session.delete(asociacion)
                db.session.flush()

            espacios_red_twitter = red_twitter_url.replace(" ","")
            if espacios_red_twitter != "":
                red_twitter = db.session.query(Tipo_red).filter(Tipo_red.id == 3)[0]
                tiene_redes = Tiene_redes(url=espacios_red_twitter)
                tiene_redes.red = red_twitter
                empresa.redes.append(red_twitter)

            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3) is None:
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3)
                db.session.delete(asociacion)
                db.session.flush()
            
            db.session.add(tiene_redes)
            db.session.flush()
            db.session.commit()
            # Agregar nuevas redes
            # Mostrar redes que ya tienes y permitir editarlas

            flash("Perfil editado exitosamente", "exito_editar_empresa")
            return redirect("/profile_empresa")
        else:
            print("Usuario no es empresa")
            return redirect("/")
    else:
        print("Usuario no inicio sesion")
        return redirect("/")




