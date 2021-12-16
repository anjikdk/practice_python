import sys

print(sys.version)
print(sys.executable)
print(sys.version_info)

lst = ["abc","xyz","hyd","blr","apple"]

print(len(lst))
if "hyd" in lst:
    print("hyd is there in the above list")

y = {"ch" : "chennai","atp":"anantapur"}

#x.append(y)

print(lst)
print(y)

def displayListValues(thisList):
    print("for loop ====================")
    for i in thisList:
        print(i)

    print("for loop with index ====================")
    for i in range(len(thisList)):
        print(thisList[i])

    print("while loop ===============")
    i = 0
    while i < len(thisList):
        print(thisList[i])
        i = i+1

    print("list comprehenion ====================")
    [print(i) for i in thisList]

displayListValues(lst)