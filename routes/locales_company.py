from . import * 

@routes.route("/locales")
def mostrar_locales():
    try: 
        if "iduser" in session:
            if session["esEmp"] == 1:
                empresa =  db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
                lista_locales = empresa.locales
                return render_template("locales_company.html", lista_locales=lista_locales)
            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise