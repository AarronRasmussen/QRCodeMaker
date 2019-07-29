import argparse
import qrcode

parser = argparse.ArgumentParser()
parser.add_argument("qrData")
parser.add_argument("imgSave")
args = parser.parse_args()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(args.qrData)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(args.imgSave)

