def arithmetic_arranger(problems, wAnswers=False):
    mapp = [x.split(" ") for x in problems]

    width = 6
    align = ">"

    for x in range(len(problems)):
        b = problems[x].split(" ")
        
        y ='{0[0]:{align}{width}}\n'.format(b[x], width=width, align = align)
        z ='{0[1]:{align}{width}}{0[2]:>{width}}\n'.format(b, width=3, align = "<")
        w = '-'*6
        print(y,z,w)

    for c in range(1): 
        for x in range(len(problems)):
            b = [''.join(problems[x].split(" ")[0]), ''.join(problems[x].split()[1:])]
            print('{0:{align}{width}}'.format(b[c], width=width, align=align),  end = ' ')

            
        print()


    return #str(y+z+w)


#print(arithmetic_arranger([ "32 + 6in98", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

