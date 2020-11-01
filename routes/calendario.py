from . import *

@routes.route("/calendario")
def calendario():
    if "iduser" in session:
        return render_template("calendar.html")
    else:
        return redirect("/")