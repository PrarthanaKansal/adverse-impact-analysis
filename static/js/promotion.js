var sendData = null;

var raceNumber = null;

var race = document.getElementById("myDIV");
race.style.display = "none";

var gender = document.getElementById("myDIVGender");
gender.style.display = "none";

var age = document.getElementById("myDIVAge");
age.style.display = "none";



/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function computeGender(e){
    // var a = 2.3;
    // console.log(Number.isInteger(a));
    e.preventDefault();
    $("#resultsGender").addClass('d-none');
    if(checkGenderInputs()){
      $.ajax({
          method: 'POST',
          url: "/api/compute",
          beforeSend: function() {

              var calculateGender = 1;
              var calculateAge = 0;
              var calculateRace = 0;

              var totalMales = parseFloat($("#totalMales").val() == "" ? 0 : $("#totalMales").val());
              var selectedMales = parseFloat($("#selectedMales").val() == "" ? 0 : $("#selectedMales").val());

              var totalFemales = parseFloat($("#totalFemales").val() == "" ? 0 : $("#totalFemales").val());
              var selectedFemales = parseFloat($("#selectedFemales").val() == "" ? 0 : $("#selectedFemales").val());

              var totalOthers = parseFloat($("#totalOthers").val() == "" ? 0 : $("#totalOthers").val());
              var selectedOthers = parseFloat($("#selectedOthers").val() == "" ? 0 : $("#selectedOthers").val());

              if($('input[name=benchmark-gender]:checked', '#benchmark-form-gender').val() === undefined){
                var benchmarkIdGender = 0;
              }
              else{
                var benchmarkIdGender = $('input[name=benchmark-gender]:checked', '#benchmark-form-gender').val();
              }
              if($('input[name=protected-gender]:checked', '#protected-form-gender').val() === undefined){
                var protectedIdGender = 0;
              }
              else{
                // var protectedIdGender = $('input[name=protected-gender]:checked', '#protected-form-gender').val();
                var searchIDs = [];
                var protectedIdGender = [];

                $("#protected-form-gender input:checkbox:checked").map(function(){
                  searchIDs.push($(this).val());
                  //console.log(Number.isInteger($(this).val()));
                });
                protectedIdGender = searchIDs;
                protectedIdGender = JSON.stringify(protectedIdGender);
                // console.log("OK");
                // console.log(protectedId);
              }
              sendData = {
                  "tm": totalMales,
                  "tf": totalFemales,
                  "to": totalOthers,
                  "sm": selectedMales,
                  "sf": selectedFemales,
                  "so": selectedOthers,
                  "bidG": benchmarkIdGender,
                  "pidG": JSON.stringify(protectedIdGender),

                  "calcA": calculateAge,
                  "calcG": calculateGender,
                  "calcR": calculateRace,

              }

          },
           data: sendData,
          success: function(result){
            console.log("IN SUCCESS gender");
              if(result['error']) {
                console.log("error");
                  computeGender(e);
              }
              else{
                console.log("IN SUCCESS");
                  populateDataGender(result);
                  sendData = null;
              }

          }
      });
    }

}

function computeAge(e){
    e.preventDefault();
    $("#resultsAge").addClass('d-none');
    if(checkAgeInputs()){
      $.ajax({
          method: 'POST',
          url: "/api/compute",
          beforeSend: function() {

            var calculateAge = 1;
            var calculateGender = 0;
            var calculateRace = 0;

            var totalYounger = parseFloat($("#totalYounger").val() == "" ? 0 : $("#totalYounger").val());
            var selectedYounger = parseFloat($("#selectedYounger").val() == "" ? 0 : $("#selectedYounger").val());

            var totalOld = parseFloat($("#totalOld").val() == "" ? 0 : $("#totalOld").val());
            var selectedOld = parseFloat($("#selectedOld").val() == "" ? 0 : $("#selectedOld").val());

              if($('input[name=benchmark-age]:checked', '#benchmark-form-age').val() === undefined){
                var benchmarkIdAge = 0;
              }
              else{
                var benchmarkIdAge = $('input[name=benchmark-age]:checked', '#benchmark-form-age').val();
              }
              if($('input[name=protected-age]:checked', '#protected-form-age').val() === undefined){
                var protectedIdAge = 0;
              }
              else{
                var searchIDs = [];
                var protectedIdAge = [];

                $("#protected-form-age input:checkbox:checked").map(function(){
                  searchIDs.push($(this).val());
                  //console.log(Number.isInteger($(this).val()));
                });
                protectedIdAge = searchIDs;
                protectedIdAge = JSON.stringify(protectedIdAge);
                // console.log("OK");
                // console.log(protectedId);
              }
              sendData = {
                "ty": totalYounger,
                "told": totalOld,
                "sy": selectedYounger,
                "sold": selectedOld,
                "bidA": benchmarkIdAge,
                "pidA": JSON.stringify(protectedIdAge),

                  "calcA": calculateAge,
                  "calcG": calculateGender,
                  "calcR": calculateRace,

              }

          },
           data: sendData,
          success: function(result){
            console.log("IN SUCCESS Age");
              if(result['error']) {
                console.log("error");
                  computeAge(e);
              }
              else{
                console.log("IN SUCCESS");
                  populateDataAge(result);
                  sendData = null;
              }

          }
      });
    }

}


