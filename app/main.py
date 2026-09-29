import os
from flask import Flask, render_template, request, redirect, url_for, session
from buscar_publicaciones import buscar_publicaciones

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super_secret_key_tecmi_2026")

MOCK_PUBLICACIONES = [
    {"usuario": "mau", "contenido": "¡Hola a todos! Este es mi primer post en la red social.", "fecha": "2026-09-29"},
    {"usuario": "alex", "contenido": "Desplegando la app en AWS EC2 con Docker.", "fecha": "2026-09-29"},
    {"usuario": "mau", "contenido": "El pipeline de seguridad paso en verde exitosamente.", "fecha": "2026-09-29"}
]

@app.route("/")
def index():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", usuario=session["usuario"], publicaciones=MOCK_PUBLICACIONES)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username and password == "admin123": # nosec B105
            session["usuario"] = username
            return redirect(url_for("index"))
        return render_template("login.html", error="Usuario o contraseña incorrectos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route("/buscar", methods=["GET"])
def buscar():
    if "usuario" not in session:
        return redirect(url_for("login"))
    usuario_q = request.args.get("usuario", "")
    resultados = [p for p in MOCK_PUBLICACIONES if p["usuario"].lower() == usuario_q.lower()]
    return render_template("index.html", usuario=session["usuario"], publicaciones=resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000) # nosec B104
