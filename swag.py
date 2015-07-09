import json #JSON Encoder and Decoder library
from datetime import datetime

## JSONmodule
#  This class controls file IO and stores entries in a map
class JSONmodule:

        ##The constructor
        #@param filename A file containg the entries in valud JSON
        # Loads the data from the json file into a dictionary
        def __init__(self, filename = "test"):
            self.updateMap(filename)

        ##Updates the map by reading values from the given file
        #@param filename
        def updateMap (self, filename = "test"):
            r = open (filename, 'r')
            self.entryMap = json.load(r)
            r.close()

        ##Writes the dictionary to the file specified
        def write (self, filename = "testout"):
            w = open (filename, 'w')
            json.dump(self.entryMap, w, indent=4)
            w.close

        ##Extracts Month from Unix timestamp in the format "May 2015"
        #@param timestamp The timestamp to be converted
        #@retval month A human-readable month value as a string
        def timestampToMonth (self, timestamp = 0):
            return datetime.fromtimestamp(timestamp).strftime('%B %Y')

        ##Returns an array of entries for the given month
        #@param month The month for which entries are requested
        #@retval entries The entries for the specified month as an array
        def getEntriesByMonth (self, month = "May 2015"):
            return self.entryMap[month]

        ##Inserts a new entry in the dictionary and writes the updated database to the given file
        #@param newEntry A tuple containing the timestamp and the text of the new entry
        #@param filename The name of the file where the database will be written after the update
        def addEntry (self, newEntry = (1425772844, "New Test Entry Text"), filename = "test"):
            month = self.timestampToMonth(newEntry[0])
            self.entryMap[month].append({"date": newEntry[0], "text":newEntry[1]})