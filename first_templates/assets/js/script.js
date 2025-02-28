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
