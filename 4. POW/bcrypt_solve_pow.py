import bcrypt
import timeit
from hashlib import sha256

x=8
y=0 # We don't know what y should be yet

while bcrypt.hashpw(f'{x*y}'.encode("utf-8"),salt=bcrypt.gensalt()).decode("utf-8")[-1]!="C":
    y+=1
    if y%10==0:
        print(bcrypt.hashpw(f'{x*y}'.encode("utf-8"),salt=bcrypt.gensalt()).decode("utf-8"))
        print(y)

print(f'solution is y = {y}',bcrypt.hashpw(f'{x*y}'.encode("utf-8"),salt=bcrypt.gensalt()).decode("utf-8"))

# import_module='''
# import timeit
# from hashlib import sha256
# '''
# timer_var='''
# x=5
# y=0
# while sha256(f'{x*y}'.encode()).hexdigest()[-1]!="0":
#     y+=1
# '''
#print(timeit.timeit(stmt=timer_var,setup=import_module))
