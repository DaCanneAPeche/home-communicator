from scripts.script_class import Script
from flask import render_template


class {class_name}(Script):
    def __init__(self) -> None:
        super().__init__("{name}", {is_a_page})

    def action(self) -> str:
        return {action_return}
