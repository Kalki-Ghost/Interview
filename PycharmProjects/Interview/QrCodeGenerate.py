# Codes generate the qrcode
import qrcode

qr = qrcode.QRCode(version=15, box_size=20, border=10)

data = "9035615310@axl"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("text.png")
