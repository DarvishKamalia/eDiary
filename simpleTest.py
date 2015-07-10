import simpleJSONmodule as simple
from datetime import datetime

test = simple.JSONmodule("simple.json")
test.addEntry((12342315232, "swag swag swag"))
test.removeEntry (12342315232)
print (type(datetime.now()))
