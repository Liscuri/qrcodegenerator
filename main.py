import qrcode
import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.RED + """
  _____   ______       ______ _______ __   _ _______  ______ _______ _______  _____   ______
 |   __| |_____/      |  ____ |______ | \  | |______ |_____/ |_____|    |    |     | |_____/
 |____\| |    \_      |_____| |______ |  \_| |______ |    \_ |     |    |    |_____| |    \_                                                                                                                                                                                                                                                                                                                                                    
""")
print(Style.RESET_ALL)

print(Fore.GREEN + "Welcome to QR Code Generator")

data = input(Fore.BLUE + "Enter the text or link you want to convert to QR Code: ")
print(Style.RESET_ALL)

choice = input(Fore.BLUE + "Do you want to change any data of the QR Code (For eg. box size, border or the color)? (y/n): ")

if choice == "y":
    box_size = int(input(Fore.BLUE + "Enter the box size: "))
    border = int(input(Fore.BLUE + "Enter the border size: "))
    fill_color = input(Fore.BLUE + "Enter the fill color hex: ")
    back_color = input(Fore.BLUE + "Enter the background color hex: ")
    print(Style.RESET_ALL)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=f"{fill_color}", back_color=f"{back_color}")

    filename = input(Fore.BLUE + "Enter the name of the file you want to save the QR Code: ")
    imgfolder = "images/" + filename + ".png"
    img.save(imgfolder)

    print(Fore.GREEN + "QR Code generated successfully! Exiting the program...")
    print(Style.RESET_ALL)
else:
    img = qrcode.make(data)
    type(img)

    filename = input(Fore.BLUE + "Enter the name of the file you want to save the QR Code: ")
    imgfolder = "images/" + filename + ".png"
    img.save(imgfolder)

    print(Fore.GREEN + f"QR Code generated successfully! Saved in  Exiting the program...")
    print(Style.RESET_ALL)
