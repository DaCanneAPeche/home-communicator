#!/usr/bin/env python3
from flask import Flask, render_template
import socket
import qrcode
from scripts_manager import ScriptsManager
from flask_socketio import SocketIO
from TOMLdatabase import TOMLDataBase


PORT = 8080
app = Flask(__name__)
socketio = SocketIO(app)
database : TOMLDataBase = TOMLDataBase("./database.toml") 

# Dynamicly generating web urls / socketio event for the scripts
scripts_manager = ScriptsManager(database=database)
scripts_manager.add_scripts(app, socketio)

import favorites # Is here in order not to get a circular import, import socket io events

@app.route('/')
def home():
    return render_template("home.html")

@app.context_processor
def pass_scripts_and_pages_to_templates():
    return dict(scripts=scripts_manager.script_names, pages=scripts_manager.pages_names)

def get_ip_adress():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        hostname = s.getsockname()[0]

    return hostname

def create_qrcode(*, show_qrcode : bool = False, ip_adress: int):
    image = qrcode.make(f"http://{ip_adress}:{PORT}")
    image.save("./static/img/qrcode.jpg")
    image.save("qrcode.jpg")
    if show_qrcode:
        image.show("QR CODE")


if __name__ == "__main__":

    ip_adress = get_ip_adress()
    
    print(f"\n- http://127.0.0.1:{PORT}\n- http://{ip_adress}:{PORT}\n")

    create_qrcode(ip_adress=ip_adress, show_qrcode=True)
    socketio.run(app, host="0.0.0.0", port=PORT, debug=False)
