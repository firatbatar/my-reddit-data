let carouselWidth = $(".carousel-inner")[0].scrollWidth;
let cardWidth = $(".carousel-item").width();
let scrollPosition = 0;
let multipleCardCarousel = document.querySelector("#projectsCarousel");

// Make the first card active
let firstCard = $(".carousel-item")[0];
$(firstCard).addClass("active");

$(".carousel-control-next").on("click", function () {
    if (scrollPosition < carouselWidth - cardWidth * 4) {
        //check if you can go any further
        scrollPosition += cardWidth; //update scroll position
        $(".carousel-inner").animate({ scrollLeft: scrollPosition }, 600); //scroll left
    }
});

$(".carousel-control-prev").on("click", function () {
    if (scrollPosition > 0) {
        scrollPosition -= cardWidth;
        $(".carousel-inner").animate({ scrollLeft: scrollPosition }, 600);
    }
});

if (window.matchMedia("(min-width: 1100px)").matches) {
    var carousel = new bootstrap.Carousel(multipleCardCarousel, {
        interval: false,
        wrap: false,
    });
} else {
    $(multipleCardCarousel).addClass("slide");
}