function compute(e) {
  e.preventDefault();
    $("#results").addClass('d-none');
    if(checkInputs()) {
        $.ajax({
            method: 'POST',
            url: "/api/compute",
            beforeSend: function() {

              var calculateAge = 0;
              var calculateGender = 0;
              var calculateRace = 1;

                var totalWhites = parseFloat($("#totalWhites").val() == "" ? 0 : $("#totalWhites").val());
                var selectedWhites = parseFloat($("#selectedWhites").val() == "" ? 0 : $("#selectedWhites").val());

                var totalBlacks = parseFloat($("#totalBlacks").val() == "" ? 0 : $("#totalBlacks").val());
                var selectedBlacks = parseFloat($("#selectedBlacks").val() == "" ? 0 : $("#selectedBlacks").val());

                var totalHispanics = parseFloat($("#totalHispanics").val() == "" ? 0 : $("#totalHispanics").val());
                var selectedHispanics = parseFloat($("#selectedHispanics").val() == "" ? 0 : $("#selectedHispanics").val());

                var totalHawaiians = parseFloat($("#totalHawaiians").val() == "" ? 0 : $("#totalHawaiians").val());
                var selectedHawaiians = parseFloat($("#selectedHawaiians").val() == "" ? 0 : $("#selectedHawaiians").val());

                var totalAsians = parseFloat($("#totalAsians").val() == "" ? 0 : $("#totalAsians").val());
                var selectedAsians = parseFloat($("#selectedAsians").val() == "" ? 0 : $("#selectedAsians").val());

                var totalAmericans = parseFloat($("#totalAmericans").val() == "" ? 0 : $("#totalAmericans").val());
                var selectedAmericans = parseFloat($("#selectedAmericans").val() == "" ? 0 : $("#selectedAmericans").val());

                var totalTows = parseFloat($("#totalTows").val() == "" ? 0 : $("#totalTows").val());
                var selectedTows = parseFloat($("#selectedTows").val() == "" ? 0 : $("#selectedTows").val());

                if($('input[name=benchmark]:checked', '#benchmark-form').val() === undefined){
                  var benchmarkId = 0;
                }
                else{
                  var benchmarkId = $('input[name=benchmark]:checked', '#benchmark-form').val();
                }
                if($('input[name=protected]:checked', '#protected-form').val() === undefined){
                  var protectedId = 0;
                }
                else{
                  // var protectedId = $('input[name=protected]:checked', '#protected-form').val();
                  var searchIDs = [];
                  var protectedId = [];

                  $("#protected-form input:checkbox:checked").map(function(){
                    searchIDs.push($(this).val());
                    //console.log(Number.isInteger($(this).val()));
                  });
                  protectedId = searchIDs;
                  protectedId = JSON.stringify(protectedId);
                  // console.log("OK");
                  // console.log(protectedId);
                }


                sendData = {
                    "tw": totalWhites,
                    "sw": selectedWhites,
                    "tb": totalBlacks,
                    "sb": selectedBlacks,
                    "thi": totalHispanics,
                    "shi": selectedHispanics,
                    "tha": totalHawaiians,
                    "sha": selectedHawaiians,
                    "tas": totalAsians,
                    "sas": selectedAsians,
                    "tam": totalAmericans,
                    "sam": selectedAmericans,
                    "tt": totalTows,
                    "st": selectedTows,
                    "bid": benchmarkId,
                    "pid": JSON.stringify(protectedId),


                    "calcA": calculateAge,
                    "calcG": calculateGender,
                    "calcR": calculateRace,
                }

            },
             data: sendData,
            success: function(result){
              //console.log("IN SUCCESS Race");
                if(result['error']) {
                  //console.log("error");
                    compute(e);
                }
                else{
                //  console.log("IN SUCCESS");
                    populateData(result);
                    sendData = null;
                }

            }
        });
    }

}



