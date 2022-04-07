# import necessary libraries
from cgitb import text
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
website = "https://www.huawei.com/"
text = "Hello World"
# file = "C:\Users\t50022566\Downloads\Access Network Basics.pptx"

# File name of the QR code Image
# Change it with your desired file name
QRCodefile = "fcode.png"
QRCodetext = "tcode.png"
QRCodeimage = "icode.png"
QRCodeweb = "wcode.png"
# Generating the QR code
QRtext = qrcode.make(text)
QRimage = qrcode.make('C:/Users/t50022566/Downloads/images_0.jpg')
# Saving image into a file
QRtext.save(QRCodetext)
QRimage.save(QRCodeimage)


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("img.png")