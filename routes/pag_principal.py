from . import *

@routes.route("/principal")
def principal():
    if "iduser" in session:
        return render_template("principal.html")
    else:
        return redirect("/")
