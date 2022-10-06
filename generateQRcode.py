# WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;
import qrcode

# QR code made quick
def quickQR():
    img = qrcode.make('Can you read this?')
    type(img) #make image
    img.save("qrcode.png")

def advancedQR():
    qr = qrcode.QRCode(
        version=1, #controls size, 1 is smallest, 40 is largest
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image(fill_color=(55, 95, 35), back_color=(255, 195, 235))
    img.save("advQrCode.png")


advancedQR()