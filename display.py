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

        font_size, char_per_line, max_line = self.__getFontSize(len(quote))        
        print("   font_size:", font_size, "char_line:", char_per_line, "max_line:", max_line, "quote_size:", len(quote))
        if (font_size == None):
            return False

        lines = self.__splitQuoteInLines(quote, char_per_line)        
        self.__printQuote(font_size, max_line, char_per_line, lines)
        return True        

    def __splitQuoteInLines(self, quote, char_per_line):
        # max 25 char per line
        count = 0
        lines_count = 0
        lines = []
        lines.append("")
        words = quote.split(" ")
        for word in words:
            if (count + len(word) <= char_per_line):
                count = count + len(word) + 1
                lines[lines_count] = lines[lines_count] + word + " "
            else:
                count = len(word) + 1
                lines_count += 1
                lines.append(word + " ")
        return lines

    def __getFontSize(self, quote_length):
        if (quote_length <= 210 and quote_length > 180):
            return 12, 35, 6
        elif (quote_length <= 180 and quote_length > 144):
            return 14, 30, 6
        elif (quote_length <= 144 and quote_length > 132):
            return 16, 24, 6
        elif (quote_length <= 132 and quote_length > 100):
            return 18, 22, 6
        elif (quote_length <= 100 and quote_length > 90):
            return 20, 20, 5
        elif (quote_length <= 90 and quote_length > 70):
            return 22, 18, 5
        elif (quote_length <= 70):
            return 24, 17, 5
        return None, None, None
        #font -> char per lines*number of lines = total possible chars
        #12 -> 35*6=210
        #14 -> 30*6=180
        #16 -> 24*6=144
        #18 -> 22*6=132
        #20 -> 20*5=100
        #22 -> 18*5=90
        #24 -> 17*5=85

    def __printQuote(self, font_size, max_line, char_per_line, lines):
        X_MARGIN = 5
        Y_MARGIN = 5
        Y_INTERLIGN = 20

        font24 = ImageFont.truetype('/home/pi/CheesyQuotes/fonts/SourceCodePro-SemiBoldItalic.ttf', font_size)
        image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(image)

        line_skip = (max_line - len(lines)) / 2
        for i, line in enumerate(lines):
            x = X_MARGIN
            y = Y_INTERLIGN * i + line_skip * Y_INTERLIGN + Y_MARGIN
            char_skip = int((char_per_line - len(line)) / 2)
            line = " " * char_skip + line
            draw.text((x, y), line, font = font24, fill = 0)

        self.epd.display(self.epd.getbuffer(image))