function checkInputs() {

    var totalWhites = parseFloat($("#totalWhites").val()== "" ? 0 : $("#totalWhites").val());
    var selectedWhites = parseFloat($("#selectedWhites").val()== "" ? 0 : $("#selectedWhites").val());
    //console.log(totalWhites);

    var totalBlacks = parseFloat($("#totalBlacks").val()== "" ? 0 : $("#totalBlacks").val());
    var selectedBlacks = parseFloat($("#selectedBlacks").val()== "" ? 0 : $("#selectedBlacks").val());

    var totalHispanics = parseFloat($("#totalHispanics").val()== "" ? 0 : $("#totalHispanics").val());
    var selectedHispanics = parseFloat($("#selectedHispanics").val()== "" ? 0 : $("#selectedHispanics").val());

    var totalHawaiians = parseFloat($("#totalHawaiians").val()== "" ? 0 : $("#totalHawaiians").val());
    var selectedHawaiians = parseFloat($("#selectedHawaiians").val()== "" ? 0 : $("#selectedHawaiians").val());

    var totalAsians = parseFloat($("#totalAsians").val()== "" ? 0 : $("#totalAsians").val());
    var selectedAsians = parseFloat($("#selectedAsians").val()== "" ? 0 : $("#selectedAsians").val());

    var totalAmericans = parseFloat($("#totalAmericans").val()== "" ? 0 : $("#totalAmericans").val());
    var selectedAmericans = parseFloat($("#selectedAmericans").val()== "" ? 0 : $("#selectedAmericans").val());

    var totalTows = parseFloat($("#totalTows").val()== "" ? 0 : $("#totalTows").val());
    var selectedTows = parseFloat($("#selectedTows").val()== "" ? 0 : $("#selectedTows").val());

      if(!Number.isInteger(totalWhites) || !Number.isInteger(totalBlacks) || !Number.isInteger(totalHispanics) || !Number.isInteger(totalHawaiians) || !Number.isInteger(totalAsians) ||  !Number.isInteger(totalAmericans) || !Number.isInteger(totalTows)){
        alert("Total Value must be an Integer");
        return false;
      }

      if(!Number.isInteger(selectedWhites) || !Number.isInteger(selectedBlacks) || !Number.isInteger(selectedHispanics) || !Number.isInteger(selectedHawaiians) || !Number.isInteger(selectedAsians) ||  !Number.isInteger(selectedAmericans) || !Number.isInteger(selectedTows)){
        alert("Selected Value must be an Integer");
        return false;
      }

    if(totalWhites >= 0 && totalBlacks >= 0 && totalHispanics >= 0 && totalHawaiians >= 0 && totalAsians >= 0 && totalAmericans >= 0 && totalTows >= 0) {
        if(selectedWhites >= 0 && selectedBlacks >= 0 && selectedHispanics >= 0 && selectedHawaiians >= 0 && selectedAsians >= 0 && selectedAmericans >= 0 && selectedTows >= 0) {
            if(selectedWhites <= totalWhites && selectedBlacks <= totalBlacks && selectedHispanics <= totalHispanics && selectedHawaiians <= totalHawaiians && selectedAsians <= totalAsians && selectedAmericans <= totalAmericans && selectedTows <= totalTows) {
                if($('input[name=benchmark]:checked', '#benchmark-form').val() === undefined) {
                    alert("Select a Benchmark group");
                    return false;
                }
                else {
                    if($('input[name=protected]:checked', '#protected-form').val() === undefined) {
                        alert("Select a Protected group");
                        return false;
                    }
                    else {
                        return true;
                    }
                }
            }
            else {
                alert("Selected Value Must be <= Total Value")
                return false;
            }
        }
        else {
            alert("Selected Value Must be >= 0")
            return false;
        }
    }
    else{
        alert("Total Value Must be >= 0")
        return false;
    }
    return true;
}

function checkGenderInputs(){
  var totalMales = parseFloat($("#totalMales").val()== "" ? 0 : $("#totalMales").val());
  var selectedMales = parseFloat($("#selectedMales").val()== "" ? 0 : $("#selectedMales").val());

  var totalFemales = parseFloat($("#totalFemales").val()== "" ? 0 : $("#totalFemales").val());
  var selectedFemales = parseFloat($("#selectedFemales").val()== "" ? 0 : $("#selectedFemales").val());

  var totalOthers = parseFloat($("#totalOthers").val()== "" ? 0 : $("#totalOthers").val());
  var selectedOthers = parseFloat($("#selectedOthers").val()== "" ? 0 : $("#selectedOthers").val());

  if(!Number.isInteger(totalMales) || !Number.isInteger(totalFemales) || !Number.isInteger(totalOthers)){
    alert("Total value must not be a fraction");
    return false;
  }
  if(!Number.isInteger(selectedMales) || !Number.isInteger(selectedFemales) || !Number.isInteger(selectedOthers)){
    alert("Selected value must not be a fraction");
    return false;
  }

  if(totalMales >= 0 && totalFemales >= 0 && totalOthers >= 0 ) {
      if(selectedMales >= 0 && selectedFemales >= 0 && selectedOthers >= 0 ) {
          if(selectedMales <= totalMales && selectedFemales <= totalFemales && selectedOthers <= totalOthers) {
              if($('input[name=benchmark-gender]:checked', '#benchmark-form-gender').val() === undefined) {
                alert("Select a Benchmark group in Gender Category");
                  return false;
              }
              else {
                  if($('input[name=protected-gender]:checked', '#protected-form-gender').val() === undefined) {
                      alert("Select a Protected group in Gender Category");
                      return false;
                  }
                  else {
                      return true;
                  }
              }
          }
          else {
              alert("Selected Value Must be <= Total Value")
              return false;
          }
      }
      else {
          alert("Selected Value Must be >= 0")
          return false;
      }
  }
  else{
      alert("Total Value Must be >= 0")
      return false;
  }
  return true;

}

