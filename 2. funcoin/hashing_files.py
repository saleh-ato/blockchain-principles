from hashlib import sha256

file=open("img/my_image.jpg","rb")
hash= sha256(file.read()).hexdigest()
file.close()
print("hash is {}".format(hash))
