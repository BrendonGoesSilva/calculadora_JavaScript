function insert(num){

  var numero = document.getElementById('result').innerHTML;
  document.getElementById('result').innerHTML = numero + num;

}

function clean(){

  document.getElementById('result').innerHTML = "";

}

function back(){

  var result = document.getElementById('result').innerHTML;
  document.getElementById('result').innerHTML = result.substring(0, result.length -1)

}

function calc(){
  
  var resultado = document.getElementById('result').innerHTML
  if(resultado){
    document.getElementById('result').innerHTML = eval(resultado);
  }

}