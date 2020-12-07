from . import *
from flask import jsonify, json
from datetime import datetime, date
import sys

@routes.route("/inicio")
def inicio():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:           
                return redirect("/profile_empresa")
            else:            
                return render_template("inicio.html")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", E)
        raise

@routes.route("/principal")
def principal():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:           
                return redirect("/profile_empresa")
            else:
                return render_template("principal.html")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/lista_locales")
def lista_locales():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:
                
                return redirect("/profile_empresa")
            else:             
                total_locales = db.session.query(Local).all()
                cantidad_locales = len(total_locales)
                print(total_locales)
                return render_template("lista_locales.html", lista_locales=total_locales, cantidad_locales=cantidad_locales)
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

# @routes.route("/buscar_locales")
# def buscar_locales():
#     if "iduser" in session:
#         if session["esEmp"] == 1:
            
#             return redirect("/profile_empresa")
#         else:             
#             total_locales = Local.query.whoosh.search(request.args.get('query')).all()
#             cantidad_locales = len(total_locales)
#             print(total_locales)
#             return render_template("lista_locales.html", lista_locales=total_locales, cantidad_locales=cantidad_locales)
#     else:
#         return redirect("/")


@routes.route("/lista_eventos")
def lista_eventos():
    try:
        if "iduser" in session:
            if session["esEmp"] == 1:
                
                return redirect("/profile_empresa")
            else:             
                total_eventos = db.session.query(Evento).all()            
                if len(total_eventos) > 1:
                    eventos_filtro = []
                    today = datetime.combine(date.today(), datetime.min.time())
                    for even in total_eventos:
                        if even.fechaInicio > today:
                            eventos_filtro.append(even)
                    total_eventos = eventos_filtro
                print(total_eventos)
                return render_template("lista_eventos.html", lista_eventos=total_eventos, cantidad_eventos=len(total_eventos))
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise

@routes.route("/principal/lista-locales", methods=["GET"])
def principal_locales():
    try:
        if "iduser" in session:
            if session["esEmp"] == 0:
                dict_locales = []
                total_locales = db.session.query(Local).all()
                for local in total_locales:                       
                    local_dict = {}
                    local_dict["id"] = local.id
                    local_dict["nombre"] = local.nombre
                    local_dict["longitud"] = str(local.longitud)
                    local_dict["latitud"] = str(local.latitud)
                    dict_locales.append(local_dict)

                return jsonify(dict_locales)

            else:
                return redirect("/")
        else:
            return redirect("/")
    except:
        e = sys.exc_info()[0]
        print("Unexpected error: ", e)
        raise