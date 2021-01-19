width = 5
for num in range(5,12):
    for base in 'dXob':
        print ('{0:{width}{base}}'.format(num, base=base, width=width),end =' ')
    print()
s = ""
n = 3


for i in range(n):
    x = """{"""+str(i)+"""}"""
    s+=str("""     {0}""").format(x)
print(s)