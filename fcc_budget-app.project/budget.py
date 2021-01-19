# class for categories
from math import ceil
class Category:
    ledger = []
    def __init__(self, budget_category):
        self.ledger = []
        self.budget_category = budget_category
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount" : amount, "description":description})
        return

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) != True:
            return False
        else:
            self.ledger.append({"amount" : (-1)*amount, "description":description})
            return True

    def get_balance(self):
        total = 0
        for i in self.ledger:
            transactions = (i['amount'])
            total += transactions
        return total

    def transfer(self, amount, send_to_category):
        if self.check_funds(amount) != True:
            return False
        else:
            self.withdraw(amount, "Transfer to "+str(send_to_category.budget_category))
            send_to_category.deposit(amount, "Transfer from "+str(self.budget_category))
            return True

    def check_funds(self, amount):
        total = 0
        for i in self.ledger:
            transactions = (i['amount'])
            total += transactions
        if total >= amount:
            return True
        else:
            return False

    def get_total_withdraws(self):
        ledger = self.ledger
        spendingTotal = 0
        for i in ledger:
            if i['amount']<0:
        withdrawTotal = round(spendingTotal,2)
        return withdrawTotal

    def __str__(self):
        fListA = []
        fListA.append(category_title_line)
                spendingTotal += i['amount']
        lineLengths = []
        total = self.get_balance()
        category_title_line = "{0:{base}{align}{width}}".format(str(self.budget_category), width=30, align ="^", base = "*")
        lineLengths.append(len(category_title_line))
        for i in self.ledger:
            description = ''.join([i for i in i['description']])[:23]
            amount = ''.join([i for i in '%.2f' % (i['amount'])])[:7]
            category_title_line = "{0:<{width1}}{1:>{width2}}".format( description, amount, width1=23,width2=7, align ="^", base = "*")
            lineLengths.append(len(category_title_line))
            fListA.append(category_title_line.rstrip())
        lineLengths.append(len("Total: "+str(total)))
        totalLine = ("Total: "+str(total))
        fListA.append(totalLine)
        nY=len(fListA)
        yString=''
        for i in range(nY):
            if i < nY-1:
                ystr = ("""{"""+str(i)+"""}\n""")
            elif i >= nY-1:
                ystr = ("""{"""+str(i)+"""}""")
            yString+=str("""{0}""").format(ystr)
        ReturnString = yString.format(*fListA)
        return ReturnString 





def create_spend_chart(categories):
    totalSalesDict = {}
    for i in categories:
        totalSalesDict[i.budget_category]=i.get_total_withdraws()
    total = 0
    salesPercentages = {}
    pFormattedLines = []
    pTotal = 11
    cascadedLabels = []
    cascadedLabelBlanks = []
    fHorizontalLines = []
    returnFList = []
    rfListPercentages = []
    rfListLabels = []
    lines = [(i*10) for i in range(0,pTotal)]
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
        salesPercentage = (salesTotal/total)*10
        salesPercentages[i] = int(ceil(salesPercentage))
        pBudget = salesPercentages[i]
        pSales = list(" "*(pTotal-pBudget))+list("o"*pBudget)
        pFormattedLines.append(pSales)
        cascadingLetters =[i for i in str(i)]
        cascadingLetters = cascadingLetters+list(" "*(cascadingLimit-len(cascadingLetters)))
        cascadedLabels.append(cascadingLetters)
    headerLine = ("Percentage spent by category")
    ###CascadingPercentages
    for yCoord in range(len(pFormattedLines[0])):
        for xCoord in range(len(pFormattedLines)):
            if xCoord == 0:
                space = len(max(pFormattedLines[xCoord]))+1
            elif xCoord == 1:
                space = 1
            elif xCoord >1:
                space = 2
            fYLine = '{0:>{width}}'.format(pFormattedLines[xCoord][yCoord], width=space)
            fXYLine = fYLine
            rfListPercentages.append(fXYLine)

    breakLine = (4*" "+"--"+(4*(len(totalSalesDict)-1))*"-")
    fHorizontalLines.append(breakLine)
    for yCoord in range(len(cascadedLabels[0])):
        for xCoord in range(len(cascadedLabels)):
            if xCoord == 0:
                space = len(max(cascadedLabels[xCoord]))+1
            elif xCoord == 1:
                space = 1
            elif xCoord >1:
                space = 2
            rfListLabels.append('{0:>{width}}'.format(cascadedLabels[xCoord][yCoord], width=space))
    lenList = []
    def chunk(lst, n):
        return list(zip(*[iter(lst)]*n))
    returnFList.append(headerLine)
    for l in chunk(rfListPercentages, 4):
        (returnFList.append(" ".join(l).ljust(len(breakLine)," ")))
    returnFList.append(breakLine)
    for l in chunk(rfListLabels, 4):
        (returnFList.append(" ".join(l).ljust(len(breakLine)," ")))
    for i in returnFList:
        lenList.append(len(i))

    nY=len(returnFList)
    yString=''
    for i in range(nY):
        if i < nY-1:
            ystr = ("""{"""+str(i)+"""}\n""")
        elif i >= nY-1:
            ystr = ("""{"""+str(i)+"""}""")
        yString+=str("""{0}""").format(ystr)
    ReturnString = yString.format(*returnFList)
    return ReturnString
