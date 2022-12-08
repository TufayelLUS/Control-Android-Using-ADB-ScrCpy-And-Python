from ppadb.client import Client


# to mirror and control a screen: https://github.com/Genymobile/scrcpy
# pip3 install pure-python-adb
# to get screen tap coordinates, enable pointer on developer option
# the developer options, usb debugging, tap and input gesture permission needs to be enableda


client = Client()
devices = client.devices()
device = devices[0]
# you can send a tap signal using x,y coordinate
device.shell("input touchscreen tap 161 2151")
# you can swipe from x1,y1 to x2,y2
device.shell("input swipe x1 y1 x2 y2")
# you can send type signal
device.shell("input text \"This is a text\"")
