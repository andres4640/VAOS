from . import *

@routes.route("/principal")
def principal():
    if "iduser" in session:
        if session["esEmp"] == 1:
            
            return redirect("/profile_empresa")

        else:
              
            total_locales = db.session.query(Local).all()
            print(total_locales)
            return render_template("principal.html", lista_locales=total_locales)
    else:
        return redirect("/")