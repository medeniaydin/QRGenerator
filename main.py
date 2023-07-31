import pyqrcode

url = input("Enter url to generate qr code: ")
qr_code = pyqrcode.create(url)

qr_code.svg("qrCode.png", scale=6)