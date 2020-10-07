from flask import Flask, render_template, request, session, redirect, url_for
from database import db, Usuario_reg, Usuario_emp
from sqlalchemy import and_, or_

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

############################ LOGIN #########################################
@app.route("/")
def index():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("login_client.html")

@app.route("/login", methods=["POST"])
def login():

    correo = request.form["correo"]
    contraseña = request.form["contraseña"]
    
    usuario_reg = db.session.query(Usuario_reg).filter(Usuario_reg.correo == correo, Usuario_reg.contraseña == contraseña)
    usuario_emp = db.session.query(Usuario_emp).filter(Usuario_emp.correo == correo, Usuario_emp.contraseña == contraseña)

    if usuario_reg.count() == 1:
        session["iduser"] = usuario_reg[0].id
        session["esEmp"] = 0
        print("Usuario Regular valido")
        return redirect(url_for("principal"))

    elif usuario_emp.count() == 1:   
        session["iduser"] = usuario_emp[0].id
        session["esEmp"] = 1
        print("Usuario Empresa valido")
        return redirect(url_for("principal"))

    else:
        print("Usario invalido")
        return render_template("login_client.html", error=True, mensaje="Error en los datos ingresados")


############################ REGISTRO DE USUARIOS #########################################
@app.route("/registro_reg")
def registrar_us():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("signup_client.html")

@app.route("/registro_emp")
def registrar_emp():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("signup_empresa.html")

@app.route("/registrar_regular", methods=["POST"])
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
            return redirect(url_for("registro_reg"))
    else:
        print("Correo ya registrado")
        return redirect(url_for("registro_reg"))

@app.route("/registrar_empresa", methods=["POST"])
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
            return redirect(url_for("registrar_emp")) 

    else:
        print("Correo ya registrado")
        return redirect(url_for("registrar_emp"))

############################ CERRAR SESION #########################################

@app.route("/cerrar_sesion", methods=['GET'])
def cerrar_sesion():
    session.clear()
    return redirect("/")


############################ PAG. PRINCIPAL #########################################

@app.route("/principal")
def principal():
    if "iduser" in session:
        return render_template("principal.html")
    else:
        return redirect("/")


@app.route("/calendario")
def calendario():
    if "iduser" in session:
        return render_template("calendar.html")
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run()   
