import PIL, os
from PIL import ImageEnhance, Image, ImageOps, ImageDraw, ImageFont
from random import randint

TEMPLATE_FILENAME = 'template.jpg'
PHRASES_FILENAME = 'phrases.txt'
EXTENSIONS = ['.jpg', '.png']

UPPER_FONT = 'times.ttf'
UPPER_SIZE = 45
LOWER_FONT = 'arialbd.ttf'
LOWER_SIZE = 14

TEMPLATE_WIDTH = 574
TEMPLATE_HEIGHT = 522
TEMPLATE_COORDS = (75, 45, 499, 373)
PADDING = 10

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
    return PIL.Image.open(fileList[randint(0, len(fileList) - 1)])

def getPhrases():
    with open(PHRASES_FILENAME) as file:
        content = file.read().splitlines()
    return content

def getRandomPhrase():
    phraseList = getPhrases()
    return phraseList[randint(0, len(phraseList) - 1)]

def drawXAxisCenteredText(image, text, font, size, pos_y):
    draw = ImageDraw.Draw(image)
    textFont = ImageFont.truetype(font, size)
    textWidth = textFont.getsize(text)[0]

    i = 1
    while textWidth >= TEMPLATE_WIDTH - PADDING:
        textFont = ImageFont.truetype(font, size - i)
        textWidth = textFont.getsize(text)[0]
        i += 1
        
    draw.text(((TEMPLATE_WIDTH - textWidth) / 2, pos_y), text, font = textFont)

def getSizeFromArea(area):
    return (area[2] - area[0], area[3] - area[1])

def makeImage():
    frame = PIL.Image.open(TEMPLATE_FILENAME)
    demot = getRandomImage()
    demot = demot.resize(getSizeFromArea(TEMPLATE_COORDS), PIL.Image.ANTIALIAS)
    frame.paste(demot, TEMPLATE_COORDS)

    drawXAxisCenteredText(frame, getRandomPhrase(), UPPER_FONT, UPPER_SIZE, 390)
    drawXAxisCenteredText(frame, getRandomPhrase(), LOWER_FONT, LOWER_SIZE, 450)
    
    frame.show()

if __name__ == '__main__':
    makeImage()
