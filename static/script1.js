$(document).ready(function(){
  $(window).scroll(function(){
  	var scroll = $(window).scrollTop();
	  if (scroll > 100) {
	    $(".black").css("background" , "green");
	  }

	  // else{
		//   $(".black").css("background" , "#333");
	  // }
  })
})
