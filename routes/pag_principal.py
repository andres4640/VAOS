from . import *

@routes.route("/principal")
def principal():
    if "iduser" in session:
        if session["esEmp"] == 1:
            
            return redirect("/profile_empresa")

        else:
              
            total_locales = db.session.query(Local).all()
            cantidad_locales = len(total_locales)
            print(total_locales)
            return render_template("principal.html", lista_locales=total_locales, cantidad_locales=cantidad_locales)
    else:
        return redirect("/")