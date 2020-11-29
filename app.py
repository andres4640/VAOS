from flask import Flask, render_template, request, session, redirect, url_for, jsonify, json
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_
from routes import *
import json

app = Flask(__name__)
app.secret_key = "a"
app.register_blueprint(routes)


ENV = "dev"

if ENV == "dev":
    #Base de datos desarrollador, la que estara en la computadora para pruebas
    app.debug = True 
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost/prueba" #Direccion de la base de datos local
    #postressql:://postgress:[PASSWORD]@localhost/[BD_NAME]
else:
    app.debug = False
    #Direccion BD en produccion, en este caso en Heroku
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xhceqikvnuiykg:9d4974dc331549cb695929a767ef077e44cd5ff01eb596fe55e77cc41f7b8981@ec2-107-20-104-234.compute-1.amazonaws.com:5432/d8l3vkg2ldsirj"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Poner, sino sale error

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/cerrar_sesion", methods=['GET'])
def cerrar_sesion():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run()   
