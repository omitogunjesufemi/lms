let quiz_container = document.getElementById('question_body');
let question_counts = document.getElementById('question_count');

let host = window.location.host
//Fetching from API

function tutor_questions(){
    fetch(`http://${host}/question/tutor_qns_api`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){

            var output = []
            output.push(
                `${json.length}`
            )

            var html_output = [];

            json.forEach(
                function (current_question, question_number) {

                    html_output.push(
                        `<tr>
                                    <td>${question_number + 1}</td>
                                    <td>${current_question.question_title}</td>
                                    <td>${current_question.answer}</td>
                                    <td>${current_question.assigned_mark}</td>
                                    <td>
                                        <div class="btn-group">
                                            <a href="details/${current_question.id}" class="btn btn-success btn-sm">Details</a>
                                        </div>
                                    </td>
                                </tr>`
                    );

                }
            );

            quiz_container.innerHTML = html_output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

function question_count(){
   fetch(`http://${host}/question/tutor_qns_api`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){

            var output = []
            output.push(
                `${json.length}`
            )
            question_counts.innerHTML = output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

tutor_questions();
question_count();

function refresh_questions(){
    tutor_questions();
}