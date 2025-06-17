from scripts.script_class import Script
import scripts
import inspect
from flask import Flask
import os
from flask_socketio import SocketIO
from TOMLdatabase import TOMLDataBase


class ScriptsManager:

    def __init__(self, database: TOMLDataBase) -> None:
        self.database = database

        self.scripts : list[Script] = []
        self.script_names : list[str] = []

        self.pages : list[Script] = []
        self.pages_names : list[str] = []

        self.favorites : list[dict] = []

        self.import_all_scripts()
        self.get_all_classes()
        self.get_script_names()
        self.init_favorites()

    def import_all_scripts(self) -> None:
        """
        Necessary function for inspect to work properly
        """
        for file in os.listdir("./scripts"):
            if file not in ("__init__.py", "script_class.py", "__pychache__"):
                file_name = file.split('.')[0]
                __import__(f"scripts.{file_name}")

    def add_scripts(self, app: Flask, socketio: SocketIO) -> None:
        for script in self.scripts:
            socketio.on_event(f"/scripts/{script.name}", script.action)
            script.init_socketio_events(socketio=socketio)

        for page in self.pages:
            app.add_url_rule(f"/pages/{page.name}", page.name, page.action)
            page.init_socketio_events(socketio=socketio)

    def get_all_classes(self) -> None:
        for _, obj in inspect.getmembers(scripts):
            if inspect.ismodule(obj):
                self.get_all_classes_from_script(obj)

    def get_all_classes_from_script(self, script) -> None:
        for _, obj in inspect.getmembers(script):
            if inspect.isclass(obj) and Script in obj.__bases__:
                instance = obj()
                if not instance.is_a_page:
                    self.scripts.append(instance)
                else:
                    self.pages.append(instance)

    def get_script_names(self) -> None:
        for script in self.scripts:
            self.script_names.append(script.name)

        for page in self.pages:
            self.pages_names.append(page.name)

    def add_to_favorites(self, new_favorite : str) -> str:
        if len(self.favorites) >= self.database["favorites"]["favorites_lenght"]:
            return "Too many favorites"

        if self.is_a_favorite(new_favorite):
            return "Already a favorite"

        favorite = {"name": new_favorite, "is_a_page": None}

        if new_favorite in self.script_names:
            favorite["is_a_page"] = False
        elif new_favorite in self.pages_names:
            favorite["is_a_page"] = True
        else:
            return "Script/pages does not exist"

        self.favorites.append(favorite)
        self.update_database_favorites()
        return "Favorite added"

    def remove_from_favorites(self, favorite_name : str) -> str:
        if not self.is_a_favorite(favorite_name):
            return "Not a favorite"

        for favorite in self.favorites:
            if favorite["name"] == favorite_name:
                self.favorites.remove(favorite)
                self.update_database_favorites()
                break

        return "Favorite removed"

    def is_a_favorite(self, possible_favorite : str) -> bool:
        for favorite in self.favorites:
            if favorite["name"] == possible_favorite:
                return True
        return False

    def init_favorites(self) -> None:
        # Trunk favorites to the right length
        self.database["favorites"]["favorites"] =\
            self.database["favorites"]["favorites"][:self.database["favorites"]["favorites_lenght"]]

        # Remove favorites that are not valid scripts / pages
        for favorite in self.database["favorites"]["favorites"]:
            if not favorite["is_a_page"] and favorite["name"] not in self.script_names or\
                    favorite["is_a_page"] and favorite["name"] not in self.pages_names:
                self.database["favorites"]["favorites"].remove(favorite)

        self.database.save()
        self.favorites = self.database["favorites"]["favorites"]

    def update_database_favorites(self) -> None:

        self.database["favorites"]["favorites"] = self.favorites
        self.database.save()

