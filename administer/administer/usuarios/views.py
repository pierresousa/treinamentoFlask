from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)

usuarios = Blueprint('usuarios', __name__,template_folder='templates/usuarios')