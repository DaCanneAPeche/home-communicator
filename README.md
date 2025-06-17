# Home communicator

A program that makes it able to make actions on a center computer by distance
from any devices connected on the same Wi-Fi. Makes it able to use your phone
as a remote controller for exemple.

## Warning
The program is made to be used in a local environment, never open the port where
the program is running (see in `main.py`).

## How it works
It creates a local web server that can be accessed from any local devices and
then use websockets to communicate.

## Install deps
```
pip install -r requirements.txt
```

## Create scripts 
Run `create_script/create_script.py` and answer the questions. A page is a script
with an HTML page instead of a single websocket request.

### Scripts
```python
# scripts/<script name>.py
def action(self) -> str:
    # the action that your computer needs to do like moving the mouse 
    return ``
```

### Pages
```python
# scripts/<page name>.py

# In the constructor :
self.add_socket_event("socket name", function) # register a socket event 
```

```javascript
// static/js/pages/<page name>.js 
socket.emit("socket name");
```

edit html : 
```html

{% block head %}
    <!-- page head -->
{% head %}

{% block content %}
    <!-- page content -->
{% endblock %}
```
adit css : `static/css/<page name>.css`

## Favorites
Open the side menu and click on the star, the script / page will now appear
directly on the screen

## Screenshot
You can change the colors in `static/css/base.css`. By default, uses the 
[catppuccin](https://catppuccin.com/) color palette.
