let submissions_length = document.getElementById('student_submission_length');
let assessment_length = document.getElementById('student_assessment_length');
let pending_assessment_length = document.getElementById('student_pending_assessment_length');
let pending_assessment = document.getElementById('student_pending_assessment');
let courses_length = document.getElementById('student_courses_length');
let courses_length_1 = document.getElementById('student_courses_length_1');
let all_assessment = document.getElementById('all_assessments');
let all_submission = document.getElementById('all_submission');

function student_submission_length(){
    fetch(`http://${host}/sitting/submissions`,{
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then (response =>response.json())
        .then (function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )

            submissions_length.innerHTML = html_output.join('');
            return html_output.indexOf(0)
        })
        .catch(err => console.log('Request Failed', err));
}

function assessment_count(){
    fetch(`http://${host}/assessment/active`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            assessment_length.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function pending_length (){
    fetch(`http://${host}/assessment/listing`, {
        method: "GET",
        headers: {"Content-type":"application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let output = [];
            let html_output = [];
            json.forEach(
                function (current_assessment){
                    if ((current_assessment.sitting == null) && (current_assessment.status == true)){
                        html_output.push(current_assessment)
                    }
                }
            )
            let output_length = html_output.length
            output.push(output_length)
            pending_assessment_length.innerHTML = output.join('')
        })
}

function pending_assessments(){
    fetch(`http://${host}/assessment/listing`, {
        method: 'GET',
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];

            json.forEach(
                function (current_assessment){
                    if ((current_assessment.sitting == null) && (current_assessment.status == true)){
                        html_output.push(
                            `<tr>
                                <td class="card-title font-weight-bolder">${current_assessment.course_title}</td>
                                <td class="card-title font-weight-bolder">${current_assessment.assessment_title}</td>
                                <td>${current_assessment.date_due}</td>
                                <td>${current_assessment.time_due}</td>
                                <td><a href="/sitting/new_sitting/${current_assessment.id}" class="btn btn-success">Do It!</a></td>
                            </tr>
                            `
                        )
                    }
                })

            pending_assessment.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function courses_count(){
    fetch(`http://${host}/enrollment/total`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            courses_length.innerHTML = html_output.join('')
            courses_length_1.innerHTML = html_output.join('') + " " + 'Courses'
        })
        .catch(err => console.log('Request Failed', err))
}

function submission() {
    fetch(`http://${host}/sitting/submissions`, {
        method: "GET",
        headers: {"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = []

            json.forEach(
                function (current_submission) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_submission.assessment_course}</td>
                            <td class="card-title font-weight-bolder">${current_submission.assessment_title}</td>
                            <td>${current_submission.date_submitted}</td>
                            <td>${current_submission.time_submitted}</td>
                            <td><a href="/sitting/detail/${current_submission.id}" class="btn btn-success">View</a></td>
                        </tr>`
                    )
                }
            )
            all_submission.innerHTML = html_output.join('')
        })
        .catch(err => console.log("Request Failed", err))
}


function all_assessments() {
    fetch(`http://${host}/assessment/listing`,{
        method:"GET",
        headers:{"Content-type":"application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){

            var html_output = [];

            json.forEach(
                function (current_assessment){
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_assessment.course_title}</td>
                            <td class="card-title font-weight-bolder">${current_assessment.assessment_title }</td>
                            <td>${current_assessment.date_due}</td>
                            <td>${current_assessment.time_due}</td>
                            <td><a href="/sitting/detail/${current_assessment.sitting}" class="btn btn-success">View</a></td>
                        </tr>`
                    )
                }
            )
            all_assessment.innerHTML = html_output.join('')
        })
        .catch(err => console.log("Request Failed", err))

}

student_submission_length();
assessment_count();
submission();
courses_count();
pending_length();
pending_assessments();
all_assessments();
