$('.login-input').on('focus', function() {
  $('.login').addClass('focused');
});

$('.login').on('submit', function(e) {
  e.preventDefault();
  $('.login').removeClass('focused').addClass('loading');
  setTimeout(function (){


  window.location = "file:///C:/Users/wstarr/Desktop/khe/diary.html";

}, 2000)
});