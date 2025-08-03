import qrcode


#1st install QRcode go to terminal and open it
# command: pip install qrcode ei library ta install korte hobe
# ekhon qrcode ke convert kore amra  image file akare save korte chaschi
# ekhon full command ta amra eivabe likhte pari pip install qrcode[pil] eivabe likhle pillow library takeo se install kore nibe



 # তুমি ভুল করে 'qrcode' আর 'text' এক লাইনে লিখে ফেলেছিলে, এটা ঠিক করলাম

# ইউজার থেকে ইনপুট নেওয়া
"""text = input("Enter the text to convert in the QR code: ")
filename = input("Enter the filename to save the QR code (with .png extension): ")

# QR কোড তৈরি করার ফাংশন
def generator_qr_code(text, filename):
    # make qrcode with make() function
    image_qrcode = qrcode.make(text)
    
    # save the image
    image_qrcode.save(filename)
    print(f"QR code saved as {filename}")

# ফাংশন কল
generator_qr_code(text, filename)"""

# ekhon amra chaschi input type na kore file er maddhome read kore anbo
# 1st e ekta txt file nibo dhoren nam dilam input.txt

def generator_qr_code(filepath):
    with open (filepath, "r") as file:
        lines = file.readlines() #[prothomline, secondline] evabe store hobe
        text = lines[0].strip()
        filename = lines[1].strip()
    #qrcode make()
    image_qrcode = qrcode.make(text)

    #save the image
    image_qrcode.save(filename)

#generator_qr_code('input.txt') 

#ekhon amra jodi input.txt file ta ekta input nam er folder er vitore rakhtam tahole input.txt file er copy relative path ta copy kore function call er vitore diye dibo
 #generator_qr_code('input\input.txt') # ekhane \ ta eivabe nadiye/ ei vabe dite hobe

generator_qr_code('input/input.txt')
