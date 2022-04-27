import hashlib
# Hash functions expect bytes as input: the encode() method turns strings to bytes
input_bytes=b"backpack"
output=hashlib.sha256(input_bytes)
output_kecc=hashlib.keccak256(input_bytes)
# We use hexdigest() to convert bytes to hex because it's easier to read
print(output)
print(output.hexdigest())
print(output_kecc.hexdigest())
