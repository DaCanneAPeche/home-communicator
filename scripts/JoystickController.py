from scripts.script_class import Script
from flask import render_template
from pynput.mouse import Controller as Mouse, Button
from pynput.keyboard import Controller as Keyboard, Key


MOUSE_SENSIBILITY = 30
SCROLL_SENSIBILITY = 10

class JoystickController(Script):
    def __init__(self) -> None:
        super().__init__("JoystickController", True)
        self.mouse = Mouse()
        self.keyboard = Keyboard()

        self.add_socket_event("left-click", self.on_left_click)
        self.add_socket_event("right-click", self.on_right_click)
        self.add_socket_event("text-input", self.on_text_input)
        self.add_socket_event("backspace", self.on_backspace)
        self.add_socket_event("enter", self.on_enter)
        self.add_socket_event("move-mouse", self.on_move_mouse)
        self.add_socket_event("scroll", self.on_scroll)

    def action(self) -> str:
        return render_template('/pages/JoystickController.html')

    def on_left_click(self) -> None:
        self.mouse.click(Button.left)

    def on_right_click(self) -> None:
        self.mouse.click(Button.right)

    def on_text_input(self, text: str) -> None:
        self.keyboard.type(text)

    def on_backspace(self) -> None:
        self.keyboard.press(Key.backspace)
        self.keyboard.release(Key.backspace)

    def on_enter(self) -> None:
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def on_move_mouse(self, normalized_vector: list[int]) -> None:
        self.mouse.move(normalized_vector[0] * MOUSE_SENSIBILITY, normalized_vector[1] * MOUSE_SENSIBILITY)

    def on_scroll(self, amount: str) -> None:
        self.mouse.scroll(0, int(float(amount) * SCROLL_SENSIBILITY))
