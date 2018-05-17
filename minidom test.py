from xml.dom.minidom import parse, parseString
dom1= parse("example xml.txt")
print(dom1.toxml())
print("")
for node in dom1.getElementsByTagName('CD'):
    print(node.getAttribute("name"))
