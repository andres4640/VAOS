from . import *
from flask import jsonify, json

@routes.route("/principal")
def principal():
    if "iduser" in session:
        if session["esEmp"] == 1:
            
            return redirect("/profile_empresa")

        else:
              
            total_locales = db.session.query(Local).all()
            cantidad_locales = len(total_locales)
            print(total_locales)
            return render_template("principal.html", lista_locales=total_locales, cantidad_locales=cantidad_locales)
    else:
        return redirect("/")

@routes.route("/principal/lista-locales", methods=["GET"])
def principal_locales():
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
                    
                    # local_schema = LocalSchema(many=True)
                    # output = local_schema(total_locales).data


            print("output:")
            print(dict_locales)

            print("JSON: ")
            print(json.dumps(dict_locales))

            return jsonify(dict_locales)

        else:
            return redirect("/")
    else:
        return redirect("/")