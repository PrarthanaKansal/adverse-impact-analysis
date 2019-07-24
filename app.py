from flask import Flask, request, render_template, jsonify
from modules import computeData, adverseImpact,StandardDevReport,ConfidenceInterval, chiSquareOrFisherExact
from modules import boolforAI, boolforchiSquareOrFisherExact, boolforSD, boolforCI
import json
import array
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/selection")
def render_selection():
    return render_template('selection.html')

@app.route("/promotion")
def render_promotion():
    return render_template('promotion.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'images/favicon.ico', mimetype='image/favicon.ico')


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


    aiReport = ""
    sdReport = ""
    ciReport = ""
    #pdReport = " <div style=text-align: center><img src=https://3s81si1s5ygj3mzby34dq6qf-wpengine.netdna-ssl.com/wp-content/uploads/2018/04/ab_balance-600x381.jpg, alt=Paris, width=600, height=250, class=center, padding-right:50px;/></div>"
    csReport = ""

    aiArray = []
    sdArray = []
    ciArray = []
    csArray = []

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
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    aiArray.append(boolforAI(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    sdArray.append(boolforSD(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    ciArray.append(boolforCI(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites));

                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    aiArray.append(boolforAI(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    sdArray.append(boolforSD(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    ciArray.append(boolforCI(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites));

                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    aiArray.append(boolforAI(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    sdArray.append(boolforSD(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    ciArray.append(boolforCI(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));

                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    aiArray.append(boolforAI(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    sdArray.append(boolforSD(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    ciArray.append(boolforCI(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites));

                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    aiArray.append(boolforAI(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    sdArray.append(boolforSD(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    ciArray.append(boolforCI(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites));

                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedWhites,totalAmericans,totalTows)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedWhites,totalAmericans,totalTows)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedWhites,totalAmericans,totalTows)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedWhites,totalAmericans,totalTows)
                    aiArray.append(boolforAI(selectedTows,selectedWhites,totalAmericans,totalTows));
                    sdArray.append(boolforSD(selectedTows,selectedWhites,totalAmericans,totalTows));
                    ciArray.append(boolforCI(selectedTows,selectedWhites,totalAmericans,totalTows));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedWhites,totalAmericans,totalTows));


            elif(benchmarkId==2):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
                    aiArray.append(boolforAI(selectedWhites,selectedBlacks,totalWhites,totalBlacks));
                    sdArray.append(boolforSD(selectedWhites,selectedBlacks,totalWhites,totalBlacks));
                    ciArray.append(boolforCI(selectedWhites,selectedBlacks,totalWhites,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedBlacks,totalWhites,totalBlacks));

                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " +adverseImpact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
                    aiArray.append(boolforAI(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks));
                    sdArray.append(boolforSD(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks));
                    ciArray.append(boolforCI(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks));
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian</font> " +adverseImpact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
                    aiArray.append(boolforAI(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks));
                    sdArray.append(boolforSD(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks));
                    ciArray.append(boolforCI(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks));
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
                    aiArray.append(boolforAI(selectedAsians,selectedBlacks,totalAsians,totalBlacks));
                    sdArray.append(boolforSD(selectedAsians,selectedBlacks,totalAsians,totalBlacks));
                    ciArray.append(boolforCI(selectedAsians,selectedBlacks,totalAsians,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedBlacks,totalAsians,totalBlacks));
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+ StandardDevReport(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
                    aiArray.append(boolforAI(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks));
                    sdArray.append(boolforSD(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks));
                    ciArray.append(boolforCI(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks));
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedBlacks,totalTows,totalBlacks)
                    aiArray.append(boolforAI(selectedTows,selectedBlacks,totalTows,totalBlacks));
                    sdArray.append(boolforSD(selectedTows,selectedBlacks,totalTows,totalBlacks));
                    ciArray.append(boolforCI(selectedTows,selectedBlacks,totalTows,totalBlacks));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedBlacks,totalTows,totalBlacks));

            elif(benchmarkId==3):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
                    aiArray.append(boolforAI(selectedWhites,selectedHispanics,totalWhites,totalHispanics));
                    sdArray.append(boolforSD(selectedWhites,selectedHispanics,totalWhites,totalHispanics));
                    ciArray.append(boolforCI(selectedWhites,selectedHispanics,totalWhites,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedHispanics,totalWhites,totalHispanics));
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American </font>" +adverseImpact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
                    aiArray.append(boolforAI(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics));
                    sdArray.append(boolforSD(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics));
                    ciArray.append(boolforCI(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics));
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
                    aiArray.append(boolforAI(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics));
                    sdArray.append(boolforSD(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics));
                    ciArray.append(boolforCI(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics));
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
                    aiArray.append(boolforAI(selectedAsians,selectedHispanics,totalAsians,totalHispanics));
                    sdArray.append(boolforSD(selectedAsians,selectedHispanics,totalAsians,totalHispanics));
                    ciArray.append(boolforCI(selectedAsians,selectedHispanics,totalAsians,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedHispanics,totalAsians,totalHispanics));
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
                    aiArray.append(boolforAI(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics));
                    sdArray.append(boolforSD(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics));
                    ciArray.append(boolforCI(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics));
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedHispanics,totalTows,totalHispanics)
                    aiArray.append(boolforAI(selectedTows,selectedHispanics,totalTows,totalHispanics));
                    sdArray.append(boolforSD(selectedTows,selectedHispanics,totalTows,totalHispanics));
                    ciArray.append(boolforCI(selectedTows,selectedHispanics,totalTows,totalHispanics));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedHispanics,totalTows,totalHispanics));

            elif(benchmarkId==4):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
                    aiArray.append(boolforAI(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians));
                    sdArray.append(boolforSD(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians));
                    ciArray.append(boolforCI(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians));
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + StandardDevReport(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + ConfidenceInterval(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
                    aiArray.append(boolforAI(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians));
                    sdArray.append(boolforSD(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians));
                    ciArray.append(boolforCI(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians));
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " +adverseImpact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + StandardDevReport(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + ConfidenceInterval(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos</font> " + chiSquareOrFisherExact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
                    aiArray.append(boolforAI(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians));
                    sdArray.append(boolforSD(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians));
                    ciArray.append(boolforCI(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians));
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian</font> " +adverseImpact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian</font> " + StandardDevReport(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian</font> " + ConfidenceInterval(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
                    aiArray.append(boolforAI(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians));
                    sdArray.append(boolforSD(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians));
                    ciArray.append(boolforCI(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians));
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+ StandardDevReport(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
                    aiArray.append(boolforAI(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians));
                    sdArray.append(boolforSD(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians));
                    ciArray.append(boolforCI(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians));
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
                    aiArray.append(boolforAI(selectedTows,selectedHawaiians,totalTows,totalHawaiians));
                    sdArray.append(boolforSD(selectedTows,selectedHawaiians,totalTows,totalHawaiians));
                    ciArray.append(boolforCI(selectedTows,selectedHawaiians,totalTows,totalHawaiians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedHawaiians,totalTows,totalHawaiians));

            elif(benchmarkId==5):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White</font> "+adverseImpact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White</font> "+ StandardDevReport(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White</font> "+ ConfidenceInterval(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedAsians,totalWhites,totalAsians)
                    aiArray.append(boolforAI(selectedWhites,selectedAsians,totalWhites,totalAsians));
                    sdArray.append(boolforSD(selectedWhites,selectedAsians,totalWhites,totalAsians));
                    ciArray.append(boolforCI(selectedWhites,selectedAsians,totalWhites,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedAsians,totalWhites,totalAsians));
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American </font>" +adverseImpact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + StandardDevReport(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + ConfidenceInterval(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
                    aiArray.append(boolforAI(selectedBlacks,selectedAsians,totalBlacks,totalAsians));
                    sdArray.append(boolforSD(selectedBlacks,selectedAsians,totalBlacks,totalAsians));
                    ciArray.append(boolforCI(selectedBlacks,selectedAsians,totalBlacks,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedAsians,totalBlacks,totalAsians));
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
                    aiArray.append(boolforAI(selectedHispanics,selectedAsians,totalHispanics,totalAsians));
                    sdArray.append(boolforSD(selectedHispanics,selectedAsians,totalHispanics,totalAsians));
                    ciArray.append(boolforCI(selectedHispanics,selectedAsians,totalHispanics,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedAsians,totalHispanics,totalAsians));
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
                    aiArray.append(boolforAI(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians));
                    sdArray.append(boolforSD(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians));
                    ciArray.append(boolforCI(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians));
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native</font> "+adverseImpact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
                    aiArray.append(boolforAI(selectedAmericans,selectedAsians,totalAmericans,totalAsians));
                    sdArray.append(boolforSD(selectedAmericans,selectedAsians,totalAmericans,totalAsians));
                    ciArray.append(boolforCI(selectedAmericans,selectedAsians,totalAmericans,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedAsians,totalAmericans,totalAsians));
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races </font>" +adverseImpact(selectedTows,selectedAsians,totalTows,totalAsians)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedAsians,totalTows,totalAsians)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + ConfidenceInterval(selectedTows,selectedAsians,totalTows,totalAsians)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + chiSquareOrFisherExact(selectedTows,selectedAsians,totalTows,totalAsians)
                    aiArray.append(boolforAI(selectedTows,selectedAsians,totalTows,totalAsians));
                    sdArray.append(boolforSD(selectedTows,selectedAsians,totalTows,totalAsians));
                    ciArray.append(boolforCI(selectedTows,selectedAsians,totalTows,totalAsians));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedAsians,totalTows,totalAsians));

            elif(benchmarkId==6):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White </font>"+adverseImpact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White </font>"+ StandardDevReport(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White </font>"+ ConfidenceInterval(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White </font>"+ chiSquareOrFisherExact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
                    aiArray.append(boolforAI(selectedWhites,selectedAmericans,totalWhites,totalAmericans));
                    sdArray.append(boolforSD(selectedWhites,selectedAmericans,totalWhites,totalAmericans));
                    ciArray.append(boolforCI(selectedWhites,selectedAmericans,totalWhites,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedAmericans,totalWhites,totalAmericans));
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + chiSquareOrFisherExact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
                    aiArray.append(boolforAI(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans));
                    sdArray.append(boolforSD(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans));
                    ciArray.append(boolforCI(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans));
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
                    aiArray.append(boolforAI(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans));
                    sdArray.append(boolforSD(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans));
                    ciArray.append(boolforCI(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans));
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian</font> " +adverseImpact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
                    aiArray.append(boolforAI(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans));
                    sdArray.append(boolforSD(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans));
                    ciArray.append(boolforCI(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans));
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian</font> " +adverseImpact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian </font>" + StandardDevReport(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian</font> " + ConfidenceInterval(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian</font> " + chiSquareOrFisherExact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
                    aiArray.append(boolforAI(selectedAsians,selectedAmericans,totalAsians,totalAmericans));
                    sdArray.append(boolforSD(selectedAsians,selectedAmericans,totalAsians,totalAmericans));
                    ciArray.append(boolforCI(selectedAsians,selectedAmericans,totalAsians,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedAmericans,totalAsians,totalAmericans));
                elif(protectedId==7):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Two or more races</font> " +adverseImpact(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Two or more races </font>" + StandardDevReport(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Two or more races</font> " + ConfidenceInterval(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Two or more races</font> " + chiSquareOrFisherExact(selectedTows,selectedAmericans,totalTows,totalAmericans)
                    aiArray.append(boolforAI(selectedTows,selectedAmericans,totalTows,totalAmericans));
                    sdArray.append(boolforSD(selectedTows,selectedAmericans,totalTows,totalAmericans));
                    ciArray.append(boolforCI(selectedTows,selectedAmericans,totalTows,totalAmericans));
                    csArray.append(boolforchiSquareOrFisherExact(selectedTows,selectedAmericans,totalTows,totalAmericans));

            elif(benchmarkId==7):
                if(protectedId==1):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: White</font> "+adverseImpact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: White</font> "+ StandardDevReport(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: White</font> "+ ConfidenceInterval(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: White</font> "+ chiSquareOrFisherExact(selectedWhites,selectedWhites,totalWhites,totalWhites)
                    aiArray.append(boolforAI(selectedWhites,selectedWhites,totalWhites,totalWhites));
                    sdArray.append(boolforSD(selectedWhites,selectedWhites,totalWhites,totalWhites));
                    ciArray.append(boolforCI(selectedWhites,selectedWhites,totalWhites,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedWhites,selectedWhites,totalWhites,totalWhites));
                elif(protectedId==2):
                    aiReport=  aiReport +"<br><font color='red'>For Protected Group: Black or African American</font> " +adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    sdReport=  sdReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    ciReport=  ciReport +"<br><font color='red'>For Protected Group: Black or African American </font>" + ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    csReport=  csReport +"<br><font color='red'>For Protected Group: Black or African American</font> " + chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
                    aiArray.append(boolforAI(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    sdArray.append(boolforSD(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    ciArray.append(boolforCI(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites));
                elif(protectedId==3):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" +adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Hispanic or Latinos </font>" + chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
                    aiArray.append(boolforAI(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    sdArray.append(boolforSD(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    ciArray.append(boolforCI(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites));
                elif(protectedId==4):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" +adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group : Native Hawaiian </font>" + chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
                    aiArray.append(boolforAI(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    sdArray.append(boolforSD(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    ciArray.append(boolforCI(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites));
                elif(protectedId==5):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Asian </font>" +adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Asian</font> " + StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Asian </font>" + ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Asian </font>" + chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
                    aiArray.append(boolforAI(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    sdArray.append(boolforSD(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    ciArray.append(boolforCI(selectedAsians,selectedWhites,totalAsians,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites));
                elif(protectedId==6):
                    aiReport= aiReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    sdReport= sdReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    ciReport= ciReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    csReport= csReport +"<br><font color='red'>For Protected Group: Native American or Alaska Native </font>"+ chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
                    aiArray.append(boolforAI(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    sdArray.append(boolforSD(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    ciArray.append(boolforCI(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
                    csArray.append(boolforchiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites));
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
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedMales,totalFemales,totalMales))
                    aiArray.append(boolforAI(selectedFemales,selectedMales,totalFemales,totalMales));
                    sdArray.append(boolforSD(selectedFemales,selectedMales,totalFemales,totalMales));
                    ciArray.append(boolforCI(selectedFemales,selectedMales,totalFemales,totalMales));
                    csArray.append(boolforchiSquareOrFisherExact(selectedFemales,selectedMales,totalFemales,totalMales));
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedMales,totalOthers,totalMales))
                    sdReport=   sdReport +"For Protected Group: Other " + str(StandardDevReport(selectedOthers,selectedMales,totalOthers,totalMales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedMales,totalOthers,totalMales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedMales,totalOthers,totalMales))
                    aiArray.append(boolforAI(selectedOthers,selectedMales,totalOthers,totalMales));
                    sdArray.append(boolforSD(selectedOthers,selectedMales,totalOthers,totalMales));
                    ciArray.append(boolforCI(selectedOthers,selectedMales,totalOthers,totalMales));
                    csArray.append(boolforchiSquareOrFisherExact(selectedOthers,selectedMales,totalOthers,totalMales));
            elif(benchmarkIdGender==2):
                if(protectedIdGender==1):
                    aiReport=  aiReport + "For Protected Group: Male " +str(adverseImpact(selectedMales,selectedFemales,totalMales,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Male " +str(StandardDevReport(selectedMales,selectedFemales,totalMales,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedFemales,totalMales,totalFemales))
                    csReport= csReport +  "For Protected Group: Male " +str(chiSquareOrFisherExact(selectedMales,selectedFemales,totalMales,totalFemales))
                    aiArray.append(boolforAI(selectedMales,selectedFemales,totalMales,totalFemales));
                    sdArray.append(boolforSD(selectedMales,selectedFemales,totalMales,totalFemales));
                    ciArray.append(boolforCI(selectedMales,selectedFemales,totalMales,totalFemales));
                    csArray.append(boolforchiSquareOrFisherExact(selectedMales,selectedFemales,totalMales,totalFemales));
                elif(protectedIdGender==3):
                    aiReport=  aiReport + "For Protected Group: Other " +str(adverseImpact(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    sdReport=  sdReport + "For Protected Group: Other " +str(StandardDevReport(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    ciReport=  ciReport + "For Protected Group: Other " + str(ConfidenceInterval(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    csReport=  csReport + "For Protected Group: Other " +str(chiSquareOrFisherExact(selectedOthers,selectedFemales,totalOthers,totalFemales))
                    aiArray.append(boolforAI(selectedOthers,selectedFemales,totalOthers,totalFemales));
                    sdArray.append(boolforSD(selectedOthers,selectedFemales,totalOthers,totalFemales));
                    ciArray.append(boolforCI(selectedOthers,selectedFemales,totalOthers,totalFemales));
                    csArray.append(boolforchiSquareOrFisherExact(selectedOthers,selectedFemales,totalOthers,totalFemales));
            elif(benchmarkIdGender==3):
                if(protectedIdGender==1):
                    aiReport=  aiReport +"For Protected Group: Male " +str(adverseImpact(selectedMales,selectedOthers,totalMales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Male " + str(StandardDevReport(selectedMales,selectedOthers,totalMales,totalOthers))
                    ciReport=  ciReport +"For Protected Group: Male " + str(ConfidenceInterval(selectedMales,selectedOthers,totalMales,totalOthers))
                    csReport=  csReport +"For Protected Group: Male " + str(chiSquareOrFisherExact(selectedMales,selectedOthers,totalMales,totalOthers))
                    aiArray.append(boolforAI(selectedMales,selectedOthers,totalMales,totalOthers));
                    sdArray.append(boolforSD(selectedMales,selectedOthers,totalMales,totalOthers));
                    ciArray.append(boolforCI(selectedMales,selectedOthers,totalMales,totalOthers));
                    csArray.append(boolforchiSquareOrFisherExact(selectedMales,selectedOthers,totalMales,totalOthers));
                elif(protectedIdGender==2):
                    aiReport= aiReport + "For Protected Group: Female "+ str(adverseImpact(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    sdReport=  sdReport +"For Protected Group: Female "+ str(StandardDevReport(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    ciReport=   ciReport +"For Protected Group: Female "+ str(ConfidenceInterval(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    csReport=  csReport +"For Protected Group: Female "+ str(chiSquareOrFisherExact(selectedFemales,selectedOthers,totalFemales,totalOthers))
                    aiArray.append(boolforAI(selectedFemales,selectedOthers,totalFemales,totalOthers));
                    sdArray.append(boolforSD(selectedFemales,selectedOthers,totalFemales,totalOthers));
                    ciArray.append(boolforCI(selectedFemales,selectedOthers,totalFemales,totalOthers));
                    csArray.append(boolforchiSquareOrFisherExact(selectedFemales,selectedOthers,totalFemales,totalOthers));

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
                    csReport = csReport +"For Protected Group: People greater than or equal to the age of 40 " + str(chiSquareOrFisherExact(selectedOld,selectedYounger,totalOld,totalYounger))
                    aiArray.append(boolforAI(selectedOld,selectedYounger,totalOld,totalYounger));
                    sdArray.append(boolforSD(selectedOld,selectedYounger,totalOld,totalYounger));
                    ciArray.append(boolforCI(selectedOld,selectedYounger,totalOld,totalYounger));
                    csArray.append(boolforchiSquareOrFisherExact(selectedOld,selectedYounger,totalOld,totalYounger));
            elif(benchmarkIdAge==2):
                if(protectedIdAge==1):
                    aiReport = aiReport +"For Protected Group: People less than the age of 40 " + str(adverseImpact(selectedYounger,selectedOld,totalYounger,totalOld))
                    sdReport = sdReport +"For Protected Group: People less than the age of 40 " + str(StandardDevReport(selectedYounger,selectedOld,totalYounger,totalOld))
                    ciReport = ciReport +"For Protected Group: People less than the age of 40 " + str(ConfidenceInterval(selectedYounger,selectedOld,totalYounger,totalOld))
                    csReport = csReport + "For Protected Group: People less than the age of 40 " + str(chiSquareOrFisherExact(selectedYounger,selectedOld,totalYounger,totalOld))
                    aiArray.append(boolforAI(selectedYounger,selectedOld,totalYounger,totalOld));
                    sdArray.append(boolforSD(selectedYounger,selectedOld,totalYounger,totalOld));
                    ciArray.append(boolforCI(selectedYounger,selectedOld,totalYounger,totalOld));
                    csArray.append(boolforchiSquareOrFisherExact(selectedYounger,selectedOld,totalYounger,totalOld));

    print(aiArray)
    print(csArray)
    print(sdArray)
    print(ciArray)
    return jsonify({
        'aiReport' : aiReport,
        'csReport' : csReport,
        'sdReport' : sdReport,
        'ciReport' : ciReport,

        'aiArray' : aiArray,
        'csArray' : csArray,
        'ciArray' : ciArray,
        'sdArray' : sdArray,
    })

if(__name__ == "__main__"):
    app.run()
