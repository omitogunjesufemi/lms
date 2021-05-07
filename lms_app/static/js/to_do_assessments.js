let pending_to_do_lists = document.getElementById('pending_to_do_list');
let turned_in_to_do_list = document.getElementById('turned_in_to_do_list');

function pending_to_do_list(){
    fetch(`http://${host}/assessment/listing`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []

            json.forEach(
                function (current_assessment){
                    if ((current_assessment.sitting == null) && (current_assessment.status == true)){
                        html_output.push(
                            `<div class="card">
                                    <div class="card-header">
                                        <h2 class="font-weight-bolder">${current_assessment.course_title}</h2>

                                    </div>
                                    <div class="card-body">
                                        <h4 class="card-title">${ current_assessment.assessment_title }</h4>
                                        <p class="card-category font-weight-bolder">
                                            Due: ${ current_assessment.date_due } | ${ current_assessment.time_due }
                                        </p>

                                    </div>
                                    <div class="card-footer">
                                        <div class="stats">
                                            <i class="material-icons">access_time</i>
                                            Uploaded:
                                        </div>
                                        <a href="/sitting/new_sitting/${current_assessment.id}" class="btn btn-success">Take Test</a>
                                    </div>
                                </div>
                            `
                        )
                    }
                }
            )
            pending_to_do_lists.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request failed', err))
}

function turned_in_to_do(){
    fetch(`http://${host}/sitting/submissions`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = []

            json.forEach(
                function (current_submission){
                   html_output.push(
                        `<div class="card">
                            <div class="card-header">
                                <h2 class="font-weight-bolder">${ current_submission.assessment_course }</h2>

                            </div>
                            <div class="card-body">
                                <h4 class="card-title">${ current_submission.assessment_title }</h4>
                                <p class="card-category font-weight-bolder">
                                    Submitted: ${ current_submission.date_submitted } | ${ current_submission.time_submitted }
                                </p>

                            </div>
                            <div class="card-footer">
                                <div class="stats">
                                    <i class="material-icons">access_time</i>
                                    Submitted
                                </div>
                                <a href="/sitting/detail/${current_submission.id}" class="btn btn-success">View</a>
                            </div>
                        </div>
                        `
                   )
                }
            )
            turned_in_to_do_list.innerHTML = html_output.join('')
        }
        )
        .catch(err => console.log('Request failed', err))
    }

pending_to_do_list();
turned_in_to_do();