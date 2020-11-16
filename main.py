import qrcode
import datetime

data = input("Enter the data > ")

datalen = len(data)
BOX_SIZE = 8

if datalen > 1000:
	print("The clarity and the details will be so small to be scanned try reducing characters!\nThis will still create the QR Code.")
	BOX_SIZE = 2
elif datalen > 700:
	BOX_SIZE = 2
elif datalen > 600:
	BOX_SIZE = 3
elif datalen < 400 and datalen > 80:
	BOX_SIZE = 4
elif datalen > 0:
	BOX_SIZE = 8
else:
	print("Please enter some text")
	exit(1)

filename = input("Enter the filename > ").strip(".png").strip()
if len(filename) < 1:
	date = datetime.datetime.now()
	filename = f'{date.day}-{date.month}-{date.year}[{date.hour}-{date.minute}-{date.second}]'
	print("It seems you dont have time to enter the filename so I entered for you as",filename)


img = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=BOX_SIZE,
    border=4,
)

img.add_data(data)
img.make(fit=True)

qr_img = img.make_image(fill_color="black", back_color="white")


qr_img.save(filename + ".png")