import time, threading
import constants
from quotes import QuotesManager
from display import DisplayManager

# ps -ef | grep python
# sudo kill -9 [pid]
# pip freeze > requirements.txt
# pip install -r requirements.txt

class Main:
    def __init__(self):
        self._quotesManager = QuotesManager()
        self._displayManager = DisplayManager()

    def main(self):
        try:
            while (True):
                quote = self.retrieve_quote()
                self.display_quote(quote)
                time.sleep(constants.REFRESH_TIME_SEC)
        except Exception as e: 
            print("Error: " + e)
    
    def retrieve_quote(self):
        quote = self._quotesManager.GetRandomQuote(constants.INSPIRATIONAL)
        print(quote)
        return quote        
    
    def display_quote(self, quote):
        self._displayManager.printQuote(quote)

    

main = Main()
main.main()