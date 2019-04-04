function myFunction() {
  var x = document.getElementById("myNav");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}
$(document).ready(function(){
  $(".dropdown").hover(function(){
    $(".dropdown-content").show(500);
  },
  function(){
    $(".dropdown-content").hide(600);
  });
  $(".navbar.responsive.icon").click(function(){
    $(".navbar.responsive").slideToggle(1000);
    $(".navbar.responsive.a").slideToggle(1000); 
    $(".navbar.responsive.dropdown").slideToggle(1000); 
  });
  $(".navbar.responsive.dropdown").click(function(){
     $(".navbar.responsive.dropdown.dropdown-content").toggle(10000);
  });
});
