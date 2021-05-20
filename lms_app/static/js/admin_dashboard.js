let students_counts = document.getElementById('student_counts');
let student_list_body = document.getElementById('student_list_body');
let tutors_counts = document.getElementById('tutor_counts');
let tutor_list_body = document.getElementById('tutor_list_body');
let courses_counts = document.getElementById('course_counts');
let assessments_counts = document.getElementById('assessment_counts');
let assessment_list_body = document.getElementById('assessment_list_body');
let sitting_list_body = document.getElementById('sitting_list_tbody');
let question_list_body = document.getElementById('question_list_body');
let particular_question_list_body = document.getElementById('particular_question_list_body');
let appointments_identifier = document.getElementById('appointment_identifier');
let inactive_assessment_for_admin = document.getElementById('inactive_assessment_for_admin')

let path_name = window.location.pathname
let res = path_name.split("/")
let last_item = res[res.length - 1]
console.log(last_item)


function student_head_count(){
    fetch(`http://${host}/student/api/list`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            html_output.push(
                `${json.length}`
            )
            students_counts.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function student_listing(){
    fetch(`http://${host}/student/api/list`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_student, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_student.first_name} ${current_student.last_name}</td>
                            <td>${current_student.email}</td>
                            <td>${current_student.registration_number}</td>
                            <td><a href="/student/details/${current_student.id}" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            student_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}


function tutor_head_count(){
    fetch(`http://${host}/tutor/api/list`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            html_output.push(
                `${json.length}`
            )
            tutors_counts.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function tutor_listing(){
    fetch(`http://${host}/tutor/api/list`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_tutor, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_tutor.first_name} ${current_tutor.last_name}</td>
                            <td>${current_tutor.email}</td>
                            <td>${current_tutor.registration_number}</td>
                            <td><a href="/tutor/details/${current_tutor.id}" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            tutor_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}


function course_count(){
    fetch(`http://${host}/course/api/list`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            html_output.push(
                `${json.length}`
            )
            courses_counts.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function assessment_count(){
    fetch(`http://${host}/assessment/listing`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            html_output.push(
                `${json.length}`
            )
            assessments_counts.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function assessment_listing(){
    fetch(`http://${host}/assessment/listing`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_assessment, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_assessment.assessment_title}</td>
                            <td>${current_assessment.course_title}</td>
                            <td>${current_assessment.date_due}</td>
                            <td>${current_assessment.time_due}</td>
                            <td><a href="/assessment/detail/${current_assessment.id}" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            assessment_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}


function appointments(){
    fetch(`http://${host}/appointment/api/appointment`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            json.forEach(
                function (current_appointment){
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_appointment.tutors_reg}</td>
                            <td>${current_appointment.course_title}</td>
                            <td>${current_appointment.date_appointed}</td>
                            <td><a href="/appointment/appoint" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            appointments_identifier.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function inactive_assessments(){
    fetch(`http://${host}/assessment/listing`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = [];
            json.forEach(
                function (current_assessment){
                    if (current_assessment.status == false){
                        html_output.push(
                            `<tr>
                                <td class="card-title font-weight-bolder">${current_assessment.assessment_title}</td>
                                <td>${current_assessment.date_due}</td>
                                <td>${current_assessment.time_due}</td>
                                <td><a href="/assessment/detail/${current_assessment.id}" class="btn btn-success">View</a></td>
                            </tr>
                            `
                        )
                    }
                })

            inactive_assessment_for_admin.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function submission_listing(){
    fetch(`http://${host}/sitting/submissions`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_submission, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_submission.participant_registration_number}</td>
                            <td>${current_submission.assessment_course}</td>
                            <td>${current_submission.assessment_title}</td>
                            <td>${current_submission.date_submitted}</td>
                            <td>${current_submission.time_submitted}</td>
                            <td><a href="/sitting/detail/${current_submission.id}" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            sitting_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function question_listing(){
    fetch(`http://${host}/question/tutor_qns_api`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_question, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_question.question_title}</td>
                            <td>${current_question.question_content}</td>
                            <td>${current_question.assigned_mark}</td>
                            <td><a href="/question/details/${current_question.id}" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            question_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}

function particular_question_listing(){
    fetch(`http://${host}/question/qns_api/${last_item}`, {
        method: "GET",
        headers: {"Context-type": "application/json; charset=UTF-8"}
    })
        .then(response => response.json())
        .then(function (json) {
            let html_output = [];
            json.forEach(
                function (current_question, current_position) {
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_position + 1}</td>
                            <td class="card-title font-weight-bolder">${current_question.question_title}</td>
                            <td>${current_question.question_content}</td>
                            <td>${current_question.assigned_mark}</td>
                            <td><a href="#" class="btn btn-success">View</a></td>
                        </tr>
                        `
                    )
                })
            particular_question_list_body.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err));
}




student_head_count();
student_listing();
tutor_head_count();
tutor_listing();
course_count();
assessment_count();
assessment_listing();
appointments();
inactive_assessments();
submission_listing();
question_listing();
particular_question_listing();