from . import * 
#### YA NO SIRVE

@routes.route("/empresa_editar")
def empresa_editar():
    if "iduser" in session:
        if session["esEmp"] == 1:

            empresa = db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            redes_sociales = db.session.query(Tiene_redes).filter(Tiene_redes.id_empresa == session["iduser"])

            #Editar direccion HTML
            return render_template("profile_company.html", empresa = empresa, redes = redes_sociales)  
        else:
            return redirect("/")
    else:
        return redirect("/")




