
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



document.addEventListener('DOMContentLoaded', function() {
    const editProfileBtn = document.querySelector('.edit-profile-btn');
    const editProfileForm = document.getElementById('edit-profile-form');
    const addAddressBtn = document.querySelector('.add-address-btn');
    const addAddressForm = document.getElementById('add-address-form');
    const ShowBillFormBtn = document.querySelector('.confirm-order-btn');
    const BillForm = document.getElementById('BillForm');

    // Hide the forms initially if they exist
    if (editProfileForm) editProfileForm.style.display = 'none';
    if (addAddressForm) addAddressForm.style.display = 'none';
    if (BillForm) BillForm.style.display = 'none';

    // Toggle the visibility of an element
    function toggleVisibility(element) {
        if (element) {
            element.style.display = element.style.display === 'none' ? 'block' : 'none';
        }
    }

    function toggleVisibilityFlex(element) {
        if (element) {
            element.style.display = element.style.display === 'none' ? 'flex' : 'none';
        }
    }
    // Attach event listeners if the buttons exist
    if (editProfileBtn) {
        editProfileBtn.addEventListener('click', function() {
            toggleVisibility(editProfileForm);
        });
    }

    if (addAddressBtn) {
        addAddressBtn.addEventListener('click', function() {
            toggleVisibility(addAddressForm);
        });
    }

    if (ShowBillFormBtn) {
        ShowBillFormBtn.addEventListener('click', function() {
            toggleVisibilityFlex(BillForm);
        });
    }
});
