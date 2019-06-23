from flask import Flask, request, render_template, jsonify
from modules import computeData, adverseImpact,StandardDevReport,ConfidenceInterval, chiSquareOrFisherExact
#from modules import ProbabilityDistribution,
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')


@app.route("/api/compute", methods=['GET', 'POST'])
def compute():
    if(request.form.to_dict() == {}):
        return jsonify({'error' : '500'})
    calculateAge = int(request.form['calcA'])
    calculateGender = int(request.form['calcG'])
    calculateRace = int(request.form['calcR'])

    if(calculateRace==1):
        totalWhites = int(request.form['tw'])
        selectedWhites = int(request.form['sw'])
        totalBlacks = int(request.form['tb'])
        selectedBlacks = int(request.form['sb'])
        totalHispanics = int(request.form['thi'])
        selectedHispanics = int(request.form['shi'])
        totalHawaiians = int(request.form['tha'])
        selectedHawaiians = int(request.form['sha'])
        totalAsians = int(request.form['tas'])
        selectedAsians = int(request.form['sas'])
        totalAmericans = int(request.form['tam'])
        selectedAmericans = int(request.form['sam'])
        totalTows = int(request.form['tt'])
        selectedTows = int(request.form['st'])
        benchmarkId = int(request.form['bid'])
        protectedIdArray = json.loads(request.form['pid'])

    if(calculateGender==1):
        totalMales = int(request.form['tm'])
        totalFemales = int(request.form['tf'])
        totalOthers = int(request.form['to'])
        selectedMales = int(request.form['sm'])
        selectedFemales = int(request.form['sf'])
        selectedOthers = int(request.form['so'])
        benchmarkIdGender = int(request.form['bidG'])
        protectedIdGenderArray = json.loads(request.form['pidG'])

    if(calculateAge==1):
        totalYounger = int(request.form['ty'])
        totalOld = int(request.form['told'])
        selectedYounger = int(request.form['sy'])
        selectedOld = int(request.form['sold'])
        benchmarkIdAge = int(request.form['bidA'])
        protectedIdAgeArray = json.loads(request.form['pidA'])

    # print("calA"+ str(calculateAge))
    # print("calG"+ str(calculateGender))
    # print("calR"+ str(calculateRace))
    # print(protectedIdArray)
    # print(protectedIdArray[0])
    # print(protectedIdArray[1])
    # print(protectedIdArray[2])
    # print(protectedIdArray[3])
    # print(protectedIdArray[4])
    # print(len(protectedIdArray))

    aiReport = ""
    sdReport = ""
    ciReport = ""
    ##pdReport = ""
    csReport = ""

    #call functions
    #computeData("sup")
    if(calculateRace==1):
        #print("In Race")
        a = len(protectedIdArray)
        for i in range(2,a-2,4):
            protectedId = int(protectedIdArray[i])
            if(benchmarkId==1):
                if(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedWhites,totalAmericans,totalTows)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedWhites,totalAmericans,totalTows)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedWhites,totalAmericans,totalTows)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedWhites,totalAmericans,totalTows)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedWhites,totalAmericans,totalTows)

            elif(benchmarkId==2):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedBlacks,totalTows,totalBlacks)

            elif(benchmarkId==3):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                elif(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedHispanics,totalTows,totalHispanics)

            elif(benchmarkId==4):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                elif(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)

            elif(benchmarkId==5):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                elif(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedAsians,totalTows,totalAsians)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedAsians,totalTows,totalAsians)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedAsians,totalTows,totalAsians)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedAsians,totalTows,totalAsians)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedAsians,totalTows,totalAsians)

            elif(benchmarkId==6):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                elif(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                elif(protectedId==7):
                    aiReport= aiReport +"For Protected Group: Two or more races " +adverseImpact(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    sdReport= sdReport +"For Protected Group: Two or more races " + StandardDevReport(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    ciReport= ciReport +"For Protected Group: Two or more races " + ConfidenceInterval(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    #pdReport= #pdReport +"For Protected Group: Two or more races " + ProbabilityDistribution(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    csReport= csReport +"For Protected Group: Two or more races " + chiSquareOrFisherExact(selectedTows,selectedAmericans,totalTows,totalAmericans)

            elif(benchmarkId==7):
                if(protectedId==1):
                    aiReport= aiReport +"For Protected Group: White "+adverseImpact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    sdReport= sdReport +"For Protected Group: White "+ StandardDevReport(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    ciReport= ciReport +"For Protected Group: White "+ ConfidenceInterval(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: White "+ ProbabilityDistribution(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    csReport= csReport +"For Protected Group: White "+ chiSquareOrFisherExact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                elif(protectedId==2):
                    aiReport=  aiReport +"For Protected Group: Black or African American " +adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    sdReport=  sdReport +"For Protected Group: Black or African American " + StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    ciReport=  ciReport +"For Protected Group: Black or African American " + ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    #pdReport=  #pdReport +"For Protected Group: Black or African American " + ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    csReport=  csReport +"For Protected Group: Black or African American " + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                elif(protectedId==3):
                    aiReport= aiReport +"For Protected Group: Hispanic or Latinos " +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"For Protected Group: Hispanic or Latinos " + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"For Protected Group: Hispanic or Latinos " + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Hispanic or Latinos " + ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"For Protected Group: Hispanic or Latinos " + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                elif(protectedId==4):
                    aiReport= aiReport +"For Protected Group : Native Hawaiian " +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"For Protected Group : Native Hawaiian " + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"For Protected Group : Native Hawaiian " + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    #pdReport= #pdReport +"For Protected Group : Native Hawaiian " + ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"For Protected Group : Native Hawaiian " + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                elif(protectedId==5):
                    aiReport= aiReport +"For Protected Group: Asian " +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"For Protected Group: Asian " + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"For Protected Group: Asian " + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Asian " + ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"For Protected Group: Asian " + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                elif(protectedId==6):
                    aiReport= aiReport +"For Protected Group: Native American or Alaska Native "+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"For Protected Group: Native American or Alaska Native "+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"For Protected Group: Native American or Alaska Native "+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    #pdReport= #pdReport +"For Protected Group: Native American or Alaska Native "+ ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"For Protected Group: Native American or Alaska Native "+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
    #
    # if(calculateRace==0):
    #     aiReport=""
    #     sdReport=""
    #     ciReport=""
    #     #pdReport=""
    #     csReport=""

    if(calculateGender==1):
        a = len(protectedIdGenderArray)
        for i in range(2,a-2,4):
            protectedIdGender = int(protectedIdGenderArray[i])
            if(benchmarkIdGender==1):
                if(protectedIdGender==2):
                    aiReport=  aiReport +"For Protected Group: Female "+ str(adverseImpact(selectedFemales,selectedMales,totalFemales,totalMales))
                    sdReport=  sdReport +"For Protected Group: Female "+  str(StandardDevReport(selectedFemales,selectedMales,totalFemales,totalMales))
                    ciReport=  ciReport +"For Protected Group: Female "+  str(ConfidenceInterval(selectedFemales,selectedMales,totalFemales,totalMales))
                    #pdReport=  #pdReport +"For Protected Group: Female "+ str(ProbabilityDistribution(selectedFemales,selectedMales,totalFemales,totalMales))
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedMales,totalFemales,totalMales))
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedMales,totalOthers,totalMales))
                    sdReport=   sdReport +"For Protected Group: Other " + str(StandardDevReport(selectedOthers,selectedMales,totalOthers,totalMales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedMales,totalOthers,totalMales))
                    #pdReport=  #pdReport + "For Protected Group: Other " +str(ProbabilityDistribution(selectedOthers,selectedMales,totalOthers,totalMales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedMales,totalOthers,totalMales))
            elif(benchmarkIdGender==2):
                if(protectedIdGender==1):
                    aiReport=  aiReport + "For Protected Group: Male " +str(adverseImpact(selectedMales,selectedFemales,totalMales,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Male " +str(StandardDevReport(selectedMales,selectedFemales,totalMales,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedFemales,totalMales,totalFemales))
                    #pdReport=  #pdReport + "For Protected Group: Male " +str(ProbabilityDistribution(selectedMales,selectedFemales,totalMales,totalFemales))
                    csReport= csReport +  "For Protected Group: Male " +str(chiSquareOrFisherExact(selectedMales,selectedFemales,totalMales,totalFemales))
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Other " +str(StandardDevReport(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    #pdReport=  #pdReport + "For Protected Group: Other " +str(ProbabilityDistribution(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedFemales,totalOthers,totalFemales))
            elif(benchmarkIdGender==3):
                if(protectedIdGender==1):
                    aiReport=  aiReport +"For Protected Group: Male " +str(adverseImpact(selectedMales,selectedOthers,totalMales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Male " + str(StandardDevReport(selectedMales,selectedOthers,totalMales,totalOthers))
                    ciReport=  ciReport +"For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedOthers,totalMales,totalOthers))
                    #pdReport=  #pdReport +"For Protected Group: Male " + str(ProbabilityDistribution(selectedMales,selectedOthers,totalMales,totalOthers))
                    csReport=  csReport +"For Protected Group: Male " + str(chiSquareOrFisherExact(selectedMales,selectedOthers,totalMales,totalOthers))
                elif(protectedIdGender==2):
                    aiReport= aiReport + "For Protected Group: Female "+ str(adverseImpact(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Female "+ str(StandardDevReport(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    ciReport=   ciReport +"For Protected Group: Female "+ str(ConfidenceInterval(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    #pdReport=   #pdReport +"For Protected Group: Female "+ str(ProbabilityDistribution(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedOthers,totalFemales,totalOthers))

    #
    # if(calculateRace==0 and calculateGender==0):
    #     aiReport=""
    #     sdReport=""
    #     ciReport=""
    #     #pdReport=""
    #     csReport=""


    if(calculateAge==1):
        #print("In age")
        a = len(protectedIdAgeArray)
        print(a)
        for i in range(2,a-2,4):
            protectedIdAge = int(protectedIdAgeArray[i])
            if(benchmarkIdAge==1):
                if(protectedIdAge==2):
                    aiReport = aiReport +"For Protected Group: People greater than or equal to the age of 40 " + str(adverseImpact(selectedOld,selectedYounger,totalOld,totalYounger))
                    sdReport = sdReport +"For Protected Group: People greater than or equal to the age of 40 " + str(StandardDevReport(selectedOld,selectedYounger,totalOld,totalYounger))
                    ciReport = ciReport +"For Protected Group: People greater than or equal to the age of 40 " +  str(ConfidenceInterval(selectedOld,selectedYounger,totalOld,totalYounger))
                    #pdReport = #pdReport +"For Protected Group: People greater than or equal to the age of 40 " + str(ProbabilityDistribution(selectedOld,selectedYounger,totalOld,totalYounger))
                    csReport = csReport +"For Protected Group: People greater than or equal to the age of 40 " + str(chiSquareOrFisherExact(selectedOld,selectedYounger,totalOld,totalYounger))
            elif(benchmarkIdAge==2):
                if(protectedIdAge==1):
                    aiReport = aiReport +"For Protected Group: People less than the age of 40 " + str(adverseImpact(selectedYounger,selectedOld,totalYounger,totalOld))
                    sdReport = sdReport +"For Protected Group: People less than the age of 40 " + str(StandardDevReport(selectedYounger,selectedOld,totalYounger,totalOld))
                    ciReport = ciReport +"For Protected Group: People less than the age of 40 " + str(ConfidenceInterval(selectedYounger,selectedOld,totalYounger,totalOld))
                    #pdReport = #pdReport +"For Protected Group: People less than the age of 40 " + str(ProbabilityDistribution(selectedYounger,selectedOld,totalYounger,totalOld))
                    csReport = csReport + "For Protected Group: People less than the age of 40 " + str(chiSquareOrFisherExact(selectedYounger,selectedOld,totalYounger,totalOld))


    return jsonify({
        'aiReport' : aiReport,
        'csReport' : csReport,
        'sdReport' : sdReport,
        'ciReport' : ciReport,
    #    '#pdReport' : #pdReport,
    })

if(__name__ == "__main__"):
    app.run()
