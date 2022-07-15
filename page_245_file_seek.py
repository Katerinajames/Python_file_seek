
f=open('seek.txt','w')
f.write("1,2,3,5")

f.seek(5)
f.write('Hello, World!')

f.close()
print("-------------------------------")
f=open('seek.txt','r')
h=f.read()

print(h)

f.close()
