var goToTop = function() {

    $('.js-gotop').on('click', function(event){

        event.preventDefault();

        $('html, body').animate({
            scrollTop: $('html').offset().top
        }, 500);

        return false;
    });

    $(window).scroll(function(){

        var $win = $(window);
        if ($win.scrollTop() > 200) {
            $('.js-top').addClass('active');
        } else {
            $('.js-top').removeClass('active');
        }

    });
};


var accordion = function() {
    $('.gtco-accordion-heading').on('click', function(event){

        var $this = $(this);

        $this.closest('.gtco-accordion').find('.gtco-accordion-content').slideToggle(400);
        if ($this.closest('.gtco-accordion').hasClass('active')) {
            $this.closest('.gtco-accordion').removeClass('active');
        } else {
            $this.closest('.gtco-accordion').addClass('active');
        }
        event.preventDefault();
    });
};

jQuery(function($) {'use strict';
    goToTop();
    accordion();
    //Responsive Nav
    $('li').find('.fa-angle-down').each(function(){
        $(this).on('click', function(){
            if( $(window).width() < 768 ) {
                $(this).parent().next().slideToggle();
            }
            return false;
        });
    });

    //Fit Vids
    if( $('#video-container').length ) {
        $("#video-container").fitVids();
    }

    //Initiat WOW JS
    new WOW().init();

    // portfolio filter
    $(window).load(function(){

        $('.main-slider').addClass('animate-in');
        $('.preloader').remove();
        //End Preloader

        if( $('.masonery_area').length ) {
            $('.masonery_area').masonry();//Masonry
        }

        var $portfolio_selectors = $('.portfolio-filter >li>a');

        if($portfolio_selectors.length) {

            var $portfolio = $('.portfolio-items');
            $portfolio.isotope({
                itemSelector : '.portfolio-item',
                layoutMode : 'fitRows'
            });

            $portfolio_selectors.on('click', function(){
                $portfolio_selectors.removeClass('active');
                $(this).addClass('active');
                var selector = $(this).attr('data-filter');
                $portfolio.isotope({ filter: selector });
                return false;
            });
        }

    });


    $('.timer').each(count);
    function count(options) {
        var $this = $(this);
        options = $.extend({}, options || {}, $this.data('countToOptions') || {});
        $this.countTo(options);
    }

    // Search
    $('.fa-search').on('click', function() {
        $('.field-toggle').fadeToggle(200);
    });

    // Contact form
    // var form = $('#main-contact-form');
    // form.submit(function(event){
    //
    //     var form_status = $('<div class="form_status"></div>');
    //     $.ajax({
    //         url: $(this).attr('action'),
    //         beforeSend: function(){
    //             form.prepend( form_status.html('<p><i class="fa fa-spinner fa-spin"></i> Email is sending...</p>').fadeIn() );
    //         }
    //     }).done(function(data){
    //         data=JSON.parse(data);
    //         if(data.status="200") {
    //             form_status.html('<p class="text-success">Thank you for contact us. As early as possible  we will contact you</p>').delay(3000).fadeOut();
    //         }
    //         if (data.status == "500")
    //         {
    //             form_status.html('<p class="text-success">sry you for contact us. As early as possible  we will contact you</p>').delay(3000).fadeOut();
    //         }
    //     });
    //
    //     // event.preventDefault();
    // });

    // Progress Bar
    $.each($('div.progress-bar'),function(){
        $(this).css('width', $(this).attr('data-transition')+'%');
    });

    if( $('#gmap').length ) {
        var map;

        map = new GMaps({
            el: '#gmap',
            lat: 43.04446,
            lng: -76.130791,
            scrollwheel:false,
            zoom: 16,
            zoomControl : false,
            panControl : false,
            streetViewControl : false,
            mapTypeControl: false,
            overviewMapControl: false,
            clickable: false
        });

        map.addMarker({
            lat: 43.04446,
            lng: -76.130791,
            animation: google.maps.Animation.DROP,
            verticalAlign: 'bottom',
            horizontalAlign: 'center',
            backgroundColor: '#3e8bff',
        });
    }

});