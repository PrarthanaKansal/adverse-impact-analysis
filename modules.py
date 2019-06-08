import math

#working
def adverseImpact(minoritySelected, majoritySelected, minority, majority):
    rateOfMinority = minoritySelected / minority
    rateOfMajority = majoritySelected / majority
    if rateOfMajority == 0:
        adverseImpactMinority = 0
    else:
        adverseImpactMinority = rateOfMinority / rateOfMajority
    if rateOfMinority == 0:
        adverseImpactMajority = 0
    else:
        adverseImpactMajority = rateOfMajority / rateOfMinority
    # print('Rate of Minority: ' + str(rateOfMinority))
    # print('Rate of Majority: ' + str(rateOfMajority))
    # print('Adverse Impact on Minority: ' + str(adverseImpactMinority))
    # print('Adverse Impact on Majority: ' + str(adverseImpactMajority))
    return adverseImpactMinority
#pass

#working
def displayAI(numm):
    if(numm < 0.8):
        print("Minority Applicants are Selected at a rate less than 80% (4/5ths) of the rate that Male Applicants are Selected.")
pass


#working
def chiSquare(minoritySelected, majoritySelected, minority, majority):
    minorityNotSelected = minority - minoritySelected  # d
    majorityNotSelected = majority - majoritySelected  # b
    N = majority + minority  # majoritySelected a
    # minoritySelected c
    if minorityNotSelected and majorityNotSelected >0 :
        chiSquare = (((((majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected)) * (
                    (majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected))) * N) / (
                                 (majoritySelected + majorityNotSelected) * (minoritySelected + minorityNotSelected) * (
                                     majorityNotSelected + minorityNotSelected) * (majoritySelected + minoritySelected)))
        print('Value for ChiSquare: ' + str(chiSquare))

        if (chiSquare < 3.841):
            print("The value of the statistic is less than 3.841")
            print("Absence of bias with 95% chance")
        else:
            if chiSquare > 6.6635:
                print("Bias with 99% chance")
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                print("Bias with 95% chance")
    else:
        print("chi square : NaN")
        print("Absence of bias")


pass

# chiSquare(minoritySelected, majoritySelected, minority, majority)

def fisherexact(minoritySelected, majoritySelected, minority, majority):
    y1=majority+minority
    y2=majoritySelected+minoritySelected
    x1=majority+majoritySelected
    x2=minority+minoritySelected
    print('y1: '+ str(y1))
    print('y2: '+ str(y2))
    print('x1: '+ str(x1))
    print('x2: '+ str(x2))

    return (fact(y1)*fact(y2)*fact(x1)*fact(x2))/(fact(x1+x2)*fact(majority)*fact(majoritySelected)*fact(minority)*fact(majoritySelected))

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

#if((majority<=26) && (minority<=26) && (majoritySelected<26) && (minoritySelected <26)):
    #print('Fisher Exact___________')
    #print('FisherExact: '+ str(fisherexact(minoritySelected, majoritySelected, minority, majority)))

def SD (minoritySelected, majoritySelected, minority, majority):
    n1 = minoritySelected+majoritySelected
    n2 = minority+majority
    p = minority/n2
    q = n1 / n2
    return math.sqrt((p*(1-p))/n1) * math.sqrt(1-q)

def StandardDevReport(minoritySelected, majoritySelected, minority, majority):
    y = SD(minoritySelected, majoritySelected, minority, majority)
    n2 = minority+majority
    p = minority / n2
    n1 = minoritySelected + majoritySelected
    r = minoritySelected
    #check
    if (y>0):
        sd = ((r/n1)-p)/y
        #conditioned
        print("SD is :")
        print(sd)
        if sd < 2:
            print("No significance in SD")
        else:
            print("Significantly biased")
    else:
        print("Standard Deviation report : NaN")

#StandardDevReport(minoritySelected, majoritySelected, minority, majority)

def is_CI(lb,ub, ratio):

    if(ratio >= lb and ratio <= ub):
        print("desperate impact not found")
    else:
        print("desperate impact found")
pass


def ConfidenceInterval(majority,majoritySelected,minority,minoritySelected):

    sd = SD(minoritySelected, majoritySelected, minority, majority)
    r = minoritySelected
    n = majoritySelected+minoritySelected
    p = minority / (majority+minority)
    #q = (b+d)/(a+c)

    ratio = r/n
    #print(ratio)
    lb = p - (1.96 * sd)
    ub = p + (1.96 * sd)

    print("lower bound is", lb)
    print("upper bound is", ub)
    is_CI(lb,ub, ratio)
pass

#ConfidenceInterval(majority,majoritySelected,minority,minoritySelected)
def displayPD(mino, maj, minority, majority,x):
    print("in loop")
    for i in range(x-2,x+2):
        #print("rate of female applicants" + "{}/{}".format(i,minority))
        #print("rate of male applicants" + "{}/{}".format(x-i,majority))
        if i == x:
            print("Adverse impact against minority : YES")
        else:
            print("Adverse impact against minority : NO")
