import sys

from lib.epd2in13_V2 import EPD, EPD_WIDTH, EPD_HEIGHT
from PIL import Image, ImageDraw, ImageFont

epd = EPD() # get the display
epd.init(epd.FULL_UPDATE)           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear(0xFF)      # clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (EPD_HEIGHT, EPD_WIDTH), 255)
    HRedImage = Image.new('1', (EPD_HEIGHT, EPD_WIDTH), 255)
    
    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 30) # Create our font, passing in the font file and font size
    
    draw.text((25, 65), string, font = font, fill = 0)
    
    epd.display(epd.getbuffer(HBlackImage))

def example():
    # Drawing on the image
    font15 = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 15)
    font24 = ImageFont.truetype('/home/pi/CheesyQuotes/fonts/Peddana-Regular.ttf', 24)
    

    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    draw.rectangle([(0,0),(50,50)],outline = 0)
    draw.rectangle([(55,0),(100,50)],fill = 0)
    draw.line([(0,0),(50,50)], fill = 0,width = 1)
    draw.line([(0,50),(50,0)], fill = 0,width = 1)
    draw.chord((10, 60, 50, 100), 0, 360, fill = 0)
    draw.ellipse((55, 60, 95, 100), outline = 0)
    draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
    draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
    draw.polygon([(110,0),(110,50),(150,25)],outline = 0)
    draw.polygon([(190,0),(190,50),(150,25)],fill = 0)
    draw.text((120, 60), 'Catherine', font = font15, fill = 0)
    draw.text((110, 90), 'Maxime Thomassin', font = font24, fill = 0)
    epd.display(epd.getbuffer(image))
    
#printToDisplay("Hello, Catherine & Maxime!")    
example()