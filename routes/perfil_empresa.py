from . import *

@routes.route("/profile_empresa")
def profile_empresa():
    if "iduser" in session:
        if session["esEmp"] == 1:

            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            clientes = empresa.clientes.count()
            lista_locales = empresa.locales
            
            return render_template("profile_company.html", empresa = empresa, num_cli = clientes, locales=lista_locales)  
        else:
            return redirect("/")
    else:
        return redirect("/")