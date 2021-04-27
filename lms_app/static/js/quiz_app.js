
let quiz_container = document.getElementById('question_body');
let submission_container = document.getElementById('submission_body');

let host = window.location.host
//Fetching from API

function tutor_questions(){
    fetch(`http://${host}/question/tutor_qns_api`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){

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

tutor_questions();

function refresh_questions(){
    tutor_questions();
}

function tutor_submissions(){
    fetch(`http://${host}/sitting/submitted_to_tutor`,{
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then (response =>response.json())
        .then (function (json){
            let html_output = []

            json.forEach(
                function (current_submission, count_number){
                    html_output.push(
                        `<tr>
                                    <td>${count_number + 1}</td>
                                    <td>${current_submission.participant_registration_number}</td>
                                    <td>${current_submission.assessment_title}</td>
                                    <td>${current_submission.date_submitted}</td>
                                    <td>${current_submission.time_submitted}</td>
                                    <td>
                                        <div class="btn-group">
                                            <a href="detail/${current_submission.id}" class="btn btn-success btn-sm">Details</a>
                                        </div>
                                    </td>
                                </tr>`
                    )
                });
            submission_container.innerHTML = html_output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

function refresh_submission_list(){
    tutor_submissions();
}

tutor_submissions();



