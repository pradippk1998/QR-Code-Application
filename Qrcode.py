# for creating QR code first we need to install package "pyqrcode"
import pyqrcode

url=input("Enter a url to generate QR code: ")

QR=pyqrcode.create(url)

QR.png("webqr.png", scale=8)