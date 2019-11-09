from flask import Flask, render_template, request, redirect, url_for
import os
import cx_Oracle

app = Flask(__name__)

# ORACLE CONNECTION
connection = cx_Oracle.connect("dummy2/dummy2@localhost:49161/xe")

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/musi")
def casa():
    return render_template("axel.html")


@app.route("/about")
def acercaDe():
    return render_template("about.html")


@app.route("/agregar_usuarios")
def addUsers():
    return render_template("AgregarUsuarios.html")


@app.route("/add_user", methods=["POST"])
def addUser():
    if request.method == "POST":
        cur = connection.cursor()
        nombre = request.form["name"]
        apellidos = request.form["lastName"]
        email = request.form["email"]
        psswd = request.form["password"]

        cur.execute( "INSERT INTO usuarios(NOMBRE, APELLIDO, CORREO, PASSWORD, ES_ACTIVO) VALUES ('%s','%s','%s','%s','%s')" % (nombre, apellidos, email, psswd, '1'))
        connection.commit()
        cur.close()
    return redirect("/agregar_usuarios")


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
