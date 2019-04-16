$(document).ready(function(){     
  var w = $(window).height();     
  var width = 1;
  var p=0;
  var d = $(document).height();
  var elem = document.getElementById("myPageBar");
  var scrolled_val = $(document).scrollTop();
  elem.style.width = ((w+scrolled_val)/d)*100 +'%';
  $(window).scroll( function() { 
    var scrolled_val = $(document).scrollTop();
    var sum = w+scrolled_val;
    var percent = (sum/d)*100;
    elem.style.width = percent +'%';
    });
  });