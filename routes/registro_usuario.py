from flask import Flask, render_template, request, session, redirect, url_for
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_

from . import routes


@routes.route("/registro_reg")
def registrar_us():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("signup_client.html")

@routes.route("/registro_emp")
def registrar_emp():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("signup_empresa.html")

@routes.route("/registrar_regular", methods=["POST"])
def registrar_regular():
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    nacimiento = request.form["nacimiento"]
    nacionalidad = request.form["nacionalidad"]
    genero = int(request.form["genero"])
    correo = request.form["correo"]
    nombre_usuario = request.form["nombre_usuario"]
    contraseña = request.form["contraseña"]

    if db.session.query(Usuario_reg).filter(Usuario_reg.correo == correo).count() == 0 : 

        if db.session.query(Usuario_reg).filter(Usuario_reg.nombre_usuario == nombre_usuario).count() == 0:

            usuario = Usuario_reg(
                correo=correo, 
                nombre=nombres, 
                apellido=apellidos,
                genero=genero,
                nombre_usuario=nombre_usuario,
                fecha_nacimiento = nacimiento,
                contraseña = contraseña
                )
            
            db.session.add(usuario)
            db.session.commit()

            print("Usuario registado")

            return redirect("/")
            
            
        else:
            print("Nombre de usuario ya registrado")
            return redirect(url_for("routes.registro_reg"))
    else:
        print("Correo ya registrado")
        return redirect(url_for("routes.registro_reg"))

@routes.route("/registrar_empresa", methods=["POST"])
def registrar_empresa():

    nombre = request.form["nombre"]
    ruc = request.form["ruc"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    contraseña = request.form["contraseña"]

    if db.session.query(Usuario_emp).filter(Usuario_emp.correo == correo).count() == 0 :
        if db.session.query(Usuario_emp).filter(Usuario_emp.ruc == ruc).count() == 0 :

            empresa = Usuario_emp(
                correo=correo,
                ruc=ruc,
                contraseña=contraseña,
                nombre=nombre,
                telefono=telefono
            )
            
            db.session.add(empresa)
            db.session.commit()

            print("Empresa registada")
            return redirect("/") 
        else:

            print("RUC ya registrado")
            return redirect(url_for("routes.registrar_emp")) 

    else:
        print("Correo ya registrado")
        return redirect(url_for("routes.registrar_emp"))



