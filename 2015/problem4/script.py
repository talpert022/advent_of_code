import hashlib
import time

SECRET_KEY = 'iwrupvqb'

print((hashlib.md5('iwrupvqb9958218'.encode()).hexdigest()))

def get_append_num(key):
    num = 1
    md5_hash = ''
    while(md5_hash[0:6] != '000000'):
        num += 1
        md5_hash = hashlib.md5((key + str(num)).encode()).hexdigest()
    return num

start = time.time()
num = get_append_num(SECRET_KEY)
end = time.time()
print('Answer = ' + str(num))
print(f'Time to complete {(end-start)} s')