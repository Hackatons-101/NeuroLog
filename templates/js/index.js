$('.login-input').on('focus', function() {
  $('.login').addClass('focused');
});
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
$('.login').on('submit', function(e) {
  e.preventDefault();
  $('.login').removeClass('focused').addClass('loading');
  setTimeout(function (){

if(username == "Psychologist" || "Admin" || "admin"){
	window.location = "psychologistView.html" //FIX THIS?
}
else{
	//push from javascript to python linker file
	window.location = "diary.html";
}


}, 100)
});