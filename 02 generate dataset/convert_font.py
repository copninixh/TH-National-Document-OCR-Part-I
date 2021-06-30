from PIL import Image, ImageFont, ImageDraw
import os
import codecs

list = [("THSarabunIT9","THSarabunIT๙.ttf" , "IT9" , "Normal"),
("THSarabunIT9","THSarabunIT๙ Italic.ttf" , "IT9" , "Italic"),
("THSarabunIT9","THSarabunIT๙ Bold.ttf" , "IT9" , "Bold"),
("THSarabunIT9","THSarabunIT๙ BoldItalic.ttf" , "IT9" , "BoldItalic"),
("THSarabunPSK","THSarabun.ttf" , "PSK" , "Normal"),
("THSarabunPSK","THSarabun Italic.ttf" , "PSK" , "Italic"),
("THSarabunPSK","THSarabun Bold.ttf" , "PSK" , "Bold"),
("THSarabunPSK","THSarabun BoldItalic.ttf" , "PSK" , "BoldItalic"),
("THSarabunNew","THSarabunNew.ttf" , "New" , "Normal"),
("THSarabunNew","THSarabunNew Italic.ttf" , "New" , "Italic"),
("THSarabunNew","THSarabunNew Bold.ttf" , "New" , "Bold"),
("THSarabunNew","THSarabunNew BoldItalic.ttf" , "New" , "BoldItalic")
]

for t in list:
    font_path = "fonts/{}/".format(t[0])
    font_name = t[1]
    out_path = "Dataset/{}/{}/".format(t[0],t[3])

    font_size = 72 # px
    font_color = "#000000" # HEX Black
    bg_color = '#ffffff'
    width = 120 
    height = 120

    # Create Font using PIL
    font = ImageFont.truetype(font_path+font_name, font_size)

   

    desired_characters = "ๅํ็่้๊๋ฯฺๆ์ํ๎๏๚๛฿"
    list_character = [("1","ABCČĆDĐEFG"),
    ("2","HIJKLMNOPQ"),
    ("3","RSŠTUVWXYZ"),
    ("4","Žabcčćdđef"),
    ("5","ghijklmnop"),
    ("6","qrsštuvwxy"),
    ("7","zž12345678"),
    ("8","90‘?’“!”(%"),
    ("9",")[#]{@}/&"),
    ("10","<-+÷×=>®©$"),
    ("11","€£¥¢:;,.*ก"),
    ("12","ขฃคฅฆงจฉชซ"),
    ("13","ฌญฎฏฐฑฒณดต"),
    ("14","ถทธนบปผฝพฟ"),
    ("15","ภมยรลวศษสห"),
    ("16","ฬอฮฤฦะัาำิ"),
    ("17","ีึืุูเแโไใ"),
    ("18","ๅํ็่้๊๋ฯฺๆ"),
    ("19","์ํ๎๏๚๛฿ฺ0"),
    ("20","๐๑๒๓๔๕๖๗๘๙")
    ]

    for cs in list_character:

        desired_characters = cs[1]

        for character in desired_characters:
            
            # Create PNG Image with that size
            img = Image.new("RGBA", (width, height), color=bg_color)
            draw = ImageDraw.Draw(img)
            position = (50,20)
            
            # Draw the character
            
            draw.text(position, str(character), font=font, fill=font_color)
            # Save the character as png
            try:
                img.save(out_path + "format_" + cs[0] + "_" + t[0] + "_" + t[3] + "_" + str(ord(character)) + ".png")
                file_name = out_path + "format_" + cs[0] + "_" + t[0] + "_" + t[3] + "_" + str(ord(character)) + ".gt.txt"
                file = codecs.open(file_name, "w", "utf-8") 
                file.write("{}".format(character)) 
                file.close() 
            except:
                print(f"[-] Couldn't Save:\t{character}")