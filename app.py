from flask import Flask, request, render_template, jsonify
from modules import computeData, adverseImpact,StandardDevReport,ConfidenceInterval,ProbabilityDistribution, chiSquareOrFisherExact

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/api/compute", methods=['GET', 'POST'])
def compute():
    if(request.form.to_dict() == {}):
        return jsonify({'error' : '500'})
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
    protectedId = int(request.form['pid'])

    #call functions
    computeData("sup")
    if(benchmarkId==1):
        if(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            sdReport=StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            ciReport=ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            sdReport=StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            ciReport=ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            sdReport=StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
            sdReport=StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
            ciReport=ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            sdReport=StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            ciReport=ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedWhites,totalAmericans,totalTows)
            sdReport=StandardDevReport(selectedTows,selectedWhites,totalAmericans,totalTows)
            ciReport=ConfidenceInterval(selectedTows,selectedWhites,totalAmericans,totalTows)
            #pdReport=ProbabilityDistribution(selectedTows,selectedWhites,totalAmericans,totalTows)
            csReport=chiSquareOrFisherExact(selectedTows,selectedWhites,totalAmericans,totalTows)

    elif(benchmarkId==2):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
            sdReport=StandardDevReport(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
            ciReport=ConfidenceInterval(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedBlacks,totalWhites,totalBlacks)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
            sdReport=StandardDevReport(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
            ciReport=ConfidenceInterval(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedBlacks,totalHispanics,totalBlacks)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
            sdReport=StandardDevReport(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedBlacks,totalHawaiians,totalBlacks)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
            sdReport=StandardDevReport(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
            ciReport=ConfidenceInterval(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedBlacks,totalAsians,totalBlacks)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
            sdReport=StandardDevReport(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
            ciReport=ConfidenceInterval(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedBlacks,totalAmericans,totalBlacks)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedBlacks,totalTows,totalBlacks)
            sdReport=StandardDevReport(selectedTows,selectedBlacks,totalTows,totalBlacks)
            ciReport=ConfidenceInterval(selectedTows,selectedBlacks,totalTows,totalBlacks)
            #pdReport=ProbabilityDistribution(selectedTows,selectedBlacks,totalTows,totalBlacks)
            csReport=chiSquareOrFisherExact(selectedTows,selectedBlacks,totalTows,totalBlacks)

    elif(benchmarkId==3):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
            sdReport=StandardDevReport(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
            ciReport=ConfidenceInterval(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedHispanics,totalWhites,totalHispanics)
        elif(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
            sdReport=StandardDevReport(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
            ciReport=ConfidenceInterval(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedHispanics,totalBlacks,totalHispanics)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
            sdReport=StandardDevReport(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedHispanics,totalHawaiians,totalHispanics)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
            sdReport=StandardDevReport(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
            ciReport=ConfidenceInterval(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedHispanics,totalAsians,totalHispanics)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
            sdReport=StandardDevReport(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
            ciReport=ConfidenceInterval(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedHispanics,totalAmericans,totalHispanics)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedHispanics,totalTows,totalHispanics)
            sdReport=StandardDevReport(selectedTows,selectedHispanics,totalTows,totalHispanics)
            ciReport=ConfidenceInterval(selectedTows,selectedHispanics,totalTows,totalHispanics)
            #pdReport=ProbabilityDistribution(selectedTows,selectedHispanics,totalTows,totalHispanics)
            csReport=chiSquareOrFisherExact(selectedTows,selectedHispanics,totalTows,totalHispanics)

    elif(benchmarkId==4):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
            sdReport=StandardDevReport(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
            ciReport=ConfidenceInterval(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedHawaiians,totalWhites,totalHawaiians)
        elif(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
            sdReport=StandardDevReport(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
            ciReport=ConfidenceInterval(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedHawaiians,totalBlacks,totalHawaiians)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
            sdReport=StandardDevReport(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
            ciReport=ConfidenceInterval(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedHawaiians,totalHispanics,totalHawaiians)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
            sdReport=StandardDevReport(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
            ciReport=ConfidenceInterval(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedHawaiians,totalAsians,totalHawaiians)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
            sdReport=StandardDevReport(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
            ciReport=ConfidenceInterval(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedHawaiians,totalAmericans,totalHawaiians)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
            sdReport=StandardDevReport(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
            ciReport=ConfidenceInterval(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
            #pdReport=ProbabilityDistribution(selectedTows,selectedHawaiians,totalTows,totalHawaiians)
            csReport=chiSquareOrFisherExact(selectedTows,selectedHawaiians,totalTows,totalHawaiians)

    elif(benchmarkId==5):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedAsians,totalWhites,totalAsians)
            sdReport=StandardDevReport(selectedWhites,selectedAsians,totalWhites,totalAsians)
            ciReport=ConfidenceInterval(selectedWhites,selectedAsians,totalWhites,totalAsians)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedAsians,totalWhites,totalAsians)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedAsians,totalWhites,totalAsians)
        elif(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
            sdReport=StandardDevReport(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
            ciReport=ConfidenceInterval(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedAsians,totalBlacks,totalAsians)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
            sdReport=StandardDevReport(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
            ciReport=ConfidenceInterval(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedAsians,totalHispanics,totalAsians)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
            sdReport=StandardDevReport(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedAsians,totalHawaiians,totalAsians)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
            sdReport=StandardDevReport(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
            ciReport=ConfidenceInterval(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedAsians,totalAmericans,totalAsians)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedAsians,totalTows,totalAsians)
            sdReport=StandardDevReport(selectedTows,selectedAsians,totalTows,totalAsians)
            ciReport=ConfidenceInterval(selectedTows,selectedAsians,totalTows,totalAsians)
            #pdReport=ProbabilityDistribution(selectedTows,selectedAsians,totalTows,totalAsians)
            csReport=chiSquareOrFisherExact(selectedTows,selectedAsians,totalTows,totalAsians)

    elif(benchmarkId==6):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
            sdReport=StandardDevReport(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
            ciReport=ConfidenceInterval(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedAmericans,totalWhites,totalAmericans)
        elif(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
            sdReport=StandardDevReport(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
            ciReport=ConfidenceInterval(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedAmericans,totalBlacks,totalAmericans)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
            sdReport=StandardDevReport(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
            ciReport=ConfidenceInterval(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedAmericans,totalHispanics,totalAmericans)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
            sdReport=StandardDevReport(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedAmericans,totalHawaiians,totalAmericans)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
            sdReport=StandardDevReport(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
            ciReport=ConfidenceInterval(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedAmericans,totalAsians,totalAmericans)
        elif(protectedId==7):
            aiReport=adverseImpact(selectedTows,selectedAmericans,totalTows,totalAmericans)
            sdReport=StandardDevReport(selectedTows,selectedAmericans,totalTows,totalAmericans)
            ciReport=ConfidenceInterval(selectedTows,selectedAmericans,totalTows,totalAmericans)
            #pdReport=ProbabilityDistribution(selectedTows,selectedAmericans,totalTows,totalAmericans)
            csReport=chiSquareOrFisherExact(selectedTows,selectedAmericans,totalTows,totalAmericans)

    elif(benchmarkId==7):
        if(protectedId==1):
            aiReport=adverseImpact(selectedWhites,selectedWhites,totalWhites,totalWhites)
            sdReport=StandardDevReport(selectedWhites,selectedWhites,totalWhites,totalWhites)
            ciReport=ConfidenceInterval(selectedWhites,selectedWhites,totalWhites,totalWhites)
            #pdReport=ProbabilityDistribution(selectedWhites,selectedWhites,totalWhites,totalWhites)
            csReport=chiSquareOrFisherExact(selectedWhites,selectedWhites,totalWhites,totalWhites)
        elif(protectedId==2):
            aiReport=adverseImpact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            sdReport=StandardDevReport(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            ciReport=ConfidenceInterval(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            #pdReport=ProbabilityDistribution(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
            csReport=chiSquareOrFisherExact(selectedBlacks,selectedWhites,totalBlacks,totalWhites)
        elif(protectedId==3):
            aiReport=adverseImpact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            sdReport=StandardDevReport(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            ciReport=ConfidenceInterval(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            #pdReport=ProbabilityDistribution(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
            csReport=chiSquareOrFisherExact(selectedHispanics,selectedWhites,totalHispanics,totalWhites)
        elif(protectedId==4):
            aiReport=adverseImpact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            sdReport=StandardDevReport(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            ciReport=ConfidenceInterval(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            #pdReport=ProbabilityDistribution(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
            csReport=chiSquareOrFisherExact(selectedHawaiians,selectedWhites,totalHawaiians,totalWhites)
        elif(protectedId==5):
            aiReport=adverseImpact(selectedAsians,selectedWhites,totalAsians,totalWhites)
            sdReport=StandardDevReport(selectedAsians,selectedWhites,totalAsians,totalWhites)
            ciReport=ConfidenceInterval(selectedAsians,selectedWhites,totalAsians,totalWhites)
            #pdReport=ProbabilityDistribution(selectedAsians,selectedWhites,totalAsians,totalWhites)
            csReport=chiSquareOrFisherExact(selectedAsians,selectedWhites,totalAsians,totalWhites)
        elif(protectedId==6):
            aiReport=adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            sdReport=StandardDevReport(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            ciReport=ConfidenceInterval(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            #pdReport=ProbabilityDistribution(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
            csReport=chiSquareOrFisherExact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
    #aiReport = 12
    #aiReport=adverseImpact(selectedAmericans,selectedWhites,totalAmericans,totalWhites)
    #csReport = 21
    #sdReport = 2
    #ciReport = "saf"
    pdReport = 213



    return jsonify({
        'aiReport' : aiReport,
        'csReport' : csReport,
        'sdReport' : sdReport,
        'ciReport' : ciReport,
        '#pdReport' : pdReport,
    })

if(__name__ == "__main__"):
    app.run()
