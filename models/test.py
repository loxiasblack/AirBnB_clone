#!/usr/bin/python3
import uuid
from datetime import datetime
myuuid = uuid.uuid4()
mydate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("My UUID is: " + str(myuuid))
print("and is born at: " + mydate)
