import datetime
from datetime import date
import time
d0 = date(1889,4,20)
now = datetime.datetime.now()
d1 = date(now.year,now.month,now.day)
delta = d1 - d0
