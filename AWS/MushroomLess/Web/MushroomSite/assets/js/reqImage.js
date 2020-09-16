var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    //var x = new String(myObj.body);

    document.getElementById('tog').innerHTML = myObj[0];
    document.getElementById('score').innerHTML = myObj[1];
    console.log(myObj);
    
  }
};
xmlhttp.open('GET', 'https://rnnwnu5bl9.execute-api.us-east-1.amazonaws.com/default/lambda-1', true);
xmlhttp.send();
//#document.getElementById("toggel").innerHTML = "Tutorix";
