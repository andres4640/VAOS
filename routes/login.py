from . import *

@routes.route("/")
def index():
    if "iduser" in session:
        return redirect("/principal")
    else:
        return render_template("login_client.html")

@routes.route("/login", methods=["POST"])
def login():

    correo = request.form["correo"]
    contraseña = request.form["contraseña"]
    
    usuario_reg = db.session.query(Usuario_reg).filter(Usuario_reg.correo == correo, Usuario_reg.contraseña == contraseña)
    usuario_emp = db.session.query(Usuario_emp).filter(Usuario_emp.correo == correo, Usuario_emp.contraseña == contraseña)

    if usuario_reg.count() == 1:
        session["iduser"] = usuario_reg[0].id
        session["esEmp"] = 0
        print("Usuario Regular valido")
        return redirect(url_for("routes.principal"))

    elif usuario_emp.count() == 1:   
        session["iduser"] = usuario_emp[0].id
        session["esEmp"] = 1
        print("Usuario Empresa valido")
        return redirect(url_for("routes.principal"))

    else:
        print("Usario invalido")
        return render_template("login_client.html", error=True, mensaje="Error en los datos ingresados")

