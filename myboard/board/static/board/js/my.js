$(document).ready(function() {

  $(".collapsible").click(function(){
  $(".mycontent").show('fast');
})
  $(".fa-times").click(function(){
    $(".mycontent").hide();
  });
});