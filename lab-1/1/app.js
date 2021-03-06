console.log('Welcome to data transmission ');

document.getElementById('message').innerHTML = 'Message from JavaScript';

var user = {
    "id" : 1,
    "name" : "Laura",
    "email" : "laura_secan@yahoo.ro"

};

console.log(user.id)
console.log(user.name);
console.log(user.email);

function test () {
    console.log(user.name === 'Laura' ? "Numele este laura" : "Numele nu este laura")
    console.log(user.id === 1 ? "Id-ul este 1" : "Id-ul nu este 1");
}

test();

$(document).ready(function(){
    $("p").dblclick(function(){
      $(this).hide();
    });
  });