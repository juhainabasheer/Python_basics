x,y=78,78

print(id(x))
print(id(y))
print(x is y)

l=[56,"Python",12]
j=[56,"Python",12]
print(id(l))
print(id(j))
print(l is j)

l=[56,"Python",12]
j=l
print(id(l))
print(id(j))


# a=20
# b=20
# print(a==b)
# print(a is b)
#
# print(id(a))
# print(id(b))

ab=tuple(range(1,100))
cd=tuple(range(1,100))
print(ab is cd)
# cd=ab
# print(id(ab))
# print(id(cd))
#
# print(ab==cd)
# print(ab is cd)