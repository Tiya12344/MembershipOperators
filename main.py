#identity  operator
maggi = 6
tanghulu = 6
if maggi is tanghulu:
    print("the identity of maggi and tanghulu is the same")
else:
    print("the identity of maggi and tanghulu is not the same")


ciao = 5
salve = 60
if ciao is not salve:
    print("the identity of ciao and salve is not the same")
else:
    print("the identity of ciao and salve is  the same")

#membership operators

name = "Liya"
X = {1 : "Tea", 2: 'coffee'}

print("T" in name)
print( 3 in X)
print("Tea" in X)
print("i" not in name)
