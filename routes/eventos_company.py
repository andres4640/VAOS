from . import * 

@routes.route("/eventos")
def mostrar_eventos():
    if "iduser" in session:
        if session["esEmp"] == 1:
            lista_eventos = []
            empresa =  db.session.query(Usuario_emp).filter(Usuario_emp.id == session["iduser"])[0]
            lista_locales = empresa.locales
            for loc in lista_locales:
                for eve in loc.eventos:
                    lista_eventos.append(eve)

            return render_template("eventos_company.html", lista_eventos=lista_eventos)
        else:
            return redirect("/")
    else:
        return redirect("/")
    

