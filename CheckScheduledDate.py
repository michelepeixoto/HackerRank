from datetime import datetime, timedelta, date

s = "2018-07-03 12:50"
scheduled = datetime(int(s[:4]), 
                    int(s[5:7]), 
                    int(s[8:10]), 
                    hour=int(s[11:13]), 
                    minute=int(s[14:16]))
current = datetime.now()
diff = str(current - scheduled)
if diff[0] == "-":
    print("False") #exit code 1
else:
    print("True") #exit code 0