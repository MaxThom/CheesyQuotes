import time, threading, os, datetime
import constants
from quotes import QuotesManager
from display import DisplayManager

# ps -ef | grep python
# sudo kill -9 [pid]
# pip freeze > requirements.txt
# pip install -r requirements.txt

class Main:
    def __init__(self):
        self._script_dir = os.path.dirname(os.path.realpath('__file__'))
        self._quotesManager = QuotesManager()
        self._displayManager = DisplayManager()

    def main(self):
        try:
            while (True):
                quote = self.retrieve_quote()
                self.display_quote(quote)
                time.sleep(constants.REFRESH_TIME_SEC)
        except Exception as e: 
            self.log_message(e)
    
    def retrieve_quote(self):
        quote = self._quotesManager.GetRandomQuote(constants.INSPIRATIONAL)
        print(quote)
        return quote        
    
    def display_quote(self, quote):
        self._displayManager.printQuote(quote)

    def log_message(self, msg):
        print(msg)
        f = open(self._script_dir + "/files/logs.txt", "a")
        f.write("[%s] %s.\n" % (datetime.datetime.now(), msg))
        f.close()    

main = Main()
main.main()