def arithmetic_arranger(problems, wAnswers=False):
    formattedList = []
    wAnswers = wAnswers
    align = ">"
    width = 6
    for i in problems:
        x = eval('{0}{1}{2}'.format(*i.split()+[' ']))

        width = (len(str(x))+1)
        width2 = (len(('{1}'.format(*i.split()+[' ']))))
        if wAnswers == True:
            line1 = ('''{0:{align}{width}}\n'''.format(*i.split(), width=width+1, align=align, base=10))
            line2 = ('''{0:<{widthR}}{1:{align}{width}}\n'''.format(*i.split()[1:], width=width,widthR=width2, align=align, base=10))
            spacer = '-'*(width+1)
            line3 = ('''\n{0:{align}{width}}'''.format(x, width=width+1, align=align, base=10))
            formattedList.append(line1+line2+spacer+line3)
        else:
            line1 = ('''{0:{align}{width}}\n'''.format(*i.split(), width=width+1, align=align, base=10))
            line2 = ('''{0:<{widthR}}{1:{align}{width}}\n'''.format(*i.split()[1:], width=width,widthR=width2, align=align, base=10))
            spacer = '-'*(width+1)
            #line3 = None
            formattedList.append(line1+line2+spacer)
    

    player = [0, 1, 2, 3]
    lines = [formattedList[i].splitlines() for i in player]
    newFormattedList = []
    for l in zip(*lines):        
        zz = '{0}  {1}  {2}  {3}'.format(*l)
        newFormattedList.append(zz)
    if wAnswers == True:
        return '{0}\n{1}\n{2}\n{3}'.format(*newFormattedList)
    if wAnswers == False:
        return '{0}\n{1}\n{2}'.format(*newFormattedList)


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
#["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]