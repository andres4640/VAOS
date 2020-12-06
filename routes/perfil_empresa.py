from . import *

@routes.route("/profile_empresa")
def profile_empresa():
    if "iduser" in session:
        if session["esEmp"] == 1:
            session["empresaid"] = session["iduser"]
        elif session["esEmp"] == 0:         
            empid = request.args.get('empid')
            print(empid)
            session["empresaid"]=empid


        empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["empresaid"])[0]
        redes_sociales = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"])
        clientes = empresa.clientes.count()
        lista_locales = empresa.locales

        facebook_url = ""
        twitter_url = ""
        instragram_url = ""
        sigue = 0 

        if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==1).first() is not None :
            facebook_url = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==1).first().url

        if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==2).first() is not None :
            twitter_url = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==2).first().url
        if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==3).first() is not None :
            instragram_url = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["empresaid"],Tiene_redes.id_red==3).first().url
                
        redes_emp = empresa.redes
        if redes_emp is not None: 
            for red in redes_emp:
                if red.id_red == 1:
                    facebook_url = red.url
                elif red.id_red == 2:
                    instragram_url =red.url
                elif red.id_red == 3:
                    twitter_url =red.url
        if session["esEmp"] == 0:
            usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]      
            for em in usuario.seguidos:
                if int(em.id) == int(session["empresaid"]):
                    sigue = 1
        print(sigue)
        return render_template("profile_company.html", empresa = empresa, num_cli = clientes, locales=lista_locales, redes = redes_sociales,
        facebook_url=facebook_url,twitter_url=twitter_url,instagram_url=instragram_url, sigue=sigue, esEmp=session["esEmp"])  
    else:
        return redirect("/")

@routes.route("/empresa_editar_confirmar", methods=["POST"])
def empresa_editar_confirmar():
    if "iduser" in session:
        if session["esEmp"] == 1:
            nombre = request.form["nombre"]
            telefono = request.form["telefono"]
            correo = request.form["correo"]
            red_fb_url = request.form["facebook"]
            red_insta_url = request.form["instagram"]
            red_twitter_url = request.form["twitter"]

            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            empresa.nombre = nombre
            empresa.telefono = telefono
            empresa.correo = correo

            facebook_url = ""
            twitter_url = ""
            instragram_url = ""

            redes_emp = empresa.redes
            if redes_emp is not None: 
                for red in redes_emp:
                    if red.id_red == 1:
                        facebook_url = red.url
                    elif red.id_red == 2:
                        instragram_url =red.url
                    elif red.id_red == 3:
                        twitter_url =red.url


            espacios_red_feb = red_fb_url.replace(" ","")
            if espacios_red_feb != "":
                if espacios_red_feb != facebook_url:
                    if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==1).first() is not None :
                        asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==1)[0]
                        db.session.delete(asociacion)
                        db.session.flush()
                    red_fb = db.session.query(Tipo_red).filter(Tipo_red.id == 1)[0]
                    tiene_redes = Tiene_redes(url=espacios_red_feb)
                    tiene_redes.red = red_fb
                    tiene_redes.empresa = empresa
                #empresa.redes.append(red_fb)
            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"], Tiene_redes.id_red==1).first() is not None:
                #if espacios_red_feb != "":
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"], Tiene_redes.id_red==1)[0]
                db.session.delete(asociacion)
                db.session.flush()

            espacios_red_insta = red_insta_url.replace(" ","")
            if espacios_red_insta != "":
                if espacios_red_insta != instragram_url:
                    if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2).first() is not None :
                        asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2)[0]
                        db.session.delete(asociacion)
                        db.session.flush()

                    red_insta = db.session.query(Tipo_red).filter(Tipo_red.id == 2)[0]
                    tiene_redes = Tiene_redes(url=espacios_red_insta)
                    tiene_redes.red = red_insta
                    tiene_redes.empresa = empresa
                #empresa.redes.append(red_insta)
            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2).first() is not None:
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==2)[0]
                db.session.delete(asociacion)
                db.session.flush()

            espacios_red_twitter = red_twitter_url.replace(" ","")
            if espacios_red_twitter != "":
                if espacios_red_twitter != instragram_url:
                    if db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3).first() is not None :
                        asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3)[0]
                        db.session.delete(asociacion)
                        db.session.flush()

                    red_twitter = db.session.query(Tipo_red).filter(Tipo_red.id == 3)[0]
                    tiene_redes = Tiene_redes(url=espacios_red_twitter)
                    tiene_redes.red = red_twitter
                    tiene_redes.empresa = empresa
                #empresa.redes.append(red_twitter)

            elif espacios_red_feb == "" and db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3).first() is not None:
                asociacion = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"],Tiene_redes.id_red==3)[0]
                db.session.delete(asociacion)
                db.session.flush()
            
            #db.session.add(tiene_redes)
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

@routes.route("/seguir", methods=["POST"])
def seguir_empresa():
    if "iduser" in session:
        if session["esEmp"] == 0:

            usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
            print("Local a seguir: ", session["empresaid"])
            print(db.session.query(Usuario_emp).filter(Usuario_emp.id == session["empresaid"]).first())
            emp = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["empresaid"])[0]
            usuario.seguidos.append(emp)

            db.session.flush()
            db.session.commit()

            direcc = '/profile_empresa?empid='+ session["empresaid"]

            return redirect(direcc)
        else:
            return redirect("/")
    else:
        return redirect("/")

@routes.route("/no_seguir", methods=["POST"])
def no_seguir_empresa():
    if "iduser" in session:
        if session["esEmp"] == 0:

            usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
            emp = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["empresaid"])[0]
            usuario.seguidos.remove(emp)

            db.session.flush()
            db.session.commit()

            direcc = '/profile_empresa?empid='+ session["empresaid"]

            return redirect(direcc)
        else:
            return redirect("/")
    else:
        return redirect("/")