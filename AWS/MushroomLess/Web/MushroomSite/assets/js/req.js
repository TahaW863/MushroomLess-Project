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
    var Res;
    if (value == 1) {
      Res = 'YES!';
    } else {
      Res = 'No!';
    }
    document.getElementById('toggel').innerHTML = Res;
    console.log(x);
    document.getElementById('score').innerHTML = myObj.body;
  }
};
xmlhttp.open('GET', 'SOME-LAMBDA-API', true);
xmlhttp.send();
//#document.getElementById("toggel").innerHTML = "Tutorix";
