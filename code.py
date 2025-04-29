import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Coding With Md Musheer Anjum Posti")
qr.png("MyCode.png", scale=8)