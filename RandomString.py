import random
import string

random = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10000)])
print(random.upper())
