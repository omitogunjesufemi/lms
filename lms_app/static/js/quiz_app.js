
let quiz_container = document.getElementById('quiz');
let submit_button = document.getElementById('submit_test');
let curr_qns = document.getElementById('current_question');
let current_qns = document.getElementById('current_qns');

let previous_button = document.getElementById('previous');
let next_button = document.getElementById('next');


let querystring = window.location.pathname.split('/');

let host = window.location.host

let param = querystring[3]

//Fetching from API
 // fetch(`http://${host}/question/qns_api/${param}`, {
 //        method: "GET",
 //        headers: {"Content-type": "application/json; charset=UTF-8"},
 //    })
 //    .then(response => response.json())
 //    .then(function (json){
 //
 //        var html_output = [];
 //
 //        json.forEach(
 //            function (current_question, question_number) {
 //                let choices = [];
 //                choices.push(
 //                    `
 //                    <div>
 //                        <label>
 //                            A: <input type="radio" name="${current_question.id}" value="choice1"> ${current_question.choice1}
 //                        </label>
 //                    </div>
 //                    <div>
 //                        <label>
 //                            B: <input type="radio" name="${current_question.id}" value="choice2"> ${current_question.choice2}
 //                        </label>
 //                    </div>
 //                    <div>
 //                        <label>
 //                            C: <input type="radio" name="${current_question.id}" value="choice3"> ${current_question.choice3}
 //                        </label>
 //                    </div>
 //                    <div>
 //                        <label>
 //                            D: <input type="radio" name="${current_question.id}" value="choice4"> ${current_question.choice4}
 //                        </label>
 //                    </div>
 //
 //                `
 //                );
 //
 //                html_output.push(
 //                    `<div class="slide" id="${question_number+1}">
 //                         <div class="text-center"><span id="qns__">${question_number+1}</span>.  ${current_question.question_title}</div>
 //                         <div class="text-center font-weight-light">${current_question.question_content}</div>
 //
 //                         <div class="mt-3" style="font-size: 14pt;">${choices}</div>
 //                    </div>`
 //                );
 //                console.log(html_output)
 //            }
 //        );
 //
 //        quiz_container.innerHTML = html_output.join('');
 //    })
 //    .catch(err => console.log('Request Failed', err));



//Pagination
// let slide__ = document.childNodes;
// let slides = slide__[1].childNodes[2].childNodes[5].childNodes[1].childNodes[1].childNodes[1].childNodes[1].childNodes[1].childNodes[3].childNodes

let slides = document.querySelectorAll(".slide");

let current_slide = 0;

function showSlide(n){
    slides[current_slide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    current_slide = n;

    if (current_slide === 0) {
        current_qns.innerText = n+1;
        previous_button.disabled = true;
        previous_button.classList.remove("btn-outline-success");
        previous_button.classList.add("btn-outline-secondary");
    }
    else {
        previous_button.disabled = false;
        current_qns.innerText = n+1;
        previous_button.classList.remove("btn-outline-secondary");
        previous_button.classList.add("btn-outline-success");
    }

    if (current_slide === slides.length-1){
        next_button.disabled = true;
        current_qns.innerText = n+1;
        current_qns.classList.remove("text-danger");
        current_qns.classList.add("text-success");
        next_button.classList.remove("btn-outline-success");
        next_button.classList.add("btn-outline-secondary");
        submit_button.hidden = false;
    }
    else {
        next_button.disabled = false;
        current_qns.innerText = n+1;
        next_button.classList.remove("btn-outline-secondary");
        next_button.classList.add("btn-outline-success");
        submit_button.hidden = true;
    }
}

showSlide(current_slide);

function show_next_slide(){
        showSlide(current_slide+1);
    }

function show_prev_slide(){
        showSlide(current_slide-1);
        current_qns.classList.remove("text-success")
        current_qns.classList.add("text-danger")
    }

    previous_button.addEventListener('click', show_prev_slide);
    next_button.addEventListener('click', show_next_slide );








