$('.login-input').on('focus', function() {
  $('.login').addClass('focused');
});
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
$('.login').on('submit', function(e) {
  e.preventDefault();
  $('.login').removeClass('focused').addClass('loading');
  setTimeout(function (){


  window.location = "diary.html";

}, 1000)
});