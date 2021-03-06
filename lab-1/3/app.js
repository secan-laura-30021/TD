var counter = 0;

function printValue(divId, value) {
  document.getElementById(divId).innerHTML = value;
}
printValue('counter', 0);

document.getElementById('inc').addEventListener('click', increment);

function increment() {
  counter++;
  printValue('counter', counter);
}

function sum(n) {
  if (typeof n != 'number') return "not a number";
  var sum = 0;
  for(var i = 1; i <= n; i++){
    sum = sum + i;
  }
  return sum;
}


