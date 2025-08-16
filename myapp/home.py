
from flask import (Blueprint,render_template)
from myapp.db import get_db
bp=Blueprint("home",__name__)


@bp.route("/")
def index():
    return render_template("home.html")


   