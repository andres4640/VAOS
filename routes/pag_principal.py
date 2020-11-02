from . import *

@routes.route("/principal")
def principal():
    if "iduser" in session:
        if session["esEmp"] == 1:
            return redirect("/profile_empresa")

        else:
            return render_template("principal.html")
    else:
        return redirect("/")
