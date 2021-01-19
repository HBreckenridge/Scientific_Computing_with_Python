descs = ['automobile', 'clothing', 'food']
totals = [2000, 5000, 3000]
totalSales = {}
for i in range(len(descs)):
    totalSales[descs[i]]=totals[i]

def CascadePrint(totalSalesDict):
    sortedTotalSalesDict = dict(sorted(totalSalesDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True))
    totalSalesDict = sortedTotalSalesDict
    total = 0
    salesPercentages = {}
    pFormattedLines = []
    pTotal = 10
    cascadedLabels = []
    cascadedLabelBlanks = []
    lines = [(i*10) for i in range(1,pTotal+1)]
    lines.sort(reverse = True)
    lines = [str(i)+"|" for i in lines]
    pFormattedLines.append(lines)
    descLengths =[]
    for descriptions in totalSalesDict:
        salesTotal = totalSalesDict[descriptions]
        total += salesTotal
        descLengths.append(len(str(descriptions)))
    cascadingLimit = (max(descLengths))
    for i in range(cascadingLimit):
        cascadedLabelBlanks.append("   ")
    cascadedLabels.append(cascadedLabelBlanks)
    for i in totalSalesDict:
        salesTotal = totalSalesDict[i]
        salesPercentages[i] = int((salesTotal/total)*10)
        pBudget = salesPercentages[i]
        pSales = list(" "*(pTotal-pBudget))+list("o"*pBudget)
        pFormattedLines.append(pSales)
        cascadingLetters =[i for i in str(i)]
        cascadingLetters = cascadingLetters+list(" "*(cascadingLimit-len(cascadingLetters)))
        cascadedLabels.append(cascadingLetters)
    print("Percentage spent by category")
    percentagesPrint = True
    ###CascadingPercentages
    if percentagesPrint == True:
        for yCoord in range(len(pFormattedLines[0])):
            for xCoord in range(len(pFormattedLines)):
                if xCoord == 0:
                    space = len(max(pFormattedLines[xCoord]))+1
                elif xCoord == 1:
                    space = 1
                elif xCoord >1:
                    space = 2
                print('{0:>{width}}'.format(pFormattedLines[xCoord][yCoord], width=space), end=' ')
            print()
    ###BreakLine
    print(4*" "+"--"+(4*(len(totalSalesDict)-1))*"-")
    ###Reverse Cascading Titles
    if percentagesPrint == True:
        for yCoord in range(len(cascadedLabels[0])):
            for xCoord in range(len(cascadedLabels)):
                if xCoord == 0:
                    space = len(max(cascadedLabels[xCoord]))+1
                elif xCoord == 1:
                    space = 1
                elif xCoord >1:
                    space = 2
                print('{0:>{width}}'.format(cascadedLabels[xCoord][yCoord], width=space), end=' ')
            print()

CascadePrint(totalSales)