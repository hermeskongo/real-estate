"use-strict";


/**
 * Ajoute un écouteur d'événement à un ou plusieurs éléments.
 *
 * @param {HTMLElement|NodeList} element - L'élément ou la liste d'éléments auxquels ajouter l'écouteur d'événement.
 * @param {string} type - Le type d'événement à écouter (par exemple, 'click', 'mouseover').
 * @param {Function} listener - La fonction à exécuter lorsque l'événement est déclenché.
 */
const addEventOnElement = (element, type, listener) => {
    if(element instanceof NodeList) {
        element.forEach(el => {
            el.addEventListener(type, listener);
        });
    }else {
        element.addEventListener(type, listener);
    }
}


const navbar = document.querySelector('.navbar');
const navbarToggler = document.querySelector('.navbar_toggle');
const navbarItems = document.querySelectorAll('.nav-item');

const toggleNavbar = function () {
    navbar.classList.toggle('active')
    this.classList.toggle('active')
};

console.log(navbarToggler);
console.log(navbar);

const removeNavbar = function () {
    navbar.classList.remove('active')
    navbarToggler.classList.remove('active')
};

addEventOnElement(navbarToggler, 'click', toggleNavbar);
addEventOnElement(navbarItems, 'click', removeNavbar);


/**
 * Ajout d'un écouteur d'événement pour le scroll.
 * 
 */

const header = document.querySelector('[data-header]');
const topBtn = document.querySelector('.back-to-top');

window.addEventListener('scroll', () => {
    if(window.scrollY >= 1000) {
        header.classList.add('active');
        topBtn.classList.add('active');
    } else {
        header.classList.remove('active');
        topBtn.classList.remove('active');
    }
})


const phoneInputField = document.querySelector("#id_phone_number");
const phoneInput = window.intlTelInput(phoneInputField, {
    preferredCountries: ["bf", "fr"],
    separateDialCode: true,
    utilsScript: "https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/utils.js",
});

const all_success = document.querySelectorAll('.alert-success');

all_success.forEach(success =>{
    if(success) {
        setTimeout(() => {
            success.style.display = 'none'
        }, 4500)
    }
})

  // <!-- Initialize Swiper -->
    const swiper = new Swiper(".mySwiper", {
      cssMode: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
      },
      mousewheel: true,
      keyboard: true,
    });