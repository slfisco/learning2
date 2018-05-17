#more regular expressions
import re
#TWO WAYS

#m = re.search("the", "an eagle the")
#if m:
#    print(m.group(0))

#creates regular expression object. this one is kind of pointless
p = re.compile("the")
r = p.search("an eagle the")
if r:
    print(r.group(0))
