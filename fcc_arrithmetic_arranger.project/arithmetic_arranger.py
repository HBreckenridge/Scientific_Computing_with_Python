

def NumProblemCheck(A, epass, message=None):
    if len(A) > 5:
        epass = False 
        message = str("Too many problems.")
        return message
    else:
        return epass

def OpCheck(A,epass, message=None):

    for i in A:
        I = i.split(" ")
        x = I[1]
        epass = (True if x == str("+") or
            x == str("-") else False)
        if epass == False:
            epass = False
            message = str("Operator must be '+' or '-'.")
            return message
        else:
            return epass

def CharCheck(A, epass, message=None):
    charList = []
    for i in A:
        I = i.split(" ")
        strings = (str(I[0])+str(I[2]))
        charList.append(strings)

    chrString = ''.join(charList)
    epass = chrString.isdigit()

    if not chrString.isdigit():
        epass = False
        message = str("Numbers must only contain digits.")
        return message
    else:
        return epass



def OperandLengthCheck(A, epass, message=None):

    for i in A:

        for x in i.split(" ")[0::2]:
            z = len(x)
            epass = (True if z <=4  else False)
            if epass == False:
                epass = False
                message = str("Numbers cannot be more than four digits.")
                return message
    return True




def errorCheck(toCheck):
    eMessage = ''
    ePass = True
    message= NumProblemCheck(toCheck,ePass)
    if message != True:
        ePass = "Error: "+message
        return ePass
    else:
        pass
    message= OpCheck(toCheck,ePass)
    if message != True:
        ePass = "Error: "+message
        return ePass
    else:
        pass
    message= CharCheck(toCheck,ePass)
    if message != True:
        ePass = "Error: "+message
        return ePass
    else:
        pass
    message= OperandLengthCheck(toCheck,ePass)
    if message != True:
        ePass = "Error: "+message
        return ePass
    else:
        return True



def arithmetic_arranger(problems, wAnswers=False):

    eMessage = errorCheck(problems)
    #print(eMessage)
    if eMessage != True:
        #print(eMessage)
        return eMessage
    else:
        pass


    formattedList = []
    wAnswers = wAnswers
    align = ">"
    width = 6
    maxLengths =[]
    for i in problems:
        x = eval('{0}{1}{2}'.format(*i.split()+[' ']))
        maxL = (max([len(i.split(" ")[0]),len(i.split(" ")[2])]))
        maxLengths.append(maxL)
        width = (len(str(x)))
        width2 = (maxL)
        totalW = maxL+2
        if wAnswers == True:

            line1 = ('''{0:{align}{width}}\n'''.format(*i.split(), width=maxL+2, align=align, base=10))
            line2 = ('''{0:<2}{1:>{width}}\n'''.format(*i.split()[1:], width=(maxL+2)-2,widthR=len(i.split()[2]), align=align, base=10))
            spacer = '-'*(maxL+2)
            line3 = ('''\n{0:{align}{width}}'''.format(x, width=(maxL+2), align=align, base=10))
            formattedList.append(line1+line2+spacer+line3)
        else:
            line1 = ('''{0:{align}{width}}\n'''.format(*i.split(), width=maxL+2, align=align, base=10))
            line2 = ('''{0:<2}{1:{align}{width}}\n'''.format(*i.split()[1:], width=(maxL+2)-2,widthR=len(i.split()[2]), align=align, base=10))
            spacer = '-'*(maxL+2)
            #line3 = None
            formattedList.append(line1+line2+spacer)
    

    player = range(len(problems))
    #print(len(problems))
    lines = [formattedList[i].splitlines() for i in player]
    newFormattedList = []
 
    s=''
    n=len(problems)
    for i in range(n):
        x = ("""{"""+str(i)+''':'''+str(maxLengths[i]+6)+"""}""")
        s+=str("""{0}""").format(x)
    for l in zip(*lines):
        
        zz = s.format(*l).rstrip()
        newFormattedList.append(zz)
    #print(zz)


    if wAnswers == True:
        
        return '{0}\n{1}\n{2}\n{3}'.format(*newFormattedList)
    if wAnswers != True :
        return '{0}\n{1}\n{2}'.format(*newFormattedList)

actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
print(actual)
    
