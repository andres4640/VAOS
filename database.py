from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

sigue = db.Table(
    "sigue",
    db.Column("id_regular", db.Integer, db.ForeignKey("usuario_reg.id")),
    db.Column("id_empresa", db.Integer, db.ForeignKey("usuario_emp.id"))
)

tiene_ambiente = db.Table(
    "tiene_ambiente",
    db.Column("id_local", db.Integer, db.ForeignKey("local.id")),
    db.Column("id_ambiente", db.Integer, db.ForeignKey("tipo_ambiente.id"))
)
tiene_musica = db.Table(
    "tiene_musica",
    db.Column("id_local", db.Integer, db.ForeignKey("local.id")),
    db.Column("id_musica", db.Integer, db.ForeignKey("tipo_musica.id"))
)

class Valoracion(db.Model):

    __tablename__ = "valoracion"

    id = db.Column(db.Integer, primary_key=True)
    id_regular = db.Column( db.Integer, db.ForeignKey("usuario_reg.id"))
    id_local = db.Column(db.Integer, db.ForeignKey("local.id"))
    comentario = db.Column(db.Text)
    estrellas = db.Column(db.Integer)

    usuario = db.relationship("Usuario_reg", back_populates="locales_valorados")
    local = db.relationship("Local", back_populates="valoraciones")

class Tiene_redes(db.Model):

    __tablename__ = "tiene_redes"

    id_empresa = db.Column(db.Integer, db.ForeignKey("usuario_emp.id"), primary_key=True)
    id_red = db.Column(db.Integer, db.ForeignKey("tipo_red.id"), primary_key=True)
    url = db.Column(db.String(200))

    empresa = db.relationship("Usuario_emp", back_populates="redes")
    red = db.relationship("Tipo_red", back_populates="red_empresas")


class Usuario_reg(db.Model):

    __tablename__ = "usuario_reg" 

    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True)
    contraseña = db.Column(db.String(20))
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    fecha_nacimiento = db.Column(db.DateTime)
    genero = db.Column(db.Integer)
    fotoPerfil = db.Column(db.String(200))
    id_nacionalidad = db.Column(db.Integer, db.ForeignKey("nacionalidad.id")) # FK

    seguidos = db.relationship(
        "Usuario_emp",
        secondary=sigue, 
        backref=db.backref("clientes", lazy="dynamic"))

    locales_valorados = db.relationship("Valoracion", back_populates="usuario")

class Usuario_emp(db.Model):

    __tablename__ = "usuario_emp"

    id = db.Column(db.Integer, primary_key=True)
    ruc = db.Column(db.Integer)
    contraseña = db.Column(db.String(20))
    nombre = db.Column(db.String(30))
    correo = db.Column(db.String(30), unique=True)
    telefono = db.Column(db.Integer)

    redes = db.relationship("Tiene_redes", back_populates="empresa")
    
    locales = db.relationship(
        "Local",
         backref="empresa",
         lazy="select")


class Nacionalidad(db.Model):
    __tablename__ = "nacionalidad"
    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(20)) 

    usuarios = db.relationship(
        "Usuario_reg", 
        backref="nacionalidad", 
        lazy="select")

class Tipo_red(db.Model): 

    __tablename__ = "tipo_red"

    id = db.Column(db.Integer, primary_key=True)
    redsocial = db.Column(db.String(20))

    red_empresas = db.relationship("Tiene_redes", back_populates="red")

class Local(db.Model):

    __tablename__ = "local"

    id = db.Column(db.Integer, primary_key=True)

    direccion = db.Column(db.String(100))
    nombre = db.Column(db.String(15))
    descripcion = db.Column(db.String(1000))
    horaApertura = db.Column(db.String(10))
    horaCierre = db.Column(db.String(10))
    fotoPresentacion = db.Column(db.String(200))

    #id_fotocarta = db.Column(db.Integer, db.ForeignKey("foto_carta.id_local")) #FK

    id_distrito = db.Column(db.Integer, db.ForeignKey("distrito.id")) #FK
    id_empresa = db.Column(db.Integer, db.ForeignKey("usuario_emp.id")) #FK

    longitud = db.Column(db.Integer)
    latitud = db.Column(db.Integer)

    musicas = db.relationship(
        "Tipo_musica",
        secondary=tiene_musica, 
        backref=db.backref("locales_musica", lazy="dynamic"))
    ambientes = db.relationship(
        "Tipo_ambiente",
        secondary=tiene_ambiente, 
        backref=db.backref("locales_ambiente", lazy="dynamic"))

    eventos = db.relationship(
        "Evento",
        backref="empresa",
        lazy="select"
    )

    valoraciones = db.relationship("Valoracion", back_populates="local")

    fotos_carta = db.relationship("Foto_carta", backref="local", lazy="select")

class Tipo_musica(db.Model):

    __tablename__= "tipo_musica"

    id = db.Column(db.Integer, primary_key=True)
    musica = db.Column(db.String(30))

class Tipo_ambiente(db.Model):
    __tablename__= "tipo_ambiente"
    id = db.Column(db.Integer, primary_key=True)
    ambiente = db.Column(db.String(30))


class Distrito(db.Model):
    __tablename__="distrito"
    id = db.Column(db.Integer, primary_key=True)
    distrito = db.Column(db.String(30))

    locales_distrito = db.relationship(
        "Local",
        backref="distrito",
        lazy="select"
    )


class Evento(db.Model):

    __tablename__ = "evento"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    descripcion = db.Column(db.String(1000))
    fechaInicio = db.Column(db.String(15))
    fechaFin = db.Column(db.String(15))
    imagen = db.Column(db.String(200))
    precio = db.Column(db.Integer)
    id_local = db.Column(db.Integer, db.ForeignKey("local.id")) #Fk

class Foto_carta(db.Model):
    __tablename__ = "foto_carta"
    id = db.Column(db.Integer, primary_key=True)
    id_local = db.Column(db.Integer, db.ForeignKey("local.id"))
    url = db.Column(db.String(200))
