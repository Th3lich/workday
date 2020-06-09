/**
 * Created by Javi on 08/06/2020.
 */

$(function() {
    /* Clients list carousel */
    var $clientcarousel = $('#clients-list');
    var clients = $clientcarousel.children().length;
    var clientwidth = (clients * 220); // 140px width for each client item
    $clientcarousel.css('width', clientwidth);

    var rotating = true;
    var clientspeed = 0;
    var seeclients = setInterval(rotateClients, clientspeed);

    $(document).on({
        mouseenter: function () {
            rotating = false; // turn off rotation when hovering
        },
        mouseleave: function () {
            rotating = true;
        }
    }, '#clients');

    function rotateClients() {
        if (rotating != false) {
            var $first = $('#clients-list li:first');
            $first.animate({'margin-left': '-220px'}, 5000, "linear", function () {
                $first.remove().css({'margin-left': '0px'});
                $('#clients-list li:last').after($first);
            });
        }
    }

    $('.counter').each(function () {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 2800,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

    /* Menu JS */
	$('.navbar-nav a').on('click', function(e){
		if($(this).attr('href') != "/") {
			var anchor = $(this).attr('href').split("/");
			$('html, body').stop().animate({
				scrollTop: $(anchor[anchor.length - 1]).offset().top - 50
			}, 1500);
			e.preventDefault();
		}
	});


    /* Go To Top */
	$(function(){
		//Scroll event
		$(window).on('scroll', function(){
			var scrolled = $(window).scrollTop();
			if (scrolled > 300) $('.go-top').fadeIn('slow');
			if (scrolled < 300) $('.go-top').fadeOut('slow');
		});
		//Click event
		$('.go-top').on('click', function() {
			$("html, body").animate({ scrollTop: "0" },  1000);
		});
	});


});