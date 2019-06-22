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

        # print(adverseImpactMajority)
        # print(adverseImpactMinority)

    if adverseImpactMinority>0.8:
        output="The Impact  Ratio is "+ str(adverseImpactMinority)+" which is greater than 0.8. It, is evident that there is no adverse impact, based on 4/5th's rule. "
        return output
    else:
        output="The Impact  Ratio is "+ str(adverseImpactMinority)+" which is less than 0.8. It, is evident that there is adverse impact, based on 4/5th's rule. "
        return output
pass

#working
def displayAI(numm):
    if(numm < 0.8):
        return ("Minority Applicants are Selected at a rate less than 80% (4/5ths) of the rate that Male Applicants are Selected.")
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
        # print(chiSquare)
        if (chiSquare < 3.841):
            answer = answer + "\n The value of the statistic is less than 3.841. "
            answer = answer + "\n This indicates that there is absence of bias with 95% chance. Therefore, It can be concluded that these results are not the result of bias."
        else:
            if chiSquare > 6.6635:
                answer = answer + "\n The value of statistic is greater than 6.635. This indicates that its is a result of bias with 99% chance."
            elif (chiSquare > 3.841 and chiSquare < 6.635):
                answer = answer + "\n The value of statistic is greater than 3.841 but less than 6.635. This indicates that it is a result of bias with 95% chance."
    else:
        answer = answer + "\n chi square : NaN"
        answer = answer + "\n Absence of bias"

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
    # print(fe)
    if(fe<0.05):
        output="The value of P is less than 0.05 i.e "+str(fe)+" through which we can infer that the value of p is statistically sigificant. Therefore, this indicates result of bias."
        return output
    else:
        output="The value of P is greater than or equal to 0.05 i.e "+str(fe)+" through which we can infer that the value of p is statistically insigificant. Therefore, this indicates that it is not a result of bias."
        return output
    # y1=majority+minority
    # y2=majoritySelected+minoritySelected
    # x1=majority+majoritySelected
    # x2=minority+minoritySelected

def fact(n):


   if n == 1:
       return n

   if n == 0:
       return 1
   else:
       return n*fact(n-1)

#if((majority<=26) && (minority<=26) && (majoritySelected<26) && (minoritySelected <26)):
    #print('Fisher Exact___________')
    #print('FisherExact: '+ str(fisherexact(minoritySelected, majoritySelected, minority, majority)))

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
        #conditioned
        answer = "Standard Deviation is " + str(sd)

        if sd>0:
            if abs(sd) > 2:
                answer = answer + "\n  These results show no sigificant change. Hence, its not a result of bias. "
            if abs(sd) < 2:
                answer += " These results show no sigificant change. Hence, its not a result of bias."
        elif sd<0:
            if abs(sd) > 2:
                answer += " These results show sigificant change. Hence, it is a result of bias."
            if abs(sd) < 2:
                answer += " These results show no sigificant change. Hence, its not a result of bias."
        elif sd == 0:
            answer = answer + "\n NaN"
    else:
        answer = answer + "\n NaN"
    return answer



def is_CI(lb,ub, ratio):

    if(ratio >= lb and ratio <= ub):
        return "These results show that the proportion of protected group selected is contained in the confidence intervalTherefore a finding of disparate impact is not supported by this data."
    else:
        return "These results show that the proportion of protected group selected is not contained in the confidence interval. Therefore a finding of disparate impact is  supported by this data."
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

    answer = "Lower Bound is "+  str(lb)
    answer = answer + "\n Upper Bound is " + str(ub) + "\n"
    answer = answer +  is_CI(lb,ub, ratio)
    return answer
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
        answer =  fisherexact(minoritySelected, majoritySelected, minority, majority)
        return answer
    else:
        answer =  chiSquare(minoritySelected, majoritySelected, minority, majority)
        return answer
#check comments and pass before running
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
