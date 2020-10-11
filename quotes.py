import constants
import requests
import json
import os
import random

class QuotesManager:
    def __init__(self):
        self._script_dir = os.path.dirname(os.path.realpath('__file__'))
        self.quoteTypeAction = {
            constants.OFFLINE: self.__getOfflineQuote,
            constants.INSPIRATIONAL: self.__getInspirationalQuote,         
            constants.DESIGN: self.__getDesignQuote,
        }

    def GetRandomQuote(self, type=constants.INSPIRATIONAL):
        quote=""
        try:
            quote = self.quoteTypeAction[type]()
            if (type != constants.OFFLINE):
                self.__log_quote(quote)
        except requests.ConnectionError as ex:
            print("Device is not connected, using offline quote")
            quote = self.quoteTypeAction[constants.OFFLINE]()
        except Exception as ex:
            print("Unknown error, using offline quote")
            quote = self.quoteTypeAction[constants.OFFLINE]()
        return quote

    def __getInspirationalQuote(self):        
        r = requests.get(constants.URL_INSPIRATIONAL) 
        quote_details = json.loads(r.text)           
        return quote_details[0]['q']

    def __getDesignQuote(self):
        r = requests.get(constants.URL_DESIGN) 
        quote_details = json.loads(r.text)           
        return quote_details[0]["content"]["rendered"].replace("<p>", "").replace("</p>", "")

    def __getOfflineQuote(self):        
        return random.choice(list(open(self._script_dir + "/files/offline_quotes.txt"))).strip('\n')

    def __log_quote(self, quote):
        f = open(self._script_dir + "/files/offline_quotes.txt", "a")
        f.write("%s\n" % (quote))
        f.close()


    


