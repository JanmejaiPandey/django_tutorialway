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
  $("#perc").html(Math.round(percent_initial)+"%-Completed");
 
  $(window).scroll( function() { 
    
    var scrolled_val = $(document).scrollTop();
    var sum = w+scrolled_val;
    var percent = (sum/d)*100;
    if(percent <= 100)
    {
    $("#perc").html(Math.round(percent)+"%-Completed");
    }
    elem.style.width = percent +'%';
    });
    function myFunction() {
      document.getElementById("myDropdown").classList.toggle("show");
    }
    
    function filterFunction() {
      var input, filter, ul, li, a, i;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      div = document.getElementById("myDropdown");
      a = div.getElementsByTagName("a");
      for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          a[i].style.display = "";
        } else {
          a[i].style.display = "none";
        }
      }
    }
  });