function checkAgeInputs(){
  var totalOld = parseFloat($("#totalOld").val()== "" ? 0 : $("#totalOld").val());
  var selectedOld = parseFloat($("#selectedOld").val()== "" ? 0 : $("#selectedOld").val());

  var totalYounger = parseFloat($("#totalYounger").val()== "" ? 0 : $("#totalYounger").val());
  var selectedYounger = parseFloat($("#selectedYounger").val()== "" ? 0 : $("#selectedYounger").val());

  if(!Number.isInteger(totalOld) || !Number.isInteger(totalYounger)){
    alert("Total value must not be a fraction");
    return false;
  }
  if(!Number.isInteger(selectedOld) || !Number.isInteger(selectedYounger)){
    alert("Selected value must not be a fraction");
    return false;
  }

  if(totalOld >= 0 && totalYounger >= 0  ) {
      if(selectedOld >= 0 && selectedYounger >= 0  ) {
          if(selectedOld <= totalOld && selectedYounger <= totalYounger) {
              if($('input[name=benchmark-age]:checked', '#benchmark-form-age').val() === undefined) {
                  alert("Select a Benchmark group in Age Category");
                  return false;
              }
              else {
                  if($('input[name=protected-age]:checked', '#protected-form-age').val() === undefined) {
                      alert("Select a Protected group in Age Category");
                      return false;
                  }
                  else {
                      return true;
                  }
              }
          }
          else {
              alert("Selected Value Must be <= Total Value")
              return false;
          }
      }
      else {
          alert("Selected Value Must be >= 0")
          return false;
      }
  }
  else{
      alert("Total Value Must be >= 0")
      return false;
  }
  return true;

}

