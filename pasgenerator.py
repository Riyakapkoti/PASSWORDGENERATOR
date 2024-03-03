import random
import string


pass_len=8
# charvalues = string.ascii_letters + string.digits + string.punctuation
charvalues = string.printable

# password = ""
# for i in range(pass_len):
#     password += random.choice(charvalues)

# list comprehension
password="".join([random.choice(charvalues) for i in range(pass_len)])
print(password)
    
print("your random password is" , password)