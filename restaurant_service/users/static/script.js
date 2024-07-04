
let menus = document.querySelector("nav")
let menuBtn = document.querySelector(".menu-btn")
let closeBtn = document.querySelector(".close-btn")

menuBtn.addEventListener("click",function(){
    menus.classList.add("active");;
})

closeBtn.addEventListener("click",function(){
    menus.classList.remove("active");;
})

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
