from . import routes
from flask import Flask, render_template, request, session, redirect, url_for
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_

@routes.route("/profile_cliente")
def profile_cliente():
    if "iduser" in session:

        usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])
        seguidos = len(usuario[0].seguidos)

        return render_template("profile_client.html", usuario = usuario, seguidos = seguidos)     
    else:
        return redirect("/")