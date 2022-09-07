'''Show Current Time'''

import time

# Obtain current time
t = time.time()

# Total time in seconds (ts)
ts = int(t)

# Compute the current second (cs)
cs = ts % 60

# Compute Time in Minutes (tm)
tm = ts // 60

# Compute Current minutes (cm)
cm = tm % 60

# Compute time in Hours (tm)
th = tm // 60

# Current hour
ch = th % 24


print("Current time is", ch, ":", cm, ":", cs, "GMT")


# UNIX epoch is the date and time the UNIX system dates from which is 1st Jan 1970

# time.time() returns t (t - from above)

# Second from time.time() (Compute Second from above)
