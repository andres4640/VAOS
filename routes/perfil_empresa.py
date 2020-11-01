from . import *

@routes.route("/profile_empresa")
def profile_empresa():
    if "iduser" in session:
        if session["esEmp"] == 1:

            empresa = db.session.query(Tipo_ambiente).filter(Usuario_emp.id == session["iduser"])[0]
            clientes = len(empresa.clientes)
            
        return render_template("profile_company.html", empresa = empresa, num_cli = clientes)     
    else:
        return redirect("/")