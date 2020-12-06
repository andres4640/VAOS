from . import *
import json, math

@routes.route("/profile_local")
def profile_local():
    try:
        if "iduser" in session:
            
            localId = request.args.get('localid')
            local = db.session.query(Local).filter(Local.id == localId)[0]
            session["localid"] = localId
            horario = local.horaApertura + " - " + local.horaCierre
            lista_ambiente = db.session.query(Tipo_ambiente)
            lista_musicas = db.session.query(Tipo_musica)
            esEmp = session["esEmp"]

            session["empresaid"]= local.id_empresa
            emp = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["empresaid"])[0]
            nombre_emp = emp.nombre

            num_estrellas_aprox=0
            num_estrellas=0
            count=0

            lista_valoraciones = db.session.query(Valoracion).filter(Valoracion.id_local == localId)

            
            if lista_valoraciones.count() != 0:
                for estrellas in lista_valoraciones:    
                    num_estrellas += estrellas.estrellas
                    count +=1
                
                total = num_estrellas/count
                num_estrellas_aprox = math.ceil(total)

            valoraciones = db.session.query(Valoracion, Usuario_reg).join(Usuario_reg,Usuario_reg.id == Valoracion.id_regular).filter(Valoracion.id_local == localId)
            return render_template("profile_local.html", local=local, horario=horario, lista_ambientes=lista_ambiente, lista_musica=lista_musicas, esEmp=esEmp, valoraciones=valoraciones, num_estrellas=num_estrellas_aprox, count=count, empresaid=session["empresaid"], nombre_emp=nombre_emp)  
            
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/local_editar_confirmar", methods=["POST"])
def local_editar_confirmar():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:
                nombre = request.form["nombre"]
                descripcion = request.form["descripcion"]
                direccion = request.form["direccion"]
                horaApertura = request.form["horaApertura"]
                horaCierre = request.form["horaCierre"]

                ambientes = request.form.getlist("ambientes")   # La musica es ingresada mediante CheckBox y se pueden escoger varias
                musicas = request.form.getlist("musicas")       # El ambiente es ingresada mediante CheckBox y se pueden escoger varias

                local = db.session.query(Local).filter(Local.id == session["localid"]).first()

                local.nombre = nombre
                local.descripcion = descripcion
                local.direccion = direccion
                local.horaApertura = horaApertura
                local.horaCierre = horaCierre
                
                # Elimino los ambientes y musicas existentes
                for amb in local.ambientes:
                    #db.session.delete(amb)
                    local.ambientes.remove(amb)
                    db.session.commit()
                    
                for mus in local.musicas:
                    #db.session.delete(mus)
                    local.musicas.remove(mus)
                    db.session.commit()

                # Agregan ambientes y musicas 
                for amb in ambientes:
                        ambiente = db.session.query(Tipo_ambiente).filter(Tipo_ambiente.id == amb)[0]
                        local.ambientes.append(ambiente)
                for mus in musicas:
                        musica = db.session.query(Tipo_musica).filter(Tipo_musica.id == mus)[0]
                        local.musicas.append(musica)

                db.session.flush()
                db.session.commit()

                flash("Local editado exitosamente", "exito_local")
                return redirect("/locales")

            else:
                print("Usuario no es empresa")
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/valorar", methods=["POST"])
def reseña():
    try:
        if "iduser" in session:
            if session["esEmp"] == 0:
                
                data = request.get_json(force = True)
                estrellas = data["estrellas"]
                comentario = data["comentario"]

                result = ''
                print(estrellas)
                print(comentario)

                asociacion = Valoracion(comentario=comentario, estrellas=estrellas)
                asociacion.usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
                asociacion.local = db.session.query(Local).filter(Local.id == session["localid"])[0]

                db.session.flush()
                db.session.commit()

                return json.dumps({'success':True}), 201, {'ContentType':'application/json'}

            else:
                print("Usuario no es empresa")
                return redirect("/") 

        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise