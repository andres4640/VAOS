from . import *
from datetime import datetime

@routes.route("/registrar_evento_vista")
def registrar_evento_vista():
    if "iduser" in session:
        if session["esEmp"] == 1:
            usuario_emp = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            lista_locales = usuario_emp.locales
            return render_template("create_event.html", lista_locales=lista_locales)
        else: 
            return redirect("/")
    else:
        return redirect("/")
        
@routes.route("/registrar_evento_vista/registrar-evento", methods=["POST"])
def registrar_evento():
    if "iduser" in session:
        if session["esEmp"] == 1:
            if request.method == "POST":
                nombre = request.form["nombre"]
                local_id = request.form["local"]
                fechaInicio = request.form["fechaInicio"]
                fechaFinal = request.form["fechaFin"]
                horaInicio = request.form["horaInicio"]
                horaFinal = request.form["horaFin"]
                precio = request.form["precio"]
                descripcion = request.form["descripcion"]

                fecha1= fechaInicio + " " + horaInicio + ":00"
                fecha2= fechaFinal + " " + horaFinal + ":00"

                evento = Evento(
                    nombre=nombre,
                    descripcion=descripcion,
                    precio=precio,
                    fechaInicio=fecha1,
                    fechaFin=fecha2
                )

                local_query = db.session.query(Local).filter(Local.id == local_id)[0]
                local_query.eventos.append(evento)
                
                db.session.add(evento)
                db.session.commit()

                return redirect("/")

        else:
            return redirect("/")

    else:
        return redirect("/")
