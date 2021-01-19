def arithmetic_arranger(problems, wAnswers=False):
    formattedList = []
    wAnswers = wAnswers
    align = ">"
    for i in problems:
        x = eval('{0}{1}{2}'.format(*i.split()+[' ']))

        if wAnswers == True:
            y = ('''\n{0:{align}{width}}\n{1:<}{2:{align}{width}}\n{3:{align}{width}}'''.format(*i.split(), x, width=6, align=align, base=10))
        else:
            y = ('''\n{0:>5}\n{1:}{2:>4}\n-----'''.format(*i.split(' ')))
        formattedList.append((y))
    ll = []

    player = [0, 1, 2, 3]
    lines = [formattedList[i].splitlines() for i in player]
    for l in zip(*lines): 
        print(*l, '     ')
    return ''


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
#["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]