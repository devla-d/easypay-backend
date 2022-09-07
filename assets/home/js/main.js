(function($) {
    'use strict';



    /*---------------------------------------
       PORTFOLIO IMAGE LODED WITH MASONRY
    -----------------------------------------*/
    var $PortfolioMasonry = $('.portfolio-masonry');
    if (typeof imagesLoaded === 'function') {
        imagesLoaded($PortfolioMasonry, function() {
            setTimeout(function() {
                $PortfolioMasonry.isotope({
                    itemSelector: '.portfolio-item',
                    resizesContainer: false,
                    layoutMode: 'masonry',
                    filter: '*'
                });
            }, 500);

        });
    };

    /*-------------------------------------------
       SET ACTIVE CLASS FOR PORTFOLIO FILTER
    ---------------------------------------------*/
    $('.portfolio-filter li').on('click', function(event) {
        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();
    });

    /*--------------------------------
       FILTER JS FOR PORRTFOLIO
    -----------------------------------*/
    $('.portfolio-filter').on('click', 'li', function() {
        var filterValue = $(this).attr('data-filter');
        $PortfolioMasonry.isotope({ filter: filterValue });
    });


    /*--------------------------------
       VENOBOX GALLARY IMAGE VIEW
    -----------------------------------*/
    $('.venobox').venobox();



    /*--------------------------------
        WOW JS
    -----------------------------------*/
    new WOW().init();

    /*----------------------------------
    COUNTUP JS ACTIVE 
    ------------------------------------*/
    $('.counter').counterUp({
        delay: 10,
        time: 1500
    });

    /*----------------------------------
    TESTIMONIAL SLIDER
    ------------------------------------*/
    $('.testimonial-wrapper').slick({
        dots: true,
        infinite: true,
        speed: 300,
        arrows: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true
    });


    $('.client-wrapper').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 6,
        slidesToScroll: 4,
        autoplay: true,
        responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 5,
                    slidesToScroll: 3,
                    infinite: true,
                    dots: true
                }
            }, {
                breakpoint: 768,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 2
                }
            }, {
                breakpoint: 460,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }, {
                breakpoint: 320,
                settings: { slidesToShow: 1, slidesToScroll: 1 }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });

// blog-slider
    $('.blog-wrapper-2').slick({
        dots: true,
        infinite: true,
        speed: 600,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        responsive: [{
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            }, {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            }, {
                breakpoint: 460,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }, {
                breakpoint: 320,
                settings: { slidesToShow: 1, slidesToScroll: 1 }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });


    /* parallax Active*/
    $.stellar({
        horizontalScrolling: false
    });


    // ONEPAGENAV NAV

    $('.main-menu').onePageNav();

    // Mainmenu JS
    jQuery('.mobile-menu').meanmenu();

    // HeadRoom JS
    $("#headroom-active").headroom({
        tolerance: 5
    });

    /* ---------------------------------------------
        3. Header sticky style.
    --------------------------------------------- */
    $(window).on('scroll', function() {
        var wSize = $(window).width();
        if (wSize > 1 && $(this).scrollTop() > 1) {
            $('#sticky-header').addClass('sticky');
        } else {
            $('#sticky-header').removeClass('sticky');
        }
    });

    /* ---------------------------------------------
     MENU HAMBURGER AND FULL SCREEN  OVERLAY.
    --------------------------------------------- */
    $('.hamburger').on('click', function() {
        $(this).toggleClass('is-active');
        $(this).next().toggleClass('nav-show')
    });
    $('.menu-button a').on('click', function() {
        $('.overlay').fadeToggle(300);
        $(this).toggleClass('btn-open').toggleClass('btn-close');
    });
    $('.overlay').on('click', function() {
        $('.menu-button').fadeToggle(300);
        $('.button a').toggleClass('btn-open').toggleClass('btn-close');
        open = false;
    });
    //Homepage one Slider Main Section

    $(".slider-wrapper").owlCarousel({
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        loop: true,
        navText: ["<i class='ti-angle-left'></i>", "<i class='ti-angle-right'></i>"],
        mouseDrag: false,
        touchDrag: false,
        animateOut: 'fadeOut'
    });
    //Homepage Three Slider Main Section

    $(".slider-wrapper-two").owlCarousel({
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        loop: true,
        navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
        mouseDrag: false,
        touchDrag: false,
        animateOut: 'fadeOut'
    });


    $(".slider-wrapper-2").owlCarousel({
        items: 1,
        nav: true,
        dots: false,
        autoplay: true,
        loop: true,
        navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
        mouseDrag: false,
        touchDrag: false,
        animateOut: 'slideOutDown',
        animateIn: 'flipInX'
    });


    // COMMING SOON COUNTDOWN
    $('[data-countdown]').each(function() {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function(event) {
            $this.html(event.strftime(
                '<div class="cdown"><span class="days"><strong>%-D</strong><p>Days</p></span></div><div class="cdown"><span class="hour"><strong> %-H</strong><p>Hours</p></span></div> <div class="cdown"><span class="minutes"><strong>%M</strong> <p>MINUTES</p></span></div><div class="cdown"><span class="second"><strong> %S</strong><p>SECONDS</p></span></div>'
            ));
        });
    });

    // BITCOIN STATICES
      (function(b,i,t,C,O,I,N) {
        window.addEventListener('load',function() {
          if(b.getElementById(C))return;
          I=b.createElement(i),N=b.getElementsByTagName(i)[0];
          I.src=t;I.id=C;N.parentNode.insertBefore(I, N);
        },false)
      })(document,'script','https://widgets.bitcoin.com/widget.js','btcwdgt');

 
    // Elements Animation
    if($('.wow').length){
        var wow = new WOW(
          {
            boxClass:     'wow',      // animated element css class (default is wow)
            animateClass: 'animated', // animation css class (default is animated)
            offset:       0,          // distance to the element when triggering the animation (default is 0)
            mobile:       true,       // trigger animations on mobile devices (default is true)
            live:         true       // act on asynchronously loaded content (default is true)
          }
        );
        wow.init();
    }


function stickyHeader () {
    if ($('.stricky').length) {
        var strickyScrollPos = 100;
        if($(window).scrollTop() > strickyScrollPos) {
            $('.stricky').removeClass('fadeIn animated');
            $('.stricky').addClass('stricky-fixed fadeInDown animated');
            $('.scroll-to-top').fadeIn(500);
        }
        else if($(this).scrollTop() <= strickyScrollPos) {
            $('.stricky').removeClass('stricky-fixed fadeInDown animated');
            $('.stricky').addClass('slideIn animated');
            $('.scroll-to-top').fadeOut(500);
        }
    };
}

// instance of fuction while Window Scroll event
$(window).on('scroll',function () { 
    (function ($) {
        stickyHeader();
    })(jQuery);
});


$(window).on('load',function(){
    
    var preLoder = $(".preloader");
    preLoder.fadeOut(1000);
    
});




})(jQuery);
