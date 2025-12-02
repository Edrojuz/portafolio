// Animación navbar al cargar
$(document).ready(function(){
$("nav").hide().fadeIn(800);
});


// Animaciones al hacer scroll
const observer = new IntersectionObserver(entries =>{
entries.forEach(entry =>{
if(entry.isIntersecting){ entry.target.classList.add('visible'); }
})
}, {threshold:0.2});


document.querySelectorAll('.scroll-anim').forEach(el => observer.observe(el));