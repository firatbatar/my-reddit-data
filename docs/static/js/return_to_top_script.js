const returnToTop_btn = $("#return_to_top_btn");

function scroll_to_top() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function checkScroll() {
    if (document.documentElement.scrollTop >= 150 || document.body.scrollTop >= 150) {
        returnToTop_btn.css("display", "block");
    } else {
        returnToTop_btn.css("display", "none");
    }
}

if (returnToTop_btn) {
    returnToTop_btn.click(() => {
        $(window).scrollTop(0);
    })
}
window.addEventListener("scroll", checkScroll);