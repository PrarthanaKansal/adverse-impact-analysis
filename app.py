from flask import Flask, request, render_template, jsonify
from modules import computeData, adverseImpact,StandardDevReport,ConfidenceInterval, chiSquareOrFisherExact
from modules import ProbabilityDistribution
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
    pdReport = ""
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
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American </font>" +adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian </font>" + ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedWhites,totalAmericans,totalTows)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedWhites,totalAmericans,totalTows)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedWhites,totalAmericans,totalTows)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ProbabilityDistribution(selectedTows,selectedWhites,totalAmericans,totalTows)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedWhites,totalAmericans,totalTows)

            elif(benchmarkId==2):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White </font>"+ ProbabilityDistribution(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " +adverseImpact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ProbabilityDistribution(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian</font> " +adverseImpact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian </font>" + ProbabilityDistribution(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+ StandardDevReport(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ProbabilityDistribution(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedBlacks,totalTows,totalBlacks)

            elif(benchmarkId==3):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White </font>"+ ProbabilityDistribution(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American </font>" +adverseImpact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ProbabilityDistribution(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian </font>" + ProbabilityDistribution(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ProbabilityDistribution(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedHispanics,totalTows,totalHispanics)

            elif(benchmarkId==4):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White </font>"+ ProbabilityDistribution(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + StandardDevReport(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + ConfidenceInterval(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + ProbabilityDistribution(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " +adverseImpact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + StandardDevReport(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + ConfidenceInterval(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + ProbabilityDistribution(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + chiSquareOrFisherExact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian</font> " +adverseImpact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian</font> " + StandardDevReport(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian</font> " + ConfidenceInterval(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian</font> " + ProbabilityDistribution(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+ StandardDevReport(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ProbabilityDistribution(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)

            elif(benchmarkId==5):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White</font> "+adverseImpact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White</font> "+ StandardDevReport(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White</font> "+ ConfidenceInterval(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White </font>"+ ProbabilityDistribution(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American </font>" +adverseImpact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + StandardDevReport(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + ConfidenceInterval(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ProbabilityDistribution(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ProbabilityDistribution(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedAsians,totalTows,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedAsians,totalTows,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedAsians,totalTows,totalAsians)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ProbabilityDistribution(selectedTows,selectedAsians,totalTows,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedAsians,totalTows,totalAsians)

            elif(benchmarkId==6):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White </font>"+ ProbabilityDistribution(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ProbabilityDistribution(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ProbabilityDistribution(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian</font> " +adverseImpact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian</font> " +adverseImpact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian</font> " + ConfidenceInterval(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian </font>" + ProbabilityDistribution(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian</font> " + chiSquareOrFisherExact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races</font> " +adverseImpact(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races</font> " + ConfidenceInterval(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Two or more races</font> " + ProbabilityDistribution(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races</font> " + chiSquareOrFisherExact(selectedTows,selectedAmericans,totalTows,totalAmericans)

            elif(benchmarkId==7):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White</font> "+adverseImpact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White</font> "+ StandardDevReport(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White</font> "+ ConfidenceInterval(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: White</font> "+ ProbabilityDistribution(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White</font> "+ chiSquareOrFisherExact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    pdReport=  pdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian</font> " + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Asian </font>" + ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    pdReport= pdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
    #
    # if(calculateRace==0):
    #     aiReport=""
    #     sdReport=""
    #     ciReport=""
    #     pdReport=""
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
                    pdReport=  pdReport +"For Protected Group: Female "+ str(ProbabilityDistribution(selectedFemales,selectedMales,totalFemales,totalMales))
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedMales,totalFemales,totalMales))
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedMales,totalOthers,totalMales))
                    sdReport=   sdReport +"For Protected Group: Other " + str(StandardDevReport(selectedOthers,selectedMales,totalOthers,totalMales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedMales,totalOthers,totalMales))
                    pdReport=  pdReport + "For Protected Group: Other " +str(ProbabilityDistribution(selectedOthers,selectedMales,totalOthers,totalMales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedMales,totalOthers,totalMales))
            elif(benchmarkIdGender==2):
                if(protectedIdGender==1):
                    aiReport=  aiReport + "For Protected Group: Male " +str(adverseImpact(selectedMales,selectedFemales,totalMales,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Male " +str(StandardDevReport(selectedMales,selectedFemales,totalMales,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedFemales,totalMales,totalFemales))
                    pdReport=  pdReport + "For Protected Group: Male " +str(ProbabilityDistribution(selectedMales,selectedFemales,totalMales,totalFemales))
                    csReport= csReport +  "For Protected Group: Male " +str(chiSquareOrFisherExact(selectedMales,selectedFemales,totalMales,totalFemales))
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Other " +str(StandardDevReport(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    pdReport=  pdReport + "For Protected Group: Other " +str(ProbabilityDistribution(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedFemales,totalOthers,totalFemales))
            elif(benchmarkIdGender==3):
                if(protectedIdGender==1):
                    aiReport=  aiReport +"For Protected Group: Male " +str(adverseImpact(selectedMales,selectedOthers,totalMales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Male " + str(StandardDevReport(selectedMales,selectedOthers,totalMales,totalOthers))
                    ciReport=  ciReport +"For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedOthers,totalMales,totalOthers))
                    pdReport=  pdReport +"For Protected Group: Male " + str(ProbabilityDistribution(selectedMales,selectedOthers,totalMales,totalOthers))
                    csReport=  csReport +"For Protected Group: Male " + str(chiSquareOrFisherExact(selectedMales,selectedOthers,totalMales,totalOthers))
                elif(protectedIdGender==2):
                    aiReport= aiReport + "For Protected Group: Female "+ str(adverseImpact(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Female "+ str(StandardDevReport(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    ciReport=   ciReport +"For Protected Group: Female "+ str(ConfidenceInterval(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    pdReport=   pdReport +"For Protected Group: Female "+ str(ProbabilityDistribution(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedOthers,totalFemales,totalOthers))

    #
    # if(calculateRace==0 and calculateGender==0):
    #     aiReport=""
    #     sdReport=""
    #     ciReport=""
    #     pdReport=""
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
                    pdReport = pdReport +"For Protected Group: People greater than or equal to the age of 40 " + str(ProbabilityDistribution(selectedOld,selectedYounger,totalOld,totalYounger))
                    csReport = csReport +"For Protected Group: People greater than or equal to the age of 40 " + str(chiSquareOrFisherExact(selectedOld,selectedYounger,totalOld,totalYounger))
            elif(benchmarkIdAge==2):
                if(protectedIdAge==1):
                    aiReport = aiReport +"For Protected Group: People less than the age of 40 " + str(adverseImpact(selectedYounger,selectedOld,totalYounger,totalOld))
                    sdReport = sdReport +"For Protected Group: People less than the age of 40 " + str(StandardDevReport(selectedYounger,selectedOld,totalYounger,totalOld))
                    ciReport = ciReport +"For Protected Group: People less than the age of 40 " + str(ConfidenceInterval(selectedYounger,selectedOld,totalYounger,totalOld))
                    pdReport = pdReport +"For Protected Group: People less than the age of 40 " + str(ProbabilityDistribution(selectedYounger,selectedOld,totalYounger,totalOld))
                    csReport = csReport + "For Protected Group: People less than the age of 40 " + str(chiSquareOrFisherExact(selectedYounger,selectedOld,totalYounger,totalOld))


    return jsonify({
        'aiReport' : aiReport,
        'csReport' : csReport,
        'sdReport' : sdReport,
        'ciReport' : ciReport,
        'pdReport' : pdReport,
    })

if(__name__ == "__main__"):
    app.run()
