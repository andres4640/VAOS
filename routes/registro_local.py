from flask import Flask, render_template, request, session, redirect, url_for
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_
from . import routes

@routes.route("/registrar_local", methods=["POST"])
def registrar_local():

    if request.method == "POST":
        nombre = request.form["nombre"]
        descripcion = request.form["descripcion"]
        direccion = request.form["direccion"]
        horaApertura = request.form["horaApertura"]
        horaCierre = request.form["horaCierre"]

        # Falta distrito - direccion
        ambientes = request.form.getlist("ambientes")   # La musica es ingresada mediante CheckBox y se pueden escoger varias
        musicas = request.form.getlist("musicas")       # El ambiente es ingresada mediante CheckBox y se pueden escoger varias

        local = Local(
            nombre = nombre,
            descripcion = descripcion,
            horaApertura = horaApertura,
            horaCierre = horaCierre,
            id_empresa = session["iduser"],
        )

        for amb in ambientes:
            ambiente = db.session.query(Tipo_ambiente).filter(Tipo_ambiente.id == amb)
            local.ambientes.add(ambiente)
        for mus in musicas:
            musica = db.session.query(Tipo_musica).filter(Tipo_musica.id == mus)
            local.musicas.add(musica)

        db.session.add(local)
        db.session.commit()


    
