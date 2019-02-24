####outputs the amount of time required to lose the inputted amount of weight.
#computes and returns the amount of weight you should lose in a week.
def WeeklylbLoss(currentWeight):
    
    return (currentWeight / 100)

#Performs error checking on a float.
def NumTypeTest(testFloat):
    errorFlag = True
    while(errorFlag):
        try:
            float(testFloat)
        except:
            testFloat = input("Invalid Type. Enter a decimal")
        else:
            testFloat = float(testFloat)
            errorFlag = False
    return testFloat


weight2Lose = input("How many pounds do you want to lose: ")
weight2Lose = NumTypeTest(weight2Lose)

#Gathering weight input
weight = -1
while (weight < weight2Lose):
    weight = input("How much do you weigh: ")
    weight = NumTypeTest(weight)
weightLost = 0
weekCount = 0

#Subtracts weight week by week.
while ((weightLost < weight2Lose) and (weight2Lose <= weight)):
    weightLost += WeeklylbLoss(weight)
    weight -= WeeklylbLoss(weight)
    weekCount += 1

print("The weight loss will take", weekCount, "week/s.")
