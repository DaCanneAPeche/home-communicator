from __main__ import socketio, scripts_manager
from flask_socketio import emit


@socketio.on("add-favorite")
def add_to_favorites(script: str) -> list:

    response : list = scripts_manager.add_to_favorites(script)

    emit("favorites-change", scripts_manager.favorites, broadcast=True)

    return response

@socketio.on("remove-favorite")
def remove_from_favorites(script: str) -> list:
    
    response : list = scripts_manager.remove_from_favorites(script)

    emit("favorites-change", scripts_manager.favorites, broadcast=True)

    return response

@socketio.on("get-favorites")
def get_favorites(_) -> list:
    return scripts_manager.favorites

