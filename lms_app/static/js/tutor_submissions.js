let submission_container = document.getElementById('submission_body');
function tutor_submissions(){
    fetch(`http://${host}/sitting/submissions`,{
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
                })
            submission_container.innerHTML = html_output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

function refresh_submission_list(){
    tutor_submissions();
}

tutor_submissions();