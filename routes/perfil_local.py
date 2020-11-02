from . import *

@routes.route("/profile_local")
def profile_local():
    if "iduser" in session:
        if session["esEmp"] == 1:
            localId = request.args.get('localid')
            local = db.session.query(Local).filter(Local.id == localId)[0]
            horario = local.horaApertura + " - " + local.horaCierre
            
            return render_template("profile_local.html", local=local, horario=horario)  
        else:
            return redirect("/")
    else:
        return redirect("/")