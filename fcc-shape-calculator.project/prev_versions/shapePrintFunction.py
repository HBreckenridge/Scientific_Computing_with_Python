def print_rectangle(x, y):

    return


#print_rectangle(5,6)

#for align, text in zip('<^>', ['left', 'center', 'right']):
#     '{0:{fill}{align}16}'.format(text, fill=align, align=align)

y=6#len(returnFList)
shape=''
char = "*"
x = 6
for i in range(y):
    if i < y-1:
        ystr = (""""""+char*x+"""\n""")
    elif i >= y-1:
        ystr = (""""""+char*x+"""""")
    shape+=str("""{0}""").format(ystr)
print(shape)