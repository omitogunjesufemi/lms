let prev_button = document.getElementById('prev');
let nxt_button = document.getElementById('nxt');

let sliders = document.querySelectorAll(".slides");

let current_slider = 0;

function showSlides(n){
    sliders[current_slider].classList.remove('active-slide');
    sliders[n].classList.add('active-slide');
    current_slider = n;

    if (current_slider === 0) {
        prev_button.disabled = true;
        prev_button.classList.remove("btn-outline-success");
        prev_button.classList.add("btn-outline-secondary");
    }
    else {
        prev_button.disabled = false;
        prev_button.classList.remove("btn-outline-secondary");
        prev_button.classList.add("btn-outline-success");
    }

    if (current_slider === sliders.length-1){
        nxt_button.disabled = true;
        nxt_button.classList.remove("btn-outline-success");
        nxt_button.classList.add("btn-outline-secondary");
    }
    else {
        nxt_button.disabled = false;
        nxt_button.classList.remove("btn-outline-secondary");
        nxt_button.classList.add("btn-outline-success");
    }
}

showSlides(current_slider);

function show_next_slides(){
    showSlides(current_slider+1);
}

function show_prev_slides(){
    showSlides(current_slider-1);
}

prev_button.addEventListener('click', show_prev_slides);
nxt_button.addEventListener('click', show_next_slides );








