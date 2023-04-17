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

while True:
    data = input(Fore.BLUE + "Enter the text or link you want to convert to a QR Code: ")
    if not data:
        print(Fore.RED + "Please enter the text or link you want to convert to a QR Code!")
    else:
        print(Style.RESET_ALL)
        break

while True:
    choice = input(Fore.BLUE + "Do you want to change any data of the QR Code (For eg. box size, border or the color)? (y/n): ")
    if not choice:
        print(Fore.RED + "Please make a choice! (y/n)")
    elif choice == "y" or choice == "n":
        print(Style.RESET_ALL)
        break


if choice == "y":
    while True:
        box_size = int(input(Fore.BLUE + "Enter the box size: ") or 0)
        if box_size < 1:
            print(Fore.RED + "Please enter the box size!")
        else:
            break

    while True:
        border = int(input(Fore.BLUE + "Enter the border size: ") or 0)
        if border < 1:
            print(Fore.RED + "Please enter the border size!")
        else:
            break

    while True:
        fill_color = input(Fore.BLUE + "Enter the fill color hex: ")
        if not fill_color:
            print(Fore.RED + "Please enter the fill color hex!")
        else:
            break

    while True:
        back_color = input(Fore.BLUE + "Enter the background color hex: ")
        if not back_color:
            print(Fore.RED + "Please enter the background color hex!")
        else:
            break
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

    while True:
        filename = input(Fore.BLUE + "Enter the name of the file you want to save the QR Code: ")
        if not filename:
            print(Fore.RED + "Please enter the name of the file for your QR Code!")
        else:
            break
    img_folder = "images/" + filename + ".png"
    img.save(img_folder)

    print(Fore.GREEN + "QR Code generated successfully! Exiting the program...")
    print(Style.RESET_ALL)
else:
    img = qrcode.make(data)
    type(img)

    while True:
        filename = input(Fore.BLUE + "Enter the name of the file you want to save the QR Code: ")
        if not filename:
            print(Fore.RED + "Please enter the name of the file for your QR Code!")
        else:
            break
    img_folder = "images/" + filename + ".png"
    img.save(img_folder)

    print(Fore.GREEN + f"QR Code generated successfully! Exiting the program...")
    print(Style.RESET_ALL)
