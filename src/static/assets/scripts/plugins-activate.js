(function($jq) {
  $jq(document).ready(function() {
    // Closes the sidebar menu
    $jq(".menu-toggle").click(function(e) {
      e.preventDefault();
      $jq("#sidebar-wrapper").toggleClass("active");
      $jq(".menu-toggle > .fa-bars, .menu-toggle > .fa-times").toggleClass("fa-bars fa-times");
      $jq(this).toggleClass("active");
    });
    // Smoothscroll script
    $jq(".smooth-scroll").click(function(e) {
      e.preventDefault();
      var dis = $jq(this),
        target = dis.attr("href"),
        offset = parseInt($jq(target).offset().top),
        header = $jq(".sidebar-nav");
      dis.addClass("active").parent().siblings().find(".smooth-scroll").removeClass("active");
      $jq('html,body').stop().animate({ scrollTop: offset }, 200);
      $jq(".menu-toggle").trigger("click");
    });
    // Closes responsive menu when a scroll trigger link is clicked
    $jq('#sidebar-wrapper .js-scroll-trigger').click(function() {
      $jq("#sidebar-wrapper").removeClass("active");
      $jq(".menu-toggle").removeClass("active");
      $jq(".menu-toggle > .fa-bars, .menu-toggle > .fa-times").toggleClass("fa-bars fa-times");
    });
    //  TESTIMONIALS CAROUSEL HOOK
    var owl = $jq('#customers-testimonials');
    owl.owlCarousel({
      loop: true,
      center: true,
      items: 3,
      margin: 0,
      autoplay: true,
      dots: true,
      autoplayTimeout: 8500,
      smartSpeed: 450,
      responsive: {
        0: {
          items: 1
        },
        768: {
          items: 2
        },
        1170: {
          items: 3
        }
      },
      navigation: true,
      navigationText: true
    });
  });
})(jQuery)