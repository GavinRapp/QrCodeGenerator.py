#  install libraries needed
import grcode

# create function that collects text and converts it to QR Code
def generate_qrcode(text):

    qr = qrcode.QRCpde(
        version = 1,
        error_correction = qrcode.constants.ERROT_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
# save QR Code as an image
    img.save("qrimg.png")

# run the function
generate_qrcode("https://www.protonmail.com ")