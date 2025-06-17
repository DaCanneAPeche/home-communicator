from scripts.script_class import Script
from flask import render_template


class QrCode(Script):
    def __init__(self) -> None:
        super().__init__("QrCode", True)

    def action(self) -> str:
        return render_template('/pages/QrCode.html')
