// RWD MENU

var ww = document.body.clientWidth;

$(document).ready(function() {
  $(".nav li a").each(function() {
    if ($(this).next().length > 0) {
      $(this).addClass("parent");
    };
  })
  
  $(".toggleMenu").click(function(e) {
    e.preventDefault();
    $(this).toggleClass("active");
    $(".nav").toggle();
  });
  adjustMenu();
})

$(window).bind('resize orientationchange', function() {
  ww = document.body.clientWidth;
  adjustMenu();
});

var adjustMenu = function() {
  if (ww < 820) {
    // if "more" link not in DOM, add it
    if (!$(".more")[0]) {
    $('<div class="more">&nbsp;</div>').insertBefore($('.parent')); 
    }
    $(".toggleMenu").css("display", "inline-block");
    if (!$(".toggleMenu").hasClass("active")) {
      $(".nav").hide();
    } else {
      $(".nav").show();
    }
    $(".nav li").unbind('mouseenter mouseleave');
    $(".nav li a.parent").unbind('click');
    $(".nav li .more").unbind('click').bind('click', function() {
      
      $(this).parent("li").toggleClass("hover");
    });
  } 
  else if (ww >= 820) {
    // remove .more link in desktop view
    $('.more').remove(); 
    $(".toggleMenu").css("display", "none");
    $(".nav").show();
    $(".nav li").removeClass("hover");
    $(".nav li a").unbind('click');
    $(".nav li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function() {
      // must be attached to li so that mouseleave is not triggered when hover over submenu
      $(this).toggleClass('hover');
    });
  }
}



var navButton = document.querySelector(".nav-button");
navButton.addEventListener("click", function (e) {
e.preventDefault();
document.body.classList.toggle("nav-visible");
});

var navButton = document.querySelector(".nav-buttons");
navButton.addEventListener("click", function (e) {
e.preventDefault();
document.body.classList.toggle("nav-visible");
});

$(document).ready(function ($) {
    $(".nav-wrapper .menu-item-has-children").click(function () {
        $("ul", this).slideToggle();
		$(this).closest('.menu-item-has-children').toggleClass("minus");

    });
});


$(document).ready(function(){
  $('.hero-slider').slick({
        dots: true,
        infinite: true,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 10000,
        slidesToScroll: 1
      });
  });


$(document).ready(function(){
  $('.info-slider').slick({
        dots: true,
        infinite: true,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 10000,
        slidesToScroll: 1
      });
  });

$(document).ready(function() {
    $(".accordian").click(function() {
        $(this).nextAll(".content:first").slideToggle("fast");
        $(this).toggleClass("less");
    });
});


$(document).ready(function(){$("iframe").wrap("<div class='whoframed'/>"),$(".whoframed").css("position","relative"),$(".whoframed").css("padding-bottom","56.25%"),$(".whoframed").css("padding-top","25px"),$(".whoframed").css("height","0"),$(".whoframed iframe").css("position","absolute"),$(".whoframed iframe").css("top","0"),$(".whoframed iframe").css("left","0"),$(".whoframed iframe").css("width","100%"),$(".whoframed iframe").css("height","100%")});


