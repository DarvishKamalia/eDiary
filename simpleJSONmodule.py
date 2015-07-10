import json #JSON Encoder and Decoder library
from datetime import datetime

## JSONmodule
#  This class controls file IO and stores entries in a list
class JSONmodule:

        ##The constructor
        #@param filename A file containg the entries in valud JSON
        # Loads the data from the json file into a list of maps
        def __init__(self, filename = "test"):
            self.updateList(filename)

        ##Updates the list by reading values from the given file
        #@param filename The file containing the list in valid JSON format
        def updateList (self, filename = "test"):
            r = open (filename, 'r')
            self.entryList = json.load(r)
            r.close()

        ##Writes the list to the file specified
        #@param filename The name of the output file
        def write (self, filename = "testout"):
            w = open (filename, 'w')
            json.dump(self.entryList, w, indent=4)
            w.close()

        ##Extracts Month from Unix timestamp in the format "May 2015"
        #@param timestamp The timestamp to be converted
        #@retval month A human-readable month value as a string
        def timestampToMonth (self, timestamp = 0):
            return datetime.fromtimestamp(timestamp).strftime('%B %Y')

        ##Returns an array of entries for the given month
        #@param month The month for which entries are requested
        #@retval searchResults The entries for the specified month as an array
        def getEntriesByMonth (self, month = "May 2015"):
            searchResults = []
            for entry in self.entryList:
                entryMonth = self.timestampToMonth(entry["date"])
                if (month == entryMonth):
                    searchResults.append(entry)
            return searchResults

        ##Searches for all entries containing the given string
        #@param toSearch The string to search for
        #@retval searchResults A list of tuples, each containing a timestamp and the text of the entry
        def getEntriesByKeywords (self, keyword = "swag"):
            searchResults = []
            for entry in self.entryList:
                if keyword in entry["text"] :
                    searchResults.append(entry)
            return searchResults 

        ##Inserts a new entry in the list and writes the updated list to the given file
        #@param newEntry A tuple containing the timestamp and the text of the new entry
        #@param filename The name of the file where the list will be written after the update
        def addEntry (self, newEntry, filename = "testout"):
            self.entryList.append ({"date": newEntry[0], "text": newEntry[1]})
            self.write(filename)

        ##Deletes the entry with the given timestamp from the list
        #@param toDelete The timestamp of the entry to be deleted
        def removeEntry (self, toDelete, filename = "testafterdelete"):
            for entry in self.entryList:
                entryTimestamp = entry["date"]
                if (entryTimestamp == toDelete):
                    self.entryList.remove(entry)
            self.write (filename)
