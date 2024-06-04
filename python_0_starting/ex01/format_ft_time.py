import time
from datetime import datetime


ts = time.time()
print("Seconds since January 1, 1970:", "{:,.4f}".format(ts), "or",
      "{:.2e}".format(ts), "in scientific notation")
print(datetime.today().strftime("%b %d %Y"))
