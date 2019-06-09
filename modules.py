from __future__ import division
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
    answer = ''
    if minorityNotSelected and majorityNotSelected >0 :
        chiSquare = (((((majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected)) * (
                    (majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected))) * N) / (
                                 (majoritySelected + majorityNotSelected) * (minoritySelected + minorityNotSelected) * (
                                     majorityNotSelected + minorityNotSelected) * (majoritySelected + minoritySelected)))
        answer = 'Value for ChiSquare: ' + str(chiSquare)
        print(chiSquare)
        if (chiSquare < 3.841):
            answer = answer + "\n The value of the statistic is less than 3.841"
            answer = answer + "\n Absence of bias with 95% chance"
        else:
            if chiSquare > 6.6635:
                answer = answer + "\n Bias with 99% chance"
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                answer = answer + "\n Bias with 95% chance"
    else:
        answer = answer + "\n chi square : NaN"
        answer = answer + "\n Absence of bias"

    return answer
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
    answer = ''
    #check
    if (y>0):
        sd = ((r/n1)-p)/y
        #conditioned
        answer = "Standard Deviation is " + str(sd)

        if sd < 2:
            answer = answer + "\n No significance in SD"
        else:
            answer = answer + "\n Significantly biased"
    else:
        answer = answer + "\n NaN"
    return answer
#StandardDevReport(minoritySelected, majoritySelected, minority, majority)

def is_CI(lb,ub, ratio):

    if(ratio >= lb and ratio <= ub):
        return "Desperate Impact not found"
    else:
        return "Desperate Impact found"
pass


def ConfidenceInterval(minoritySelected, majoritySelected, minority, majority):

    sd = SD(minoritySelected, majoritySelected, minority, majority)
    r = minoritySelected
    n = majoritySelected+minoritySelected
    p = minority / (majority+minority)
    #q = (b+d)/(a+c)

    ratio = r/n
    #print(ratio)
    lb = p - (1.96 * sd)
    ub = p + (1.96 * sd)

    answer = "lower bound is "+  str(lb)
    answer = answer + "\n upper bound is " + str(ub) + "\n"
    answer = answer +  is_CI(lb,ub, ratio)
    return answer
pass

#ConfidenceInterval(majority,majoritySelected,minority,minoritySelected)
def ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority):
	total = minoritySelected + majoritySelected

	for val in range(0,total+1):

		if((minoritySelected+majoritySelected) <= majority):
			mino = val
			majo = total - val

			#print(mino + '  ' + majo)
			if( adverseImpact(mino,majo,minority,majority) < 0.8 ):
                #answer = ''
				answer = 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority: '+ 'YES'
				answer = answer + ' Probability: '+ str(mino/minority)
				return answer
			elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
                #answer = ''
				answer = 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority: '+ 'NO'
				answer = answer + ' Probability: '+ str(mino/minority)
				return answer

		elif((minoritySelected+majoritySelected) > majority):

			mino = (minoritySelected+majoritySelected) - majority
			majo = majority - val
			#print(str(mino) + '  ' + str(majo))
			if( adverseImpact(mino,majo,minority,majority) < 0.8 ):
                #answer = ''
				answer =  'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority: '+ 'YES'
				answer = answer + ' Probability: '+ str(mino/minority)
				return answer
			elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
                #answer = ''
				answer =  answer +'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority: '+ 'NO'
				answer = answer + ' Probability: '+ str(mino/minority)
				return answer
        return "NaN"


def chiSquareOrFisherExact(minoritySelected, majoritySelected, minority, majority):
    if(minoritySelected < 5 or majoritySelected < 5):
        answer=  fisherexact(minoritySelected, majoritySelected, minority, majority)
    else:
        answer =  chiSquare(minoritySelected, majoritySelected, minority, majority)
    return answer
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

def computeData(s):
    print(s)

if(__name__ == "__main__"):
    majority = 5
    majoritySelected = 2
    minority = 1
    minoritySelected = 0
    calling1(minoritySelected, majoritySelected, minority, majority)
