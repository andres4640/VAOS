from . import * 


@routes.route("/local_editar")
def local_editar():
    if "iduser" in session:
        if session["esEmp"] == 1:
            localId = request.args.get('localid')
            local = db.session.query(Local).filter(Local.id == localId)[0]
            horario = local.horaApertura + " - " + local.horaCierre
            #Editar direccion HTML
            return render_template("profile_company.html", local=local, horario=horario) 
        else:
            return redirect("/")
    else:
        return redirect("/")

# @routes.route("/local_editar_confirmar")
# def local_editar_confirmar():

#     if "iduser" in session:
#         if session["esEmp"] == 0:
#             nombre = request.form["nombre"]
#             descripcion = request.form["descripcion"]
#             direccion = request.form["direccion"]
#             horaApertura = request.form["horaApertura"]
#             horaCierre = request.form["horaCierre"]

#             ambientes = request.form.getlist("ambientes")   # La musica es ingresada mediante CheckBox y se pueden escoger varias
#             musicas = request.form.getlist("musicas")       # El ambiente es ingresada mediante CheckBox y se pueden escoger varias

#             localId = request.args.get('localid')

#             local = db.session.query(Local).filter(Local.id == localId)[0]

#             local.nombre = nombre
#             local.descripcion = descripcion
#             local.direccion = direccion
#             local.horaApertura = horaApertura
#             local.horaCierre = horaCierre
            
#             # Elimino los ambientes y musicas existentes
#             for amb in local.ambientes:
#                     local.ambientes.delete(amb)
#             for mus in local.musicas:
#                     local.musicas.delete(mus)

#             # Agregan ambientes y musicas 
#             for amb in ambientes:
#                     ambiente = db.session.query(Tipo_ambiente).filter(Tipo_ambiente.id == amb)[0]
#                     local.ambientes.append(ambiente)
#             for mus in musicas:
#                     musica = db.session.query(Tipo_musica).filter(Tipo_musica.id == mus)[0]
#                     local.musicas.append(musica)

#             db.session.flush()
#             db.session.commit()

#             flash("Local editado exitosamente", "exito_local")
#             return redirect("/locales")

#         else:
#             print("Usuario no es empresa")
#             return redirect("/")
#     else:
#         return redirect("/")