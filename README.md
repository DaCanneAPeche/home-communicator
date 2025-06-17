# Home communicator

A program that makes it able to make actions on a center computer by distance
from any devices connected on the same Wi-Fi. Make it able to use your phone
as a remote controller for exemple.

## How it works
It creates a local web server that can be accessed from any local devices and
then use websockets to communicate.

## Create scripts 
Run 'create_script/create_script.py' and answer the question. A page is a script
with an HTML page instead of a single websocket.

## Warning
The program is made to be used in a local environment, never open the port where
the program is running (see in 'main.py')
