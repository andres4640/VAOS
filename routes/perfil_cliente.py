from . import *

@routes.route("/profile_cliente")
def profile_cliente():
    if "iduser" in session:

        usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])
        seguidos = len(usuario[0].seguidos)

        return render_template("profile_client.html", usuario = usuario, seguidos = seguidos)     
    else:
        return redirect("/")