document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('divSetting');
    const menuModal = document.getElementById('menuModal');
    const closeMenu = document.querySelector('#menuModal .close');

    menuIcon.addEventListener('click', function() {
        menuModal.classList.add('show');
    });

    closeMenu.addEventListener('click', function() {
        menuModal.classList.remove('show');
    });

    window.addEventListener('click', function(event) {
        if (event.target === menuModal) {
            menuModal.classList.remove('show');
        }
    });
});