We first import the pyqrcode library.
We prompt the user to enter a URL using the input() function and store it in the url variable.
We create the QR code using pyqrcode.create(url) and store it in the qr variable.
Finally, we save the QR code as a PNG image using qr.png("webqr.png", scale=8). The scale parameter determines the size of the QR code image.
The generated QR code image will be saved in the current directory with the filename webqr.png.
