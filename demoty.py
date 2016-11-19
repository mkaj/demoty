import PIL, os
from PIL import ImageEnhance, Image, ImageOps, ImageDraw, ImageFont
from random import randint

TEMPLATE_FILENAME = 'template.jpg'
TEMPLATE_COORDS = (75, 45, 499, 373)
PHRASES_FILENAME = 'phrases.txt'
EXTENSIONS = ['.jpg', '.png']

UPPER_FONT = 'times.ttf'
LOWER_FONT = 'arial.ttf'

W = 574
H = 522

def isValidExtension(filename):
    for extension in EXTENSIONS:
        if filename.endswith(extension):
            return True
    return False

def getRandomImage():
    fileList = []
    for dirpath, dirnames, filenames in os.walk('.'):
        if TEMPLATE_FILENAME in filenames: filenames.remove(TEMPLATE_FILENAME)
        for filename in [f for f in filenames if isValidExtension(f)]:
            fileList.append(filename)
    return fileList[randint(0, len(fileList) - 1)]

def getPhrases():
    with open(PHRASES_FILENAME) as file:
        content = file.read().splitlines()
    return content

def getRandomPhrase():
    phraseList = getPhrases()
    return phraseList[randint(0, len(phraseList) - 1)]

def makeImage():
    frame = PIL.Image.open(TEMPLATE_FILENAME)
    demot = PIL.Image.open(getRandomImage())
    demot = demot.resize((TEMPLATE_COORDS[2] - TEMPLATE_COORDS[0], TEMPLATE_COORDS[3] - TEMPLATE_COORDS[1]), PIL.Image.ANTIALIAS)
    frame.paste(demot, TEMPLATE_COORDS)

    draw = ImageDraw.Draw(frame)

    upperText = getRandomPhrase()
    upperTextFont = ImageFont.truetype(UPPER_FONT, 45)
    w, h = upperTextFont.getsize(upperText)
    draw.text((int((W-w)/2),390), upperText, font=upperTextFont)

    lowerText = getRandomPhrase()
    lowerTextFont = ImageFont.truetype(LOWER_FONT, 16)
    w, h = lowerTextFont.getsize(lowerText)
    draw.text((int((W-w)/2),460), lowerText, font=lowerTextFont)
    
    frame.show()

makeImage()
