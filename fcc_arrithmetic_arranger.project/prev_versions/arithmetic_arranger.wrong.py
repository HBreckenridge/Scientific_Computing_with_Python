def arithmetic_arranger(problems, wAnswers=False):
    formattedList = []
    wAnswers = wAnswers
    for i in problems:
        l1, l2 = i.split(" ")[0], i.split(" ")[1::]
        width = 1
        line2 = ('{a}'.format(a = width))
        sum = eval('{0}{1}{2}'.format(l1,*l2))
        
        print(line2)
        print(sum)
    
    return


#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
#["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]



        formattedList.append(line1+line2+spacer+line3)
    player = [0, 1, 2, 3]
    lines = [formattedList[i].splitlines() for i in player]
    for l in zip(*lines): 
        print(*l, '')