
let quiz_container = document.getElementById('quiz')
let submit_button = document.getElementById('submit')
let curr_qns = document.getElementById('current_question')

let querystring = window.location.pathname.split('/');

let host = window.location.host

let param = querystring[3]

let questions_pack = fetch(`http://${host}/question/qns_api/${param}`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
    .then(response => response.json())
    .then(function (json){

        let html_output = [];

        json.forEach(
            function (current_question, question_number) {
                let choices = [];
                choices.push(
                    `
                    <div>
                        <label>
                            A: <input type="radio" name="${current_question.id}" value="choice1"> ${current_question.choice1}
                        </label>
                    </div>
                    <div>
                        <label>
                            B: <input type="radio" name="${current_question.id}" value="choice2"> ${current_question.choice2}
                        </label>
                    </div>
                    <div>
                        <label>
                            C: <input type="radio" name="${current_question.id}" value="choice3"> ${current_question.choice3}
                        </label>
                    </div>
                    <div>
                        <label>
                            D: <input type="radio" name="${current_question.id}" value="choice4"> ${current_question.choice4}
                        </label>
                    </div>
                
                `
                );

                html_output.push(
                    `<div class="slide">
                         <div class="question text-center">${question_number+1}.  ${current_question.question_title}</div>
                         <div class="question text-center font-weight-light">${current_question.question_content}</div>
                         
                         <div class="question mt-3" style="font-size: 14pt;">${choices}</div>
                    </div>
                <br>
                    
                `
                );
            }
        );

        quiz_container.innerHTML = html_output.join('');

    })
    .catch(err => console.log('Request Failed', err));


submit_button.addEventListener('click')






