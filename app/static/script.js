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
  $(".navbar.responsive a.icon").click(function(){
    alert("gdgd");
    $(".navbar responsive").slideToggle(1000);
    $(".navbar responsive a").slideToggle(1000); 
    $(".navbar responsive .dropdown").slideToggle(1000); 
  });
  $(".navbar responsive .dropdown").click(function(){
     $(".navbar responsive .dropdown-content").toggle(10000);
  });
});
var favicon_images = [
  'static/images/favicon-16x16.png',
  'static/images/favicon-16x16(1).png',
  'static/images/favicon-16x16(2).png',
  'static/images/favicon-16x16(4).png',
  'static/images/favicon-16x16(5).png',
  'static/images/favicon-16x16(6).png',
  'static/images/favicon-16x16(7).png'
],
image_counter = 0; // To keep track of the current image
$(document).ready(function(){
setInterval(function() {
$("link[rel='icon']").remove();
/*$("link[rel='shortcut icon']").remove();*/
$("head").append('<link rel="icon" type="image/png" sizes="16x16" href="'+favicon_images[image_counter]+'" >');

// If last image then goto first image
// Else go to next image    
if(image_counter == favicon_images.length -1)
image_counter = 0;
else
image_counter++;
}, 200);
});

var favicon_images_icon = [
  'static/images/favicon.ico',
  'static/images/favicon(1).ico',
  'static/images/favicon(2).ico',
  'static/images/favicon(4).ico',
  'static/images/favicon(5).ico',
  'static/images/favicon(6).ico',
  'static/images/favicon(7).ico'
],
image_counter = 0; // To keep track of the current image
$(document).ready(function(){
setInterval(function() {
/*$("link[rel='icon']").remove();*/
$("link[rel='shortcut icon']").remove();
$("head").append('<link rel="icon" type="image/ico" href="'+favicon_images_icon[image_counter]+'" >');

// If last image then goto first image
// Else go to next image    
if(image_counter == favicon_images.length -1)
image_counter = 0;
else
image_counter++;
}, 200);
});