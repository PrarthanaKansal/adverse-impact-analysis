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
        return ("Minority Applicants are Selected at a rate less than 80% (4/5ths) of the rate that Male Applicants are Selected.")
pass

#working
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
            return ("The value of the statistic is less than 3.841. Absence of bias with 95% chance")

        else:
            if chiSquare > 6.6635:
                return ("Bias with 99% chance")
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                return ("Bias with 95% chance")
    else:
        return ("chi square : NaN")

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
    if (n1>0):
        x= math.sqrt((p*(1-p))/n1) * math.sqrt(1-q)
        return x
    else :
        return "Nan"

def StandardDevReport(minoritySelected, majoritySelected, minority, majority):
    y = SD(minoritySelected, majoritySelected, minority, majority)
    n2 = minority+majority
    p = minority / n2
    n1 = minoritySelected + majoritySelected
    r = minoritySelected
    #check
    if (y>0 and n1 >0):
        sd = ((r/n1)-p)/y
        #conditioned
        # print("SD is :")
        # print(sd)
        StandardDevCheck(sd)
        return sd
    else:
        return "NaN"

def StandardDevCheck(sd):
    if sd < 2:
        return "No significance in SD"
    else:
        return "Significantly biased"
#StandardDevReport(minoritySelected, majoritySelected, minority, majority)

def is_CI(lb,ub, ratio):

    if(ratio >= lb and ratio <= ub):
        return "desperate impact not found"
    else:
        return "desperate impact found"
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

    answer = is_CI(lb,ub, ratio)
    x = "the lower bound is" + str(lb) + "upper bound is" + str(ub) +str(answer)

    return x
pass

#ConfidenceInterval(majority,majoritySelected,minority,minoritySelected)
def ProbabilityDistribution(minoritySelected, majoritySelected, minority, majority):
	total = minoritySelected + majoritySelected
	ans = ''

	if(minority == majority ):
		if((minoritySelected+majoritySelected) > majority):
			# print('1st')
			for val in range(0,minority+1):
				if(((minoritySelected+majoritySelected) - majority + val) > majority):
					# print('break1')
					break
				mino = (minoritySelected+majoritySelected) - majority + val
				majo = majority - val
				if(mino == minoritySelected):
					if( majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'

				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + ' ' + str(majo) +'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'

			return ans

		elif((minoritySelected+majoritySelected) <= majority):
			# print('2nd')
			for val in range(0,minority+1):
				if((total-val) < 0):
					# print('break1')
					break
				mino = val
				majo = total - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'Selected-> '+str(mino) + ' ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + ' ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans
	elif(minority > majority):
		if((majoritySelected+minoritySelected) <= majority):
			# print('3rd')
			for val in range(0,(majoritySelected+minoritySelected)+1):
				if(((minoritySelected+majoritySelected) - val) < 0):
					# print('break3')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val

				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+ '\n'
				# print(str(mino)+' '+str(majo)+' '+str(minority)+' '+str(majority))
				# print(adverseImpact(mino,majo,minority,majority))
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans

		elif((majoritySelected+minoritySelected) > majority):
			# print('4th')
			for val in range(0,majority+1):
				if((((minoritySelected+majoritySelected) - majority) + val) > minority):
					# print('break4')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = min(majority, minority) - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+ '\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+ '\n'

				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans

	#majority>minority
	else:
		if((minoritySelected+majoritySelected) <= minority):
			# print('5th')
			for val in range(0,(minoritySelected+majoritySelected)+1):
				if(((majoritySelected+minoritySelected)+ val) < 0):
					# print('break5')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
						# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
						# print('Probability: '+ str(mino/minority))
						# print()
						ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans

		elif(((minoritySelected+majoritySelected) > minority) & ((minoritySelected+majoritySelected) <= majority)):
			# print('6th')
			# print('(minoritySelected+majoritySelected) '+ str(minoritySelected)+ ' ' + str(majoritySelected)+ ' '+ str(minoritySelected+majoritySelected))
			# print(str(majority))
			for val in range(0,minority +1):
				if((((minoritySelected+majoritySelected) - minority) + val) > majority):
					# print('break6')
					break
				mino = val
				majo = (minoritySelected+majoritySelected) - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans

		elif((minoritySelected+majoritySelected) > majority):
			# print('7th')
			for val in range(0,majority+1):
				if(((minoritySelected+majoritySelected) - minority) + val > majority ):
					# print('break7')
					break
				mino = ((minoritySelected+majoritySelected) - majority) + val
				majo = majority - val
				if(mino == minoritySelected):
					if(majo == majoritySelected):
						# print('SELECTED-> '+ str(mino) + '  ' + str(majo))
						ans += 'SELECTED-> '+ str(mino) + '  ' + str(majo)+'\n'
				else:
					# print(str(mino) + '  ' + str(majo))
					ans += str(mino) + '  ' + str(majo)+'\n'
				if(adverseImpact(mino,majo,minority,majority) == 879645.000000202020):
					# print('Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+ ' NIL ' + '\nAdverse Impact Against Minority? '+ '-> NO\n'
				elif( adverseImpact(mino,majo,minority,majority) < 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> YES\n'
				elif( adverseImpact(mino,majo,minority,majority) >= 0.8 ):
					# print('Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO')
					# print('Probability: '+ str(mino/minority))
					# print()
					ans += 'Adverse Impact Ratio of Minority: '+str(adverseImpact(mino,majo,minority,majority))+ '\nAdverse Impact Against Minority? '+ '-> NO\n'
			return ans

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
