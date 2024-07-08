
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



// document.addEventListener('DOMContentLoaded', function() {
//     const editProfileBtn = document.querySelector('.edit-profile-btn');
//     const editProfileForm = document.getElementById('edit-profile-form');
    
//     editProfileForm.style.display = 'none';
    
//     editProfileBtn.addEventListener('click', function() {
//         editProfileForm.style.display = editProfileForm.style.display === 'none' ? 'block' : 'none';
//     });
// });

// document.addEventListener('DOMContentLoaded', function() {
//     const editProfileBtn = document.querySelector('.edit-profile-btn');
//     const editProfileForm = document.getElementById('edit-profile-form');
//     const addAddressBtn = document.querySelector('.add-address-btn');
//     const addAddressSection = document.getElementById('add-address-section');

//     // Hide the forms initially
//     editProfileForm.style.display = 'none';
//     addAddressSection.style.display = 'none';

//     // Toggle the edit profile form visibility
//     editProfileBtn.addEventListener('click', function() {
//         if (editProfileForm.style.display === 'none') {
//             editProfileForm.style.display = 'block';
//         } else {
//             editProfileForm.style.display = 'none';
//         }
//     });

//     // Toggle the add address form visibility
//     addAddressBtn.addEventListener('click', function() {
//         if (addAddressSection.style.display === 'none') {
//             addAddressSection.style.display = 'block';
//         } else {
//             addAddressSection.style.display = 'none';
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const editProfileBtn = document.querySelector('.edit-profile-btn');
    const editProfileForm = document.getElementById('edit-profile-form');
    const addAddressBtn = document.querySelector('.add-address-form-btn');
    const addAddressForm = document.getElementById('add-address-form');

    // Hide the forms initially
    editProfileForm.style.display = 'none';
    addAddressForm.style.display = 'none';

    // Toggle the visibility of an element
    function toggleVisibility(element) {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }

    // Attach event listeners
    editProfileBtn.addEventListener('click', function() {
        toggleVisibility(editProfileForm);
    });

    addAddressBtn.addEventListener('click', function() {
        toggleVisibility(addAddressForm);
    });
});


