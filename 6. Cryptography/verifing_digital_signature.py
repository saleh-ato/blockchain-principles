import nacl.encoding
import nacl.signing

# From the above example...
bobs_public_key = b'1bda5e01715006290fd571da5a3ff590e686b91bdc3b391a6e7d5f4a5cb841b6'


# We generate the verify_key
verify_key = nacl.signing.VerifyKey(bobs_public_key,encoder=nacl.encoding.HexEncoder)
signed_message = b'\x03\x87\xec\x88\xe9bnJC\\v\x8b\xd7\xc8\xff\xf5\x9a\xd2\x06r\x02\x18\xb4n\xc2\xe46\x99\xa0\xd3<\xc1X\x08\xb9\x009\xeb|\xff~\x99\xc7\x89\x0b"YX\x93)\xae\t\x16V\x9c\x9a\x118\x17\xcfFS\x8f\x02Send $37 to Alice'

# Now we attempt to verify the message
# Any invalidation will result in an Exception being thrown
if verify_key.verify(signed_message):
    print("True")
    print(verify_key.verify(signed_message))

'''
bobs_public_key = b'e7ff10ede8a691b982516059a0627d369504e36
33e0297e28ec5fc71994577d3'
7
8 # We generate the verify_key
9 verify_key = nacl.signing.VerifyKey(bobs_public_key,
encoder=nacl.encoding.HexEncoder)
10
11 signed_message = b'\x9fq\x02\xe1o\xb8y2\xc7\xe7@9$\xc4[\
xb2\xa4\xe1+97.>\r\xca GG\x8a Y\x86\xc3\xfe\xb9W{\xc4\x9c\
x87\x00(\x1d\xe9}j\xe4\xed\xd2\x0b\xcb\x88\x87 J\xecy\
x04GQH\xea\xcc\xc2\xe7\x03Send $37 to Alice'
'''