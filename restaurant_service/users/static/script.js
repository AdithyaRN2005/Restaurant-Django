document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.btn-cat');
    const currentPath = window.location.pathname;

    buttons.forEach(button => {
        const buttonPath = new URL(button.href).pathname;
        if (buttonPath === currentPath) {
            button.classList.add('active_btn');
        } else {
            button.classList.remove('active_btn');
        }
    });
});
