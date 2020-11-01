from . import *

@routes.route("/registrar_local_vista")
def registrar_local_vista():
    if "iduser" in session:
        if session["esEmp"] == 1:
            lista_ambiente = db.session.query(Tipo_ambiente)
            lista_musicas = db.session.query(Tipo_musica)
            return render_template("create_local.html", lista_ambientes=lista_ambiente,lista_musica=lista_musicas)
        else:
            return redirect("/")
    else:
        return redirect("/")


@routes.route("/registrar_local_vista/registrar", methods=["POST"])
def registrar_local():
    if "iduser" in session:
        if session["esEmp"] == 1:
            if request.method == "POST":
                nombre = request.form["nombre"]
                descripcion = request.form["descripcion"]
                direccion = request.form["direccion"]
                horaApertura = request.form["horaApertura"]
                horaCierre = request.form["horaCierre"]
                tipoLocal = request.form["tipo_local"]

                # Falta distrito - direccion
                ambientes = request.form.getlist("ambientes")   # La musica es ingresada mediante CheckBox y se pueden escoger varias
                musicas = request.form.getlist("musicas")       # El ambiente es ingresada mediante CheckBox y se pueden escoger varias

                print(horaApertura)
                local = Local(
                    nombre = nombre,
                    direccion = direccion,
                    descripcion = descripcion,
                    horaApertura = horaApertura,
                    horaCierre = horaCierre,
                    id_empresa = session["iduser"],
                    tipoLocal = tipoLocal
                )

                for amb in ambientes:
                    ambiente = db.session.query(Tipo_ambiente).filter(Tipo_ambiente.id == amb)[0]
                    local.ambientes.append(ambiente)
                for mus in musicas:
                    musica = db.session.query(Tipo_musica).filter(Tipo_musica.id == mus)[0]
                    local.musicas.append(musica)

                db.session.add(local)
                db.session.commit()

                flash("Local creado exitosamente")
                return redirect("/")
        else:
            return redirect("/")
    else:
        return redirect("/")


    
