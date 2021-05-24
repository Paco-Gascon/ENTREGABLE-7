#!/usr/bin/python3


from flask import Flask, render_template
import platform, os, socket, subprocess

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
	return render_template('index.html',mensaje=['SYSTEM CHECK',''])


@app.route("/<parametro>")
def mostrar(parametro):

	if parametro=="so":
		return render_template('index.html', mensaje=['SISTEMA OPERATIVO',
platform.system()])


#----------------------INICIO CODIGO NUEVO--------------------------------#

	elif parametro=="ip":
                return render_template('index.html', mensaje=['IP LOCAL',
socket.gethostbyname(socket.gethostname()+'.local')])

	elif parametro=="nombre":
                return render_template('index.html', mensaje=['NOMBRE DEL EQUIPO',
socket.gethostname()])

	elif parametro=="reinicio":
                return render_template('index.html', mensaje=['REINICIO REMOTO',
subprocess.run("reboot")])



#----------------------FIN CODIGO NUEVO------------------------------------#

	else:
		return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)


