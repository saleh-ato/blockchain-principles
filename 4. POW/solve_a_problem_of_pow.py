import timeit
from hashlib import sha256

x=5
y=0 # We don't know what y should be yet

while sha256(f'{x*y}'.encode()).hexdigest()[-1]!="0":
    y+=1
    if y%100000==0:
        print(y)

print(f'solution is y = {y}',sha256(f'{x*y}'.encode()).hexdigest())

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
