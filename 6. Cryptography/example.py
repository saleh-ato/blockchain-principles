from hashlib import sha256

message="Hello Bob, Let's meet at the Kruger National Park on 2020-12-12 at 1pm."
hash_message = sha256(("p@55w0rd" + message).encode()).hexdigest()
print(hash_message)