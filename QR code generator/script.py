import pyqrcode
import png
from pyqrcode import QRCode

def myqrcode():
    s = input("Enter value to generate qr code:")
    q = pyqrcode.create(s)
    q.png('qrcode.png', scale=6)
    print("QR code generated")

myqrcode()
