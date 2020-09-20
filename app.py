from flask import Flask, render_template, request
from database import db, Usuario_reg, Usuario_emp

app = Flask(__name__)
app.secret_key = "a"
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

with app.app_context():
    u1 = Usuario_reg(nombre="andres")
    u2 = Usuario_reg(nombre="alberto")
    u3 = Usuario_reg(nombre="soria")
    u4 = Usuario_reg(nombre="ruiz")

    e1 = Usuario_emp(nombre="A")
    e2 = Usuario_emp(nombre="B")

    e1.clientes.extend([u1,u2,u3])
    e2.clientes.extend([u1,u3,u4])

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.add(e1)
    db.session.add(e2)

    db.session.commit()


    for client in e1.clientes:
        print("Cliente 1: ", client.nombre)
    for empresa in u1.seguidos:
        print("Empresa 1: ", empresa.nombre)


if __name__ == "__main__":
    app.run()   