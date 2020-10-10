import constants
from lib.epd2in13_V2 import EPD, EPD_WIDTH, EPD_HEIGHT
from PIL import Image, ImageDraw, ImageFont

class DisplayManager:
    def __init__(self):
        self.epd = EPD()
        self.epd.init(self.epd.FULL_UPDATE)
        print("Clearing display ...")
        self.epd.Clear(0xFF)

    def printQuote(self, quote):
        # max 25 char per line
        count = 0
        lines_count = 0
        lines = []
        lines.append("")
        words = quote.split(" ")
        for word in words:
            if (count + len(word) <= 25):
                count = count + len(word)
                lines[lines_count] = lines[lines_count] + word + " "
            else:
                count = len(word)
                lines_count += 1
                lines.append(word + " ")

        font24 = ImageFont.truetype('/home/pi/CheesyQuotes/fonts/Peddana-Regular.ttf', 24)        
        image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame   
        draw = ImageDraw.Draw(image)

        for i, line in enumerate(lines):
            draw.text((10, 20*i), line, font = font24, fill = 0)

        self.epd.display(self.epd.getbuffer(image))