function populateData(data) {

  var aiReport = data.aiReport;
  var csReport = data.csReport;
  var sdReport = data.sdReport;
  var ciReport = data.ciReport;
  //console.log(aiReport);

  Node.prototype.insertAfter = function(newNode, referenceNode) {
      return referenceNode.parentNode.insertBefore(
          newNode, referenceNode.nextSibling);
  };

  var searchIDs = [];
  $("#protected-form input:checkbox:checked").map(function(){
    searchIDs.push($(this).val());
  });
  var refElem = document.getElementById("results");
  var parent = refElem.parentNode;

  var i;
  var ai = 0;
  var aiStartList = [];
  var aiEndList = [];

  var cs = 0;
  var csStartList = [];
  var csEndList = [];

  var sd = 0;
  var sdStartList = [];
  var sdEndList = [];

  var ci = 0;
  var ciStartList = [];
  var ciEndList = [];

  for(i=0; i<searchIDs.length;i++ ){

    var h = document.createElement("H5");
    h.style.width = "100%";
    h.style.height = "50px";
    h.style.backgroundColor = "orange";
    h.style.borderRadius  = "10px";
    h.id="H"+i.toString();
    if(searchIDs[i]==1){
      h.innerHTML = "For Protected Group: White "
    }
    else if (searchIDs[i]==2) {
      h.innerHTML = "For Protected Group: Black or African American"
    }
    else if (searchIDs[i]==3) {
      h.innerHTML = "For Protected Group: Hispanic or Latino "
    }
    else if (searchIDs[i]==4) {
      h.innerHTML = "For Protected Group: Native Hawaiian or Pacific Islander"
    }
    else if (searchIDs[i]==5) {
      h.innerHTML = "For Protected Group: Asian "
    }
    else if (searchIDs[i]==6) {
      h.innerHTML = "For Protected Group: Native American or Alaska Native"
    }
    else if (searchIDs[i]==7) {
      h.innerHTML = "For Protected Group: Two or more races "
    }

    h.style.textAlign = "center";
    h.style.margin = "20px";
    parent.insertAfter(h,refElem);



    var box = document.createElement("BUTTON");
    box.innerHTML = "4/5th Rule";
    box.style.background = "magenta";
    box.style.width = "20%";
    box.style.height = "100px";
    box.style.borderRadius  = "10px";
    box.style.margin = "20px";
    box.id="AI"+i.toString();
    var refElem = document.getElementById("H"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box, refElem);
    var aiStart = aiReport.indexOf("Based",ai);
    var aiEnd = aiReport.indexOf("vulnerabilities",ai);
    aiEnd += 15;
    aiStartList.push(aiStart);
    aiEndList.push(aiEnd);
    ai = aiEnd;
    console.log(aiReport.substring(aiStart,aiEnd));


    var box2 = document.createElement("BUTTON");
    box2.innerHTML = "Chi-Square Test";
    box2.style.background = "magenta";
    box2.style.width = "20%";
    box2.style.height = "100px";
    box2.style.borderRadius  = "10px";
    box2.style.margin = "20px";
    box2.id="CS"+i.toString();
    var refElem = document.getElementById("AI"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box2, refElem);
    var csStart = csReport.indexOf("The",cs);
    var csEnd = csReport.indexOf("bias",cs);
    csEnd +=5;
    csStartList.push(csStart);
    csEndList.push(csEnd);
    cs = csEnd;
    console.log(csReport.substring(csStart,csEnd));


    var box3 = document.createElement("BUTTON");
    box3.innerHTML = "Standard Deviation Test";
    box3.style.background = "magenta";
    box3.style.width = "20%";
    box3.style.height = "100px";
    box3.style.borderRadius  = "10px";
    box3.style.margin = "20px";
    box3.id="SD"+i.toString();
    var refElem = document.getElementById("CS"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box3, refElem);
    var sdStart = sdReport.indexOf("The",sd);
    var sdEnd = sdReport.indexOf("vulnerabilities",sd);
    sdEnd += 15;
    sdStartList.push(sdStart);
    sdEndList.push(sdEnd);
    sd = sdEnd;
    console.log(sdReport.substring(sdStart,sdEnd));


    var box4 = document.createElement("BUTTON");
    box4.innerHTML = "Confidence Interval Test";
    box4.style.background = "magenta";
    box4.style.width = "20%";
    box4.style.height = "100px";
    box4.style.borderRadius  = "10px";
    box4.style.margin = "20px";
    box4.id="CI"+i.toString();
    var refElem = document.getElementById("SD"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box4, refElem);

    var linebreak = document.createElement("br");
    linebreak.id = "linebreak"+i.toString();
    var refElem = document.getElementById("CI"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(linebreak, refElem);

    var refElem = document.getElementById("linebreak"+i.toString());
    var parent = refElem.parentNode;


  }

  var k;
  for(k=0; k<searchIDs.length;k++ ){
    //element.addEventListener("click", function(){ alert("Hello World!"); });

    var id = "AI"+k.toString();
  //  var aaa = document.getElementById(id);
    document.getElementById(id).onmouseover = getClickCallbackAI(k, aiReport, aiStartList, aiEndList);
  //  aaa.onclick = getClickCallbackAI(k, aiReport, aiStartList, aiEndList);

    var id = "CS"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackCS(k, csReport, csStartList, csEndList);

    var id = "SD"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackSD(k, sdReport, sdStartList, sdEndList);


  }

    formatAdverseImpact(data.aiReport);
    formatAdverseImpact(data.csReport);
    formatAdverseImpact(data.sdReport);
    formatAdverseImpact(data.ciReport);
    formatAdverseImpact(data.pdReport);
    $("#results").removeClass('d-none')
    $('html, body').animate({
        scrollTop: $("#results").offset().top
    }, 1000);

}

function getClickCallbackAI(i, aiReport, aiStartList, aiEndList) {
  return function() {
    var id = "AI"+i.toString();
    var ai = document.getElementById("myDIV");
    //var aiReport = data.aiReport;
    document.getElementById("myDIV").innerHTML=aiReport.substring(aiStartList[i],aiEndList[i]);
    if (ai.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        ai.style.opacity = 1;
        ai.style.transform = 'scale(1)';
        ai.style.display = 'block';
        // $('html, body').animate({
        //     scrollTop: $("#results").offset().top
        // }, 1000);
      },700);
    } else {
      ai.style.opacity = 0;
      ai.style.transform = 'scale(0)';
      window.setTimeout(function(){
        ai.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackCS(i, csReport, csStartList, csEndList) {
  return function() {
    var id = "CS"+i.toString();
    var cs = document.getElementById("myDIV");
    //var aiReport = data.aiReport;
    document.getElementById("myDIV").innerHTML=csReport.substring(csStartList[i],csEndList[i]);
    if (cs.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        cs.style.opacity = 1;
        cs.style.transform = 'scale(1)';
        cs.style.display = 'block';
      },700);
    } else {
      cs.style.opacity = 0;
      cs.style.transform = 'scale(0)';
      window.setTimeout(function(){
        cs.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackSD(i, sdReport, sdStartList, sdEndList) {
  return function() {
    var id = "SD"+i.toString();
    var sd = document.getElementById("myDIV");
    //var aiReport = data.aiReport;
    document.getElementById("myDIV").innerHTML=sdReport.substring(sdStartList[i],sdEndList[i]);
    if (sd.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        sd.style.opacity = 1;
        sd.style.transform = 'scale(1)';
        sd.style.display = 'block';
      },700);
    } else {
      sd.style.opacity = 0;
      sd.style.transform = 'scale(0)';
      window.setTimeout(function(){
        sd.style.display = 'none';
      },700);
    }

      };
}


function populateDataGender(data) {
  var aiReport = data.aiReport;
  var csReport = data.csReport;
  var sdReport = data.sdReport;
  var ciReport = data.ciReport;
  //console.log(aiReport);

  Node.prototype.insertAfter = function(newNode, referenceNode) {
      return referenceNode.parentNode.insertBefore(
          newNode, referenceNode.nextSibling);
  };

  var searchIDs = [];
  $("#protected-form-gender input:checkbox:checked").map(function(){
    searchIDs.push($(this).val());
  });
  var refElem = document.getElementById("resultsGender");
  var parent = refElem.parentNode;

  var i;
  var ai = 0;
  var aiStartList = [];
  var aiEndList = [];

  var cs = 0;
  var csStartList = [];
  var csEndList = [];

  var sd = 0;
  var sdStartList = [];
  var sdEndList = [];

  var ci = 0;
  var ciStartList = [];
  var ciEndList = [];

  for(i=0; i<searchIDs.length;i++ ){

    var h = document.createElement("H5");
    h.style.width = "100%";
    h.style.height = "50px";
    h.style.backgroundColor = "orange";
    h.style.borderRadius  = "10px";
    h.id="HGender"+i.toString();
    if(searchIDs[i]==1){
      h.innerHTML = "For Protected Group: Male "
    }
    else if (searchIDs[i]==2) {
      h.innerHTML = "For Protected Group: Female"
    }
    else if (searchIDs[i]==3) {
      h.innerHTML = "For Protected Group: Other "
    }


    h.style.textAlign = "center";
    h.style.margin = "20px";
    parent.insertAfter(h,refElem);



    var box = document.createElement("BUTTON");
    box.innerHTML = "4/5th Rule";
    box.style.background = "magenta";
    box.style.width = "20%";
    box.style.height = "100px";
    box.style.borderRadius  = "10px";
    box.style.margin = "20px";
    box.id="AIGender"+i.toString();
    var refElem = document.getElementById("HGender"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box, refElem);
    var aiStart = aiReport.indexOf("Based",ai);
    var aiEnd = aiReport.indexOf("vulnerabilities",ai);
    aiEnd += 15;
    aiStartList.push(aiStart);
    aiEndList.push(aiEnd);
    ai = aiEnd;
    console.log(aiReport.substring(aiStart,aiEnd));


    var box2 = document.createElement("BUTTON");
    box2.innerHTML = "Chi-Square Test";
    box2.style.background = "magenta";
    box2.style.width = "20%";
    box2.style.height = "100px";
    box2.style.borderRadius  = "10px";
    box2.style.margin = "20px";
    box2.id="CSGender"+i.toString();
    var refElem = document.getElementById("AIGender"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box2, refElem);
    var csStart = csReport.indexOf("The",cs);
    var csEnd = csReport.indexOf("bias",cs);
    csEnd +=5;
    csStartList.push(csStart);
    csEndList.push(csEnd);
    cs = csEnd;
    console.log(csReport.substring(csStart,csEnd));


    var box3 = document.createElement("BUTTON");
    box3.innerHTML = "Standard Deviation Test";
    box3.style.background = "magenta";
    box3.style.width = "20%";
    box3.style.height = "100px";
    box3.style.borderRadius  = "10px";
    box3.style.margin = "20px";
    box3.id="SDGender"+i.toString();
    var refElem = document.getElementById("CSGender"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box3, refElem);
    var sdStart = sdReport.indexOf("The",sd);
    var sdEnd = sdReport.indexOf("vulnerabilities",sd);
    sdEnd += 15;
    sdStartList.push(sdStart);
    sdEndList.push(sdEnd);
    sd = sdEnd;
    console.log(sdReport.substring(sdStart,sdEnd));


    var box4 = document.createElement("BUTTON");
    box4.innerHTML = "Confidence Interval Test";
    box4.style.background = "magenta";
    box4.style.width = "20%";
    box4.style.height = "100px";
    box4.style.borderRadius  = "10px";
    box4.style.margin = "20px";
    box4.id="CIGender"+i.toString();
    var refElem = document.getElementById("SDGender"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box4, refElem);

    var linebreak = document.createElement("br");
    linebreak.id = "linebreakGender"+i.toString();
    var refElem = document.getElementById("CIGender"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(linebreak, refElem);

    var refElem = document.getElementById("linebreakGender"+i.toString());
    var parent = refElem.parentNode;


  }

  var k;
  for(k=0; k<searchIDs.length;k++ ){
    //element.addEventListener("click", function(){ alert("Hello World!"); });

    var id = "AIGender"+k.toString();
  //  var aaa = document.getElementById(id);
    document.getElementById(id).onmouseover = getClickCallbackAIGender(k, aiReport, aiStartList, aiEndList);
  //  aaa.onclick = getClickCallbackAI(k, aiReport, aiStartList, aiEndList);

    var id = "CSGender"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackCSGender(k, csReport, csStartList, csEndList);

    var id = "SDGender"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackSDGender(k, sdReport, sdStartList, sdEndList);


  }

    formatAdverseImpact(data.aiReport);
    formatAdverseImpact(data.csReport);
    formatAdverseImpact(data.sdReport);
    formatAdverseImpact(data.ciReport);
    formatAdverseImpact(data.pdReport);
    // $("#results").removeClass('d-none')
    // $('html, body').animate({
    //     scrollTop: $("#results").offset().top
    // }, 1000);


    $("#resultsGender").removeClass('d-none')
    $('html, body').animate({
        scrollTop: $("#resultsGender").offset().top
    }, 1000);
}

function getClickCallbackAIGender(i, aiReport, aiStartList, aiEndList) {
  return function() {
    var id = "AIGender"+i.toString();
    var ai = document.getElementById("myDIVGender");
    //var aiReport = data.aiReport;
    document.getElementById("myDIVGender").innerHTML=aiReport.substring(aiStartList[i],aiEndList[i]);
    if (ai.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        ai.style.opacity = 1;
        ai.style.transform = 'scale(1)';
        ai.style.display = 'block';
        // $('html, body').animate({
        //     scrollTop: $("#results").offset().top
        // }, 1000);
      },700);
    } else {
      ai.style.opacity = 0;
      ai.style.transform = 'scale(0)';
      window.setTimeout(function(){
        ai.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackCSGender(i, csReport, csStartList, csEndList) {
  return function() {
    var id = "CSGender"+i.toString();
    var cs = document.getElementById("myDIVGender");
    //var aiReport = data.aiReport;
    document.getElementById("myDIVGender").innerHTML=csReport.substring(csStartList[i],csEndList[i]);
    if (cs.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        cs.style.opacity = 1;
        cs.style.transform = 'scale(1)';
        cs.style.display = 'block';
      },700);
    } else {
      cs.style.opacity = 0;
      cs.style.transform = 'scale(0)';
      window.setTimeout(function(){
        cs.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackSDGender(i, sdReport, sdStartList, sdEndList) {
  return function() {
    var id = "SDGender"+i.toString();
    var sd = document.getElementById("myDIVGender");
    //var aiReport = data.aiReport;
    document.getElementById("myDIVGender").innerHTML=sdReport.substring(sdStartList[i],sdEndList[i]);
    if (sd.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        sd.style.opacity = 1;
        sd.style.transform = 'scale(1)';
        sd.style.display = 'block';
      },700);
    } else {
      sd.style.opacity = 0;
      sd.style.transform = 'scale(0)';
      window.setTimeout(function(){
        sd.style.display = 'none';
      },700);
    }

      };
}


function populateDataAge(data) {
  var aiReport = data.aiReport;
  var csReport = data.csReport;
  var sdReport = data.sdReport;
  var ciReport = data.ciReport;
  //console.log(aiReport);

  Node.prototype.insertAfter = function(newNode, referenceNode) {
      return referenceNode.parentNode.insertBefore(
          newNode, referenceNode.nextSibling);
  };

  var searchIDs = [];
  $("#protected-form-age input:checkbox:checked").map(function(){
    searchIDs.push($(this).val());
  });
  var refElem = document.getElementById("resultsAge");
  var parent = refElem.parentNode;

  var i;
  var ai = 0;
  var aiStartList = [];
  var aiEndList = [];

  var cs = 0;
  var csStartList = [];
  var csEndList = [];

  var sd = 0;
  var sdStartList = [];
  var sdEndList = [];

  var ci = 0;
  var ciStartList = [];
  var ciEndList = [];

  for(i=0; i<searchIDs.length;i++ ){

    var h = document.createElement("H5");
    h.style.width = "100%";
    h.style.height = "50px";
    h.style.backgroundColor = "orange";
    h.style.borderRadius  = "10px";
    h.id="HAge"+i.toString();
    if(searchIDs[i]==1){
      h.innerHTML = "For Protected Group: People below the age of 40 "
    }
    else if (searchIDs[i]==2) {
      h.innerHTML = "For Protected Group: People above or equal to the age of 40"
    }



    h.style.textAlign = "center";
    h.style.margin = "20px";
    parent.insertAfter(h,refElem);



    var box = document.createElement("BUTTON");
    box.innerHTML = "4/5th Rule";
    box.style.background = "magenta";
    box.style.width = "20%";
    box.style.height = "100px";
    box.style.borderRadius  = "10px";
    box.style.margin = "20px";
    box.id="AIAge"+i.toString();
    var refElem = document.getElementById("HAge"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box, refElem);
    var aiStart = aiReport.indexOf("Based",ai);
    var aiEnd = aiReport.indexOf("vulnerabilities",ai);
    aiEnd += 15;
    aiStartList.push(aiStart);
    aiEndList.push(aiEnd);
    ai = aiEnd;
    console.log(aiReport.substring(aiStart,aiEnd));


    var box2 = document.createElement("BUTTON");
    box2.innerHTML = "Chi-Square Test";
    box2.style.background = "magenta";
    box2.style.width = "20%";
    box2.style.height = "100px";
    box2.style.borderRadius  = "10px";
    box2.style.margin = "20px";
    box2.id="CSAge"+i.toString();
    var refElem = document.getElementById("AIAge"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box2, refElem);
    var csStart = csReport.indexOf("The",cs);
    var csEnd = csReport.indexOf("bias",cs);
    csEnd +=5;
    csStartList.push(csStart);
    csEndList.push(csEnd);
    cs = csEnd;
    console.log(csReport.substring(csStart,csEnd));


    var box3 = document.createElement("BUTTON");
    box3.innerHTML = "Standard Deviation Test";
    box3.style.background = "magenta";
    box3.style.width = "20%";
    box3.style.height = "100px";
    box3.style.borderRadius  = "10px";
    box3.style.margin = "20px";
    box3.id="SDAge"+i.toString();
    var refElem = document.getElementById("CSAge"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box3, refElem);
    var sdStart = sdReport.indexOf("The",sd);
    var sdEnd = sdReport.indexOf("vulnerabilities",sd);
    sdEnd += 15;
    sdStartList.push(sdStart);
    sdEndList.push(sdEnd);
    sd = sdEnd;
    console.log(sdReport.substring(sdStart,sdEnd));


    var box4 = document.createElement("BUTTON");
    box4.innerHTML = "Confidence Interval Test";
    box4.style.background = "magenta";
    box4.style.width = "20%";
    box4.style.height = "100px";
    box4.style.borderRadius  = "10px";
    box4.style.margin = "20px";
    box4.id="CIAge"+i.toString();
    var refElem = document.getElementById("SDAge"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(box4, refElem);

    var linebreak = document.createElement("br");
    linebreak.id = "linebreakAge"+i.toString();
    var refElem = document.getElementById("CIAge"+i.toString());
    var parent = refElem.parentNode;
    parent.insertAfter(linebreak, refElem);

    var refElem = document.getElementById("linebreakAge"+i.toString());
    var parent = refElem.parentNode;


  }

  var k;
  for(k=0; k<searchIDs.length;k++ ){
    //element.addEventListener("click", function(){ alert("Hello World!"); });

    var id = "AIAge"+k.toString();
  //  var aaa = document.getElementById(id);
    document.getElementById(id).onmouseover = getClickCallbackAIAge(k, aiReport, aiStartList, aiEndList);
  //  aaa.onclick = getClickCallbackAI(k, aiReport, aiStartList, aiEndList);

    var id = "CSAge"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackCSAge(k, csReport, csStartList, csEndList);

    var id = "SDAge"+k.toString();
    document.getElementById(id).onmouseover = getClickCallbackSDAge(k, sdReport, sdStartList, sdEndList);


  }

    formatAdverseImpact(data.aiReport);
    formatAdverseImpact(data.csReport);
    formatAdverseImpact(data.sdReport);
    formatAdverseImpact(data.ciReport);
    formatAdverseImpact(data.pdReport);
    // $("#results").removeClass('d-none')
    // $('html, body').animate({
    //     scrollTop: $("#results").offset().top
    // }, 1000);


    $("#resultsAge").removeClass('d-none')
    $('html, body').animate({
        scrollTop: $("#resultsAge").offset().top
    }, 1000);
}

function getClickCallbackAIAge(i, aiReport, aiStartList, aiEndList) {
  return function() {
    var id = "AAger"+i.toString();
    var ai = document.getElementById("myDIVAge");
    //var aiReport = data.aiReport;
    document.getElementById("myDIAger").innerHTML=aiReport.substring(aiStartList[i],aiEndList[i]);
    if (ai.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        ai.style.opacity = 1;
        ai.style.transform = 'scale(1)';
        ai.style.display = 'block';
        // $('html, body').animate({
        //     scrollTop: $("#results").offset().top
        // }, 1000);
      },700);
    } else {
      ai.style.opacity = 0;
      ai.style.transform = 'scale(0)';
      window.setTimeout(function(){
        ai.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackCSAge(i, csReport, csStartList, csEndList) {
  return function() {
    var id = "CSAge"+i.toString();
    var cs = document.getElementById("myDIVAge");
    //var aiReport = data.aiReport;
    document.getElementById("myDIVAge").innerHTML=csReport.substring(csStartList[i],csEndList[i]);
    if (cs.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        cs.style.opacity = 1;
        cs.style.transform = 'scale(1)';
        cs.style.display = 'block';
      },700);
    } else {
      cs.style.opacity = 0;
      cs.style.transform = 'scale(0)';
      window.setTimeout(function(){
        cs.style.display = 'none';
      },700);
    }

      };
}

function getClickCallbackSDAge(i, sdReport, sdStartList, sdEndList) {
  return function() {
    var id = "SDAge"+i.toString();
    var sd = document.getElementById("myDIVAge");
    //var aiReport = data.aiReport;
    document.getElementById("myDIVAge").innerHTML=sdReport.substring(sdStartList[i],sdEndList[i]);
    if (sd.style.display === "none") {
      //ai.style.display = "block";
      window.setTimeout(function(){
        sd.style.opacity = 1;
        sd.style.transform = 'scale(1)';
        sd.style.display = 'block';
      },700);
    } else {
      sd.style.opacity = 0;
      sd.style.transform = 'scale(0)';
      window.setTimeout(function(){
        sd.style.display = 'none';
      },700);
    }

      };
}

function formatAdverseImpact(data){
  //var $ai = $( "#aiReport" );
  str = data;
  // var indexofThe = str.indexOf("The",0);
  // var heading = str.substring(0,indexofThe);
  html = $.parseHTML( str );


}