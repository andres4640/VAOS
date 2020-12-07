from . import *
import sys

@routes.route("/profile_evento")
def profile_evento():
    try:
        if "iduser" in session:      
            empid = request.args.get('empid')

            esEmp = session["esEmp"]

            evento = db.session.query(Evento).filter(Evento.id == empid)[0]
            local = db.session.query(Local).filter(Local.id == evento.id_local)[0]
            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == local.id_empresa)[0]
            return render_template("profile_event.html", evento=evento, local=local, empresa=empresa, esEmp=esEmp)
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/eliminar_evento", methods=["POST"])
def eliminar_evento():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:
                eventoId = request.args.get('eventoid')
                evento = db.session.query(Evento).filter(Evento.id == eventoId).first()

                db.session.delete(evento)
                db.session.commit()
                flash("Perfil eliminado exitosamente", "exito_editar_empresa")
                return redirect("/eventos")         
            else:
                return redirect("/")
        else:
            return redirect("/")

    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise