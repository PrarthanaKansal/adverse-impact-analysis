from __future__ import division
import math
# import operator
# from functools import reduce
# import matplotlib.pyplot as plt
# import numpy as np

def boolforAI(minoritySelected, majoritySelected, minority, majority):
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

        # print(adverseImpactMajority)
        # print(adverseImpactMinority)
        adverseImpactMinority = round(adverseImpactMinority, 3)
    if adverseImpactMinority > 0.8:
        boolAI = False

    else:
        boolAI = True
    return boolAI

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

        # print(adverseImpactMajority)
        # print(adverseImpactMinority)
        adverseImpactMinority=round(adverseImpactMinority,3)
    if adverseImpactMinority>0.8:

        output="<br><font color = green> Based on these findings, there is no evidence of discriminatory effects on the protected group. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities</font></br>"
        # The Impact  Ratio is "+ str(adverseImpactMinority)+" which is greater than 0.8. It is evident that there is no adverse impact, based on 4/5th's rule.
        return output
    else:
        output="<br><font color = red> Based on these findings, the company may be judged to have had discriminatory effects on the protected group. This negative finding may cause an evaluation of the total scope of the procedures informing hiring decisions to allow adjustments away from disparate impact vulnerabilities.</font></br>"

        # The Impact  Ratio is "+ str(adverseImpactMinority)+" which is less than 0.8. It is evident that there is adverse impact, based on 4/5th's rule.
        return output
pass

#working
def displayAI(numm):
    if(numm < 0.8):
        return ("Minority Applicants are Selected at a rate less than 80% (4/5ths) of the rate that Male Applicants are Selected.")
pass

def boolforchiSquare(minoritySelected, majoritySelected, minority, majority):
    boolchiSquare = False
    boolchiSquare = True
    minorityNotSelected = minority - minoritySelected  # d
    majorityNotSelected = majority - majoritySelected  # b
    N = majority + minority  # majoritySelected a
    # minoritySelected c
    answer = ''
    if minorityNotSelected and majorityNotSelected > 0:
        chiSquare = (((((majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected)) * (
                (majoritySelected * minorityNotSelected) - (majorityNotSelected * minoritySelected))) * N) / (
                             (majoritySelected + majorityNotSelected) * (minoritySelected + minorityNotSelected) * (
                             majorityNotSelected + minorityNotSelected) * (majoritySelected + minoritySelected)))

        chiSquare = round(chiSquare, 3)

        # print(chiSquare)
        if (chiSquare < 3.841):
            boolchiSquare = False

        else:
            if chiSquare > 6.6635:
                boolchiSquare = True
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                boolchiSquare = True
    # else:
    #     answer = answer + "<br> Chi square : NaN"
    #     answer = answer + "<br> Absence of bias"
    return boolchiSquare

def boolforchiFisher(minoritySelected, majoritySelected, minority, majority):
    majorityNotSelected = majority - majoritySelected
    minorityNotSelected = minority - minoritySelected
    a = majority
    b = minority
    c = majoritySelected + minoritySelected
    d = majorityNotSelected + minorityNotSelected
    N = minority + majority + majorityNotSelected + minorityNotSelected

    fe = (fact(a) * fact(b) * fact(c) * fact(d)) / (
            fact(N) * fact(majoritySelected) * fact(majorityNotSelected) * fact(minoritySelected) * fact(
        minorityNotSelected))
    fe = round(fe, 3)
    # print(fe)
    if (fe < 0.05):
        boolFisher = True
    else:
        boolFisher = False
    return boolFisher
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


        chiSquare=round(chiSquare,3)
        answer = 'The value for ChiSquare: ' + str(chiSquare)
        # print(chiSquare)
        if (chiSquare < 3.841):
            answer = answer + "<br><font color = green> The value of the statistic is less than 3.841. "
            answer = answer + "<br> This indicates that there is 95% chance that there is an absence of bias.</font>"
        else:
            if chiSquare > 6.6635:
                answer = answer + "<br><font color = red> The value of statistic is greater than 6.635. This indicates that there is 90% chance that it is a result of bias.</font>"
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                answer = answer + "<br><font color = red> The value of statistic is greater than 3.841 but less than 6.635. This indicates that there is a 95% chance that it is a result of bias.</font>"
    else:
        answer = answer + "<br>The value for Chi square : NaN"
        answer = answer + "<br> This indicates the absence of bias"

    return answer
pass

# chiSquare(minoritySelected, majoritySelected, minority, majority)

def fisherexact(minoritySelected, majoritySelected, minority, majority):
    majorityNotSelected= majority - majoritySelected
    minorityNotSelected=minority - minoritySelected
    a=majority
    b=minority
    c=majoritySelected+minoritySelected
    d=majorityNotSelected+ minorityNotSelected
    N=minority+majority+majorityNotSelected+minorityNotSelected

    fe=(fact(a)*fact(b)*fact(c)*fact(d))/(fact(N)*fact(majoritySelected)*fact(majorityNotSelected)*fact(minoritySelected)*fact(minorityNotSelected))
    fe=round(fe,3)
    # print(fe)
    if(fe<0.05):
        output="<br><font color = red>The value of P is less than 0.05 i.e "+str(fe)+" through which we can infer that the value of p is statistically sigificant. There is a statistically significant chance that these hiring decisions are not fully objective. This negative finding may cause an evaluation of the total scope of the procedures informing hiring decisions to allow adjustments away from disparate impact vulnerabilities. Therefore, this indicates result of bias.</font>"
        return output
    else:
        output="<br><font color = green>The value of P is greater than or equal to 0.05 i.e "+str(fe)+" through which we can infer that the value of p is statistically insigificant. These hiring decisions in this category show no statistically significant results and are within range for objective hiring expectations. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities. Therefore, this indicates that it is not a result of bias.</font>"
        return output
    # y1=majority+minority
    # y2=majoritySelected+minoritySelected
    # x1=majority+majoritySelected
    # x2=minority+minoritySelected

# sys.setrecursionlimit(1500)

# def fact(n):
#    if n == 1:
#        return n

#    if n == 0:
#        return 1
#    else:
#        return n*fact(n-1)

def fact(x):
    result = 1
    for num in range(1, x+1):
        result *= num
    return result

#if((majority<=26) && (minority<=26) && (majoritySelected<26) && (minoritySelected <26)):
    #print('Fisher Exact___________')
    #print('FisherExact: '+ str(fisherexact(minoritySelected, majoritySelected, minority, majority)))
def boolforchiSquareOrFisherExact(minoritySelected, majoritySelected, minority, majority):
    if(minoritySelected < 5 or majoritySelected < 5):
        boolforchiFisher(minoritySelected, majoritySelected, minority, majority)

    else:
        boolforchiSquare(minoritySelected, majoritySelected, minority, majority)

def boolforSD(a):
    boolSD = True
    y = SD(minoritySelected, majoritySelected, minority, majority)
    n2 = minority + majority
    p = minority / n2
    n1 = minoritySelected + majoritySelected
    r = minoritySelected

    if (y > 0):
        sd = ((r / n1) - p) / y
        sd = round(sd, 3)
        # conditioned
        answer = "The standard Deviation is " + str(sd)

        if sd > 0:
            if abs(sd) > 2:
                boolSD = False
            if abs(sd) < 2:
                boolSD = False
        elif sd < 0:
            if abs(sd) > 2:
                boolSD = True
            if abs(sd) < 2:
                boolSD = True
    # elif sd == 0:
    # answer = answer + "<br> NaN"
    # else:
    # answer = answer + "<br> NaN"
    return boolSD

def SD (minoritySelected, majoritySelected, minority, majority):
    n1 = minoritySelected+majoritySelected
    n2 = minority+majority
    # print(n1,n2)
    p = minority/n2
    q = n1 / n2

    val = math.sqrt((p*(1-p))/n1)
    val2 = math.sqrt(1-q)
    return val*val2


