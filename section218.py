''' Current Time '''

# Revise listing27
import time
t = time.time()

# Total time in Sec
ts = int(t)
# Compute current Seconds
cs = ts % 60
# Compute time in minutes
tm = ts // 60
# Compute current minutes
cm = tm % 60
# Compute time in hours
th = tm // 60
# Compute time in hours
ch = th % 24

# Prompt the user to enter the time zone
timeZone = eval(input("Enter time zone offset to GMT: "))

# Display the time in special field time zone
print(f'The current time is {ch + timeZone}:{cm}:{cs}')