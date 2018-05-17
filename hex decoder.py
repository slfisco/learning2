#hexadecimal to base64 encoder
#just kidding this already exists. boo
file = open("EOS results template3.csv", 'rb')
import codecs
#str = "616d6974"
#encoded = codecs.encode(codecs.decode(str, "hex"),"base64").decode()
#print(encoded)

import hashlib
#sha1_hash = sha1("616d6974")
#print(sha1_hash)
#sha1 = hashlib.sha1(b"test").hexdigest()

sha1 = hashlib.sha1(file.read()).hexdigest()
print(sha1)
encoded = codecs.encode(codecs.decode(sha1, "hex"),"base64").decode()
print(encoded)
