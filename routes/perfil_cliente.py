from . import *

@routes.route("/profile_cliente")
def profile_cliente():
    try:
        if "iduser" in session:

            usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
            pais = db.session.query(Nacionalidad).filter(Nacionalidad.id == usuario.id_nacionalidad)[0]
            seguidos = len(usuario.seguidos)

            return render_template("profile_client.html", us = usuario, seguidos = seguidos, nacion = pais)     
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise