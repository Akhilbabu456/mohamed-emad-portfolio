/* Elexer Theme Scripts */

(function($){ "use strict";
             
    $(window).on('load', function() {
        $('body').addClass('loaded');
    });

/*=========================================================================
    Header
=========================================================================*/        
    $('#toggle').click(function() {
        $(this).toggleClass('active');
        $('#overlay').toggleClass('open');
        $('.header-section').toggleClass('menu-active');
    });

/*=========================================================================
    Main Slider
=========================================================================*/
    $('.main-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        autoplay: true,
        items: 1,
        animateIn: "fadeIn",
        animateOut: "fadeOut"
    });        
        
/*=========================================================================
    Isotope Active
=========================================================================*/
    function galleryFilter(){
        
    }

	// Initialize Isotope immediately so we don't wait for imagesLoaded which can stall
    var $grid = $(".gallery-items").isotope({
        itemSelector: '.single-item',
        layoutMode: 'masonry',
    });

	$('.gallery-items').imagesLoaded( function() {
		 // Add isotope click function
		$('.gallery-filter li').on( 'click', function(){
	        $(".gallery-filter li").removeClass("active");
	        $(this).addClass("active");
	 
	        var selector = $(this).attr('data-filter');
	        $grid.isotope({
	            filter: selector,
	            animationOptions: {
	                duration: 750,
	                easing: 'linear',
	                queue: false,
	            }
	        });
	        return false;
	    });
        
        $grid.isotope('layout');

        // Recalculate Isotope layout when video metadata loads so they don't overlap
        $('video').each(function() {
            if (this.readyState >= 1) {
                setTimeout(function() { $('.gallery-items').isotope('layout'); }, 200);
            } else {
                $(this).on('loadedmetadata', function() {
                    $('.gallery-items').isotope('layout');
                });
            }
        });
	});

    // Load More Portfolios
    $('.loadmore-items').loadMoreResults({
        tag: {
            name: 'div',
            'class': 'single-item'
        },
        displayedItems: 8,
        showItems: 2,
        button: {
            text: 'Load More Photographs'
        }
    });

/*=========================================================================
    Active venobox
=========================================================================*/
	$('.img-popup').venobox({
		numeratio: true,
		infinigall: true
	});              
                          
/*=========================================================================
	Counter Up Active
=========================================================================*/
	var counterSelector = $('.counter');
	counterSelector.counterUp({
		delay: 10,
		time: 1000
	});
        
/*=========================================================================
    Testimonial Carousel
=========================================================================*/
	$('#testimonial-carousel').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 500,
        items: 1,
        nav: false
    });

/*=========================================================================
	Initialize smoothscroll plugin
=========================================================================*/
	smoothScroll.init({
		offset: 60
	});
        
/*=========================================================================
    Instagram Feed
=========================================================================*/
    var feed = new Instafeed({
        get: 'user',
        clientId: 'b84a5448343245f88dd43e62ba0cc9a8',
        accessToken: '4793566378.1677ed0.69bb8075ace04a73bdbe1cb83b9026b1',
        userId: '4793566378',
        limit: 8,
        resolution: 'low_resolution',
        template: '<a href="{{link}}" target="_blank"><img src="{{image}}" /></a>'
    });
    feed.run();

/*=========================================================================
	Scroll To Top
=========================================================================*/ 
    $(window).on( 'scroll', function () {
        if ($(this).scrollTop() > 100) {
            $('#scroll-to-top').fadeIn();
        } else {
            $('#scroll-to-top').fadeOut();
        }
    });

/*=========================================================================
    Autoplay Video on Scroll
=========================================================================*/
    if ('IntersectionObserver' in window) {
        var videoObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting && entry.target.paused) {
                    entry.target.play();
                } else if (!entry.isIntersecting && !entry.target.paused) {
                    entry.target.pause();
                }
            });
        }, { threshold: 0.5 });

        $('.autoplay-on-scroll').each(function() {
            videoObserver.observe(this);
        });
    }

})(jQuery);
