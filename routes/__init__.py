from flask import Flask, render_template, request, session, redirect, url_for, Blueprint
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_

routes = Blueprint('routes', __name__, static_folder=".\template", template_folder=".\templates")

from .login import *
from .registro_usuario import * 
from .calendario import *
from .pag_principal import * 
from .perfil_cliente import * 
from .perfil_empresa import * 
from .registro_local import * 

