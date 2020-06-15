import hashlib
code = input('code : ')
print('license : '+hashlib.md5(code.encode('utf-8')).hexdigest())
input('')
