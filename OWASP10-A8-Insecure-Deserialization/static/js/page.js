$(document).ready(function(){
    var hmenu = 56; // height of the fixed menu
    var stoptransparency = 200; // when stop the transparency menu
    $(this).scrollTop(0);
	$(window).scroll(function() {
		// navbar
		var position = $(this).scrollTop();
		if(position > stoptransparency) {
			$('header .navbar').removeClass('transparency');
		} else {
			$('header .navbar').addClass('transparency');
		}
		// active
		$('.anchor').each(function() {
			var target = $(this).offset().top-hmenu;
			var id = $(this).attr('id');
			if (position >= target) {
				$('.nav-link').removeClass('active').blur();
				$('.nav-link[href="#' + id + '"]').addClass('active');
			}
		});
	});
	// smooth scroll
	$('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(e) {
		e.preventDefault();
		var dest = $(this).attr('href');
        $('.nav-link').removeClass('active');
		$('html,body').animate({ scrollTop: $(dest).offset().top-hmenu }, 600);
		$('.navbar-collapse').removeClass('show');
		$('.navbar-toggler').addClass('collapsed');
	});
});