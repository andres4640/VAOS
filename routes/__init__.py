from flask import Flask, render_template, request, session, redirect, url_for, Blueprint, flash
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local, Evento, Tiene_redes
from sqlalchemy import and_, or_

routes = Blueprint('routes', __name__, static_folder=".\template", template_folder=".\templates")

from .login import *
from .registro_usuario import * 
from .calendario import *
from .pag_principal import * 
from .perfil_cliente import * 
from .perfil_empresa import * 
from .perfil_local import * 
from .registro_local import * 
from .registro_evento import * 
from .locales_company import * 
from .eventos_company import * 
from .perfil_empresa_editar import * 
from .perfil_cliente_editar import * 
from .perfil_local_editar import *
from .perfil_evento import *
from .eventos_seguidos import *