#probability not shown yet

def ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority):
    total = min(minority,majority)
    for x in range(total+1):
        mino = x
        maj = total - x
        print(adverseImpact(mino, maj, minority, majority))
        if adverseImpact(mino, maj, minority, majority) < 0.8:
            maj2 = maj+1
            if adverseImpact(mino, maj2, minority, majority) > 0.8:
                print("found")
                displayPD(mino, maj, minority, majority, x)
            #else:
                #print("not found")
        #else:
            #print("not found")

#check comments and pass before running

def calling(minoritySelected, majoritySelected, minority, majority):
    x = adverseImpact(minoritySelected, majoritySelected, minority, majority)
    displayAI(x)
    print()
    chiSquare(minoritySelected, majoritySelected, minority, majority)
    print()
    if((majoritySelected -minoritySelected) <= 1 & majoritySelected!=majority & minoritySelected!=minoritySelected):
        print('Fisher Exact___________')
        print('FisherExact: '+ str(fisherexact(minoritySelected, majoritySelected, minority, majority)))
    print()
    StandardDevReport(minoritySelected, majoritySelected, minority, majority)
    print()
    ConfidenceInterval(majority, majoritySelected, minority, minoritySelected)
    print()
    ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority)


def calling1(minoritySelected, majoritySelected, minority, majority):
    x = adverseImpact(minoritySelected, majoritySelected, minority, majority)
    displayAI(x)

    if(minoritySelected < 5 or majoritySelected < 5):
        print('FisherExact: '+ str(fisherexact(minoritySelected, majoritySelected, minority, majority)))
    else:
        chiSquare(minoritySelected, majoritySelected, minority, majority)

    print()
    StandardDevReport(minoritySelected, majoritySelected, minority, majority)
    print()
    ConfidenceInterval(majority, majoritySelected, minority, minoritySelected)
    print()
    ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority)

def phatahuacode():
    temp=5
    while(temp>0):
        
        # white
        # whiteSelected
        # black
        # blackSelected
        # hispanic
        # hispanicSelected 
        # hawaiian
        # hawaiianSelected
        # asian
        # asianSelected
        # alaska
        # alaskaSelected
        # tom
        # tomSelected

        print()
        print()
        print()
        print("Enter the number of race which is MAJORITY:")
        print("1. White")
        print("2. Black/Africans")
        print("3. Hispanic/Latinos")
        print("4. Native Hawaiian")
        print("5. Asian")
        print("6. Native American/Alaska Native")
        print("7. Two or More Races")
        majority=0
        inputMaj= takeInput()
        if(inputMaj == 1):
            majority=white
            majoritySelected=whiteSelected
            print("majority: White")
        elif(inputMaj == 2):
            majority=black
            majoritySelected=blackSelected
            print("majority: Blacks")
        elif(inputMaj == 3):
            majority=hispanic
            majoritySelected=hispanicSelected
            print("majority: Hispanic/Latinos")
        elif(inputMaj == 4):
            majority=hawaiian
            majoritySelected=hawaiianSelected
            print("majority: Native Hawaiian")
        elif(inputMaj == 5):
            majority=asian
            majoritySelected=asianSelected
            print("majority: Asian")
        elif(inputMaj == 6):
            majority=alaska
            majoritySelected=alaskaSelected
            print("majority: Native American/Alaska Native")
        elif(inputMaj == 7):
            majority=tom
            majoritySelected=tomSelected
            print("majority: Two/More Races")
        else:
            print("Invalid Input")

        print()
        print()
        print("Enter the number of race which is MINORITY:")
        print("1. White")
        print("2. Black/Africans")
        print("3. Hispanic/Latinos")
        print("4. Native Hawaiian")
        print("5. Asian")
        print("6. Native American/Alaska Native")
        print("7. Two or More Races")
        minority=0
        inputMin= takeInput()
        if(inputMin == 1):
            minority=white
            minoritySelected=whiteSelected
            print("minority: White")
        elif(inputMin == 2):
            minority=black
            minoritySelected=blackSelected
            print("minority: Blakcs")
        elif(inputMin == 3):
            minority=hispanic
            minoritySelected=hispanicSelected
            print("minority: Hispanic/Latinos")
        elif(inputMin == 4):
            minority=hawaiian
            minoritySelected=hispanicSelected
            print("minority: Hawaiian")
        elif(inputMin == 5):
            minority=asian
            minoritySelected=asianSelected
            print("minority: Asian")
        elif(inputMin == 6):
            minority=alaska
            minoritySelected=alaskaSelected
            print("minority: Native American/Alaska Native")
        elif(inputMin == 7):
            minority=tom
            minoritySelected=tomSelected
            print("minority: Two/More Races")
        else:
            print("Invalid Input")

        print()
        print()

        
        temp=temp-1
        print("############################################")

def computeData(s):
    print(s)

if(__name__ == "__main__"):
    majority = 5
    majoritySelected = 2
    minority = 1
    minoritySelected = 0
    calling1(minoritySelected, majoritySelected, minority, majority)