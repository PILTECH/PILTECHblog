document.addEventListener('DOMContentLoaded', () => {
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.querySelector('.lightbox-content');
    const closeBtn = document.querySelector('.lightbox-close');

    // Kliknięcie na każdy obrazek w galerii
    document.querySelectorAll('.img-wrapper img').forEach(img => {
        img.addEventListener('click', () => {
            lightbox.style.display = 'flex';
            lightboxImg.src = img.src;
        });
    });

    // Zamknięcie lightboxa
    closeBtn.addEventListener('click', () => {
        lightbox.style.display = 'none';
    });

    // Kliknięcie poza obrazek zamyka lightbox
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
            lightbox.style.display = 'none';
        }
    });
});

function setPostHeight() {
    const posts = document.querySelectorAll('.post');
    const vh = window.innerHeight;
    posts.forEach(post => {
        if(window.innerWidth <= 600){
            post.style.height = `${vh}px`;
        } else {
            post.style.height = 'auto';
        }
    });
}
window.addEventListener('load', setPostHeight);
window.addEventListener('resize', setPostHeight);
window.addEventListener('orientationchange', setPostHeight);
