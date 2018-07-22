#3
l1=[3,6,6]
l2=[4,5,7]

f=[x for x in map(lambda a,b:a+b,l1,l2)]
print(f)

#2
l1=[1,3,5,10,12,15,18,20,21,20]

c=[x for x in filter(lambda a:True if a%3==0 and a%5==0 else False,l1)]
print(c)


#1
a=4
cube=(lambda a:a**3)(a)
print(cube)

#4
l1=[7,6,4]
l2=[2,3,5]

d={x for x in map(lambda a,b:(a,b**2) if a>b else(b,a**2),l1,l2)}
print(d)
