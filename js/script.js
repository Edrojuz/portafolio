// Scroll suave adicional para navegación
function smoothScroll(target){
$('html, body').animate({ scrollTop: $(target).offset().top - 60 }, 600);
}


$('.nav-link').on('click', function(){
    $('.navbar-collapse').collapse('hide');
});


console.log("script.js cargado correctamente");