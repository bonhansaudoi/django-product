

/* Vnav */
// Vnav
$(document).ready(function(){  
  $("#Vnav>a").click(function(){
    $("a.active").removeClass("active"); 
    $(this).addClass("active").children().toggleClass('fa-angle-up fa-angle-down'); 
    $(this).next('.Vnav').toggle(); 
    $(this).siblings().find('i.fa-angle-up').toggleClass('fa-angle-up fa-angle-down');   
    $(this).siblings().next('.Vnav').hide();
    $("nav.Vsub").hide();
  });
  $(".Vnav>a").click(function(){
    $(".Vnav>.active").removeClass("active"); 
    $(this).addClass("active");
    $(this).siblings().find('i.fa-angle-up').toggleClass('fa-angle-up fa-angle-down'); 
    $(this).siblings().next('.Vsub').hide();
  });
  $(".Vsub-icon").click(function(){ 
    $(this).children().toggleClass('fa-angle-up fa-angle-down');
    $(this).next().toggle();
  });  
  $(".Vsub>a").click(function(){
    $(".Vsub>.active").removeClass("active"); 
    $(this).addClass("active");
  });
}); 
 
