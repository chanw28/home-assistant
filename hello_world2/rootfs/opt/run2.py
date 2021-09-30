#!/usr/bin/python3
 
msg = "Hello World2b from python run2.py!"
logger.info(msg)
hass.bus.fire(name, {"wow": "from a Hello_World2b run2.py"})