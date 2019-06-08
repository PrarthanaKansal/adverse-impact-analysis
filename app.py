from flask import Flask, request, render_template, jsonify
from modules import computeData

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/api/compute", methods=['GET', 'POST'])
def compute():
    if(request.form.to_dict() == {}):
        return jsonify({'error' : '500'})
    totalWhites = request.form['tw']
    selectedWhites = request.form['sw']
    totalBlacks = request.form['tb']
    selectedBlacks = request.form['sb']
    totalHispanics = request.form['thi']
    selectedHispanics = request.form['shi']
    totalHawaiians = request.form['tha']
    selectedHawaiians = request.form['sha']
    totalAsians = request.form['tas']
    selectedAsians = request.form['sas']
    totalAmericans = request.form['tam']
    selectedAmericans = request.form['sam']
    totalTows = request.form['tt']
    selectedTows = request.form['st']
    benchmarkId = request.form['bid']
    protectedId = request.form['pid']

    #call functions
    computeData("sup")

    aiReport = 12
    csReport = 21
    sdReport = 2
    ciReport = "saf"
    pdReport = 213

    return jsonify({
        'aiReport' : aiReport,
        'csReport' : csReport,
        'sdReport' : sdReport,
        'ciReport' : ciReport,
        'pdReport' : pdReport,
    })

if(__name__ == "__main__"):
    app.run()