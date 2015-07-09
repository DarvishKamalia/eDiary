import json #JSON Encoder and Decoder library

## JSONmodule
#  This class controls file IO and stores entries in a map
class JSONmodule:

        ##The constructor
        #@param filename A file containg the entries in valud JSON
        # Loads the data from the json file into a dictionary
        def __init__(self, filename = "test"):
            updateMap (filename)

        ##Updates the map by reading values from the given file
        #@param filename
        def updateMap (filename = "test"):
            r = open (filename, 'r')
            self.entryMap = json.load(r)
            r.close()

        ##Writes the dictionary to the file specified
        def write (filename = "testout"):
            w = open (filename, 'w')
            json.load(self.entryMap, r)
            w.close

        ##Returns an array of entries for the given month
        #@param month The month for which entries are requested
        #@retval entries The entries for the specified month as an array
        def getEntriesByMonth (month = "May 2015"):
            return self.entryMap[month]

        ##Inserts a new entry in the dictionary and writes the updated database to the given file
        #@param newEntry A tuple containing the timestamp and the text of the new entry
        #@param filename The name of the file where the database will be written after the update
        def addEntry (newEntry = (""))
