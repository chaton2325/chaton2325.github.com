document.addEventListener("DOMContentLoaded", function() {
    let images = document.querySelectorAll('.une-div img');
    let currentIndex = 0;

    function showNextImage() {
        images[currentIndex].style.display = 'none';
        currentIndex = (currentIndex + 1) % images.length;
        images[currentIndex].style.display = 'block';
    }

    // Initial setup: hide all images except the first one
    images.forEach((img, index) => {
        if (index !== 0) img.style.display = 'none';
    });

    // Change image every 3 seconds
    setInterval(showNextImage, 1500);
});

document.getElementById('menu-toggle').addEventListener('click', function() {
    var drawerMenu = document.getElementById('drawer-menu');
    drawerMenu.classList.toggle('active');
});

//Changer la coleur du header pendant le scroll
window.addEventListener('scroll', function() {
    const header = document.getElementById('header');
    const ecrit=document.getElementById('')
    if (window.scrollY > 50) { // Adjust the scroll distance as needed
        header.style.backgroundColor = 'background-color:rgb(114, 113, 113)'; // New color when scrolling
    } else {
        header.style.backgroundColor = 'rgba(245, 245, 245, 0.2)'; // Original color
    }
});


