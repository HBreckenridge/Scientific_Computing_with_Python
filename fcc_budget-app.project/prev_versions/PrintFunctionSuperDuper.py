descs = ['automobile', 'clothing', 'food']
amounts = [2000, 5000, 3000]

def SuperDuperPrintFunction(y, x):
    xWidth = range((x))
    pFormattedLines = []
    pTotal = 10
    lines = [(i*10) for i in range(1,pTotal+1)]
    lines.sort(reverse = True)
    lines = [str(i)+"|" for i in lines]
    pFormattedLines.append(lines)
    pBudgets = [6,8,2]
    pBudgetLabels = ["food", "clothing", "auto"]
    for pBudget in pBudgets:
        #pBudget = 6
        pSales = list(" "*(pTotal-pBudget))+list("o"*pBudget)

    
    
        pFormattedLines.append(pSales)
    
    
    
    nY=y
    fListA = []
    newFormattedList = []
    lines = [fList[i].splitlines() for i in range(nY)]
    yString=''

    for i in range(nY):
        if i < nY-1:
            ystr = ("""{"""+str(i)+"""}\n""")
        elif i >= nY-1:
            ystr = ("""{"""+str(i)+"""}""")
        yString+=str("""{0}""").format(ystr)
    #print(yString)
    
    #xString=""
    #nX = x
    #for i in range(nX):
    #    xstr = ("""{"""+str(i)+"""}""")
    #    #x = ("""{"""+str(i)+''':'''+str(maxLengths[i]+6)+"""}""")
    #    xString+=str("""{0}""").format(xstr)
    #print(xString)

    #for c in range(y):
        #cX = xString.format(*lines)
        #print(cX)
        #cc = yString.format(cX)
    #print(cc)
    percentagesPrint = True
    if percentagesPrint == True:
        for yCoord in range(len(pFormattedLines[0])):
            for xCoord in range(len(pFormattedLines)):
                if xCoord == 0:
                    space = len(max(pFormattedLines[xCoord]))+1
                elif xCoord >=1:
                    space = 1
                print('{0:>{width}}'.format(pFormattedLines[xCoord][yCoord], width=space), end=' ')
            print()
    
SuperDuperPrintFunction(10,4)