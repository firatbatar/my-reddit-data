function setColorMode() {
    let colorMode = localStorage.getItem('colorMode');
    $('html').removeClass();  // Remove all classes from the html tag
    $('html').addClass(colorMode);
    $('html').attr('data-bs-theme', colorMode);
}


if (!localStorage.getItem('colorMode')) {
    localStorage.setItem('colorMode', 'light');
}

$(document).ready(() => {
    setColorMode();
    $('#color-mode-toggle-btn').click(() => {
        // Change the color mode
        if (localStorage.getItem('colorMode') === 'light') {
            localStorage.setItem('colorMode', 'dark');
        } else {
            localStorage.setItem('colorMode', 'light');
        }

        setColorMode();
    });

    $('#color-mode-toggle-btn-sb').click(() => {
        console.log('clicked');
        // Change the color mode
        if (localStorage.getItem('colorMode') === 'light') {
            localStorage.setItem('colorMode', 'dark');
        } else {
            localStorage.setItem('colorMode', 'light');
        }

        setColorMode();
    });
});