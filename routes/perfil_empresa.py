from . import routes
from flask import Flask, render_template, request, session, redirect, url_for
from database import db, Usuario_reg, Usuario_emp, Tipo_ambiente, Tipo_musica, Tipo_red, Nacionalidad, Valoracion, Local
from sqlalchemy import and_, or_