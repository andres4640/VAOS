from . import * 
import sys
from datetime import date

@routes.route("/eventos_seguidos")
def mostrar_eventos_seguidos():
    try:
        if "iduser" in session:
            if session["esEmp"] == 0:
                usuario = db.session.query(Usuario_reg).filter(Usuario_reg.id == session["iduser"])[0]
                empresas = usuario.seguidos
                eventos = []
                   
                for emp in empresas:
                    lista_locales = emp.locales
                    for local in lista_locales:
                        for eve in local.eventos:
                            eventos.append(eve)
                if len(eventos) > 1:
                    eventos_filtro = []
                    today = datetime.combine(date.today(), datetime.min.time())
                    for even in eventos:
                        if even.fechaInicio > today:
                            eventos_filtro.append(even)
                    eventos = eventos_filtro

                return render_template("eventos_emp_seguidas.html", eventos=eventos, num_eventos =len(eventos))
            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise