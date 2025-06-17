from scripts.script_class import Script
from pynput.mouse import Controller
from time import sleep


class RefreshCenterComputer(Script):
    
    def __init__(self) -> None:
        super().__init__("RefreshCenterComputer", False)
        self.mouse = Controller()

    def action(self) -> str:
        self.mouse.move(1, 1)
        sleep(0.1) # Not optimal
        self.mouse.move(-1, -1)
        return ''