def StandardDevReport(minoritySelected, majoritySelected, minority, majority):
    # print(minoritySelected, majoritySelected, minority, majority)
    y = SD(minoritySelected, majoritySelected, minority, majority)
    n2 = minority+majority
    p = minority / n2
    n1 = minoritySelected + majoritySelected
    r = minoritySelected
    answer = ''
    #check
    # print('test')
    if (y>0):
        sd = ((r/n1)-p)/y
        sd=round(sd,3)
        #conditioned
        answer = "The standard Deviation is " + str(sd)

        if sd>0:
            if abs(sd) > 2:
                answer = answer + "<br><font color = green> These results show that any difference between the two groups may be attributed to standard deviation or chance. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities. </font>"
                # These results show no sigificant change. Hence, its not a result of bias.
            if abs(sd) < 2:
                answer += "<font color = green>These results show that any difference between the two groups may be attributed to standard deviation or chance. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities.</font>"
                # These results show no sigificant change. Hence, its not a result of bias.
        elif sd<0:
            if abs(sd) > 2:
                answer += "<font color = red>These results show that the difference between the two groups differ more than what could be attributed to standard deviation or chance. This negative finding may cause an evaluation of the total scope of the procedures informing hiring decisions to allow adjustments away from disparate impact vulnerabilities. </font>"
                #These results show sigificant change. Hence, it is a result of bias.
            if abs(sd) < 2:
                answer += " <font color = red>These results show that the difference between the two groups differ more than what could be attributed to standard deviation or chance. This negative finding may cause an evaluation of the total scope of the procedures informing hiring decisions to allow adjustments away from disparate impact vulnerabilities. </font>"
                #These results show no sigificant change. Hence, its not a result of bias.
        elif sd == 0:
            answer = answer + "<br> NaN"
    else:
        answer = answer + "<br> The standard deviation is: NaN. These results show that any difference between the two groups may be attributed to standard deviation or chance. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities. "
    return answer

def is_CI_bool(lb, ub, ratio):
    if (ratio >= lb and ratio <= ub):
        boolCI = False

    else:
        boolCI = True

    return boolCI


def boolforCI(minoritySelected, majoritySelected, minority, majority):
    sd = SD(minoritySelected, majoritySelected, minority, majority)
    r = minoritySelected
    n = majoritySelected + minoritySelected
    p = minority / (majority + minority)
    # q = (b+d)/(a+c)

    ratio = r / n
    # print(ratio)
    lb = p - (1.96 * sd)
    ub = p + (1.96 * sd)
    is_CI_bool(lb, ub, ratio)



def is_CI(lb,ub, ratio):

    if(ratio >= lb and ratio <= ub):
        return "<font color = green>The results indicate balanced hiring for this protected group. This positive finding will support procedures informing hiring decisions but the company should continue to monitor disparate impact vulnerabilities.</font>"

    else:
        return "<font color = red>The results indicate unbalanced hiring for this protected group. This negative finding may cause an evaluation of the total scope of the procedures informing hiring decisions to allow adjustments away from disparate impact vulnerabilities.</font>"

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
    lb = round(lb,3)
    ub = p + (1.96 * sd)
    ub = round(ub,3)

    answer = "The Lower Bound is "+  str(lb)
    answer = answer + "<br> The Upper Bound is " + str(ub) + "<br>"
    answer = answer +  is_CI(lb,ub, ratio)
    return answer
pass



def chiSquareOrFisherExact(minoritySelected, majoritySelected, minority, majority):
    if(minoritySelected < 5 or majoritySelected < 5):
        answer =  fisherexact(minoritySelected, majoritySelected, minority, majority)
        return answer
    else:
        answer =  chiSquare(minoritySelected, majoritySelected, minority, majority)
        return answer





def calling1(minoritySelected, majoritySelected, minority, majority):
    print(adverseImpact(minoritySelected, majoritySelected, minority, majority))
    print()
    print(chiSquare(minoritySelected, majoritySelected, minority, majority))
    print()
    print(fisherexact(minoritySelected, majoritySelected, minority, majority))
    print()
    print(StandardDevReport(minoritySelected, majoritySelected, minority, majority))
    print()
    print(ConfidenceInterval(minoritySelected, majoritySelected, minority, majority))
def computeData(s):
    print(s)

if(__name__ == "__main__"):
    majority = 8000
    majoritySelected = 50
    minority = 801
    minoritySelected = 10
    if(majority > 0) and (minority > 0):
        calling1(minoritySelected, majoritySelected, minority, majority)
    else:
        print(str(majority)+' '+str(minority))
        print("Since any one of the Majority or Minority is Zero, the result can not be calculated. Please check the numbers and try again.")
