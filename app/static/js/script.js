/*

Javascript - MobThon

Aqui ficará concentrado todo código referente ao JAVASCRIPT do código. é uma linguagem de programação interpretada 
de alto nível, caracterizada também, como dinâmica, fracamente tipada, prototype-based e multi-paradigma. Juntamente 
com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web.

*/ 
var menu = document.querySelector('header nav');
(function () {
    window.addEventListener('scroll', function () {
        if (window.scrollY > 0) menu.classList.add('menuScroll');
        else menu.classList.remove('menuScroll');s
    });
})();

console.log("Hello world!");