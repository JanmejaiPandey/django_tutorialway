$(document).ready(function(){ 
$(function(){
  $('.toggle-menu').click(function(e){
    e.preventDefault();
    $('.sidebar').toggleClass('toggled');
  });
});    
  var w = $(window).height();     
  var width = 1;
  var p=0;
  var d = $(document).height();
  var elem = document.getElementById("myPageBar");
  var scrolled_val = $(document).scrollTop();
  var percent_initial = ((w+scrolled_val)/d)*100; 
  elem.style.width = percent_initial +'%'; 
  $("#perc").html("PageRead:<br>"+percent_initial+"%");
 
  $(window).scroll( function() { 
    
    var scrolled_val = $(document).scrollTop();
    var sum = w+scrolled_val;
    var percent = (sum/d)*100;
    if(percent <= 100)
    {
    $("#perc").html("PageRead:<br>"+percent+"%");
    }
    elem.style.width = percent +'%';
    });
  });