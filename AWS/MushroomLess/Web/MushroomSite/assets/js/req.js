var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    var x = new String(myObj.body);
    var value = 0;
    var yeah = false;
    for (var i = 0; i < x.length; i++) {
      if (x[i] == 'e') {
        yeah = true;
      }
    }
    if (yeah) {
      value = 0;
    } else {
      if (x.length > 6) {
        if (parseInt(x[3]) >= 5) {
          value = 1;
        } else {
          value = 0;
        }
      } else {
        if (parseInt(x[1]) == 1) value = 1;
      }
    }
    var Res='NO';
    var st="Edibility";
    if (value == 1) {
      Res = 'YES!';
      
    } else {
      Res = 'No!';
    }
    
    document.getElementById('tog').innerHTML = Res;
    document.getElementById('score').innerHTML=st+" percentage: "+ new Number(myObj).toFixed(20);
    console.log(myObj);
    
  }
};
xmlhttp.open('GET', 'https://6yg9mzup2l.execute-api.us-east-1.amazonaws.com/default/Lambda-0', true);
xmlhttp.send();
//#document.getElementById("toggel").innerHTML = "Tutorix";
