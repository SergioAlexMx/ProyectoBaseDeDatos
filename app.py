from flask import Flask, render_template, request, redirect, url_for, flash
import os
import cx_Oracle
from flask import Flask, render_template, request

app = Flask(__name__)

# ORACLE CONNECTION
connection = cx_Oracle.connect("dummy2/dummy2@localhost:49161/xe")
fusuarAdd = False

# private session
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template("home.html")


@app.route("/about")
def acercaDe():
    return render_template("about.html")


@app.route("/agregar_usuarios")
def addUsers():
    return render_template("AgregarUsuarios.html")


@app.route("/usuario_agregado")
def usuarioAgregado():
    return render_template("usuarioAgregado.html")

@app.route("/mostrar_usuarios")
def mostrarUsuarios():
    cur = connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
    cur.close()
    return render_template("mostrar_usuarios.html", users = data)


@app.route("/delete_user/<string:id>")
def deleteUser(id):
    cur = connection.cursor()
    cur.execute("DELETE FROM usuarios WHERE id_usuario = %s" %(id))
    connection.commit()

    return redirect("/mostrar_usuarios")

@app.route("/add_user", methods=["POST"])
def addUser():
    if request.method == "POST":
        cur = connection.cursor()
        nombre = request.form["name"]
        apellidos = request.form["lastName"]
        email = request.form["email"]
        psswd = request.form["password"]

        cur.execute(
            "INSERT INTO usuarios(NOMBRE, APELLIDO, CORREO, PASSWORD, ES_ACTIVO) VALUES ('%s','%s','%s','%s','%s')" % (
            nombre, apellidos, email, psswd, '1'))
        connection.commit()
        cur.close()
        fusuarAdd = True
    return redirect("/add_user")


@app.route("/testDB")
def testDB():
    cur = connection.cursor()

    cur.execute("SELECT 'HELLO WORLD ' from dual")
    col = cur.fetchone()[0]
    txtOut = "<p> exec: \"SELECT 'HELLO WORLD ' from dual\" </p>" + col + " <br> Oracle Database version: " + connection.version
    cur.close()
    return txtOut


if __name__ == '__main__':
    app.run()
