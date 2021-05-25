let submissions = document.getElementById('submission_length');
let assessment = document.getElementById('assessment_count');

let appointment_count = document.getElementById('appointment_count');
let courses = document.getElementById('courses_count');
let students = document.getElementById('student_count');
let late_submissions = document.getElementById('late_submission');
let all_submissions = document.getElementById('all_submission');
let inactive = document.getElementById('inactive');

function submission_length(){
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
            submissions.innerHTML = html_output.join('');
        })
        .catch(err => console.log('Request Failed', err));
}

function assessment_count(){
    fetch(`http://${host}/assessment/listing`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )
            assessment.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function in_active_assessment(){
    fetch(`http://${host}/assessment/listing`, {
        method: 'GET',
        headers: {"Content-type": "application/json; charset=UTF-8"},
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

            inactive.innerHTML = html_output.join('')
        })
        .catch(err => console.log('Request Failed', err))
}

function courses_count(){
    fetch(`http://${host}/appointment/api/tutor`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            let html_output = []
            html_output.push(
                `${json.length}`
            )

            courses.innerHTML = html_output.join('')
            appointment_count.innerHTML = html_output.join('') + " " + "Courses"
        })
        .catch(err => console.log('Request Failed', err))
}

function enrollments(course_id){
    fetch(`http://${host}/enrollment/api/students/${course_id}`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(
            function (json){
            console.log(course_id)
            console.log(json.length)
            return json.length
        })
        .catch(err => console.log('Request Failed', err))
}

function student_count(){
    fetch(`http://${host}/appointment/api/tutor`, {
        method:"GET",
        headers:{"Content-type": "application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){
            var output = []

            json.forEach(
                function (current_appointment){
                    console.log(current_appointment.course_id)
                    let a = current_appointment.course_id
                    let int_a = parseInt(a)
                    output.push(enrollments(int_a))
                }
            )

            students.innerHTML = output.join('')
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
                            <td class="card-title font-weight-bolder">${current_submission.participant_registration_number}</td>
                            <td class="card-title font-weight-bolder">${current_submission.assessment_title}</td>
                            <td>${current_submission.date_submitted}</td>
                            <td>${current_submission.time_submitted}</td>
                            <td><a href="/sitting/detail/${current_submission.id}" class="btn btn-success">View</a></td>
                        </tr>`
                    )
                }
            )
            all_submissions.innerHTML = html_output.join('')
        })
        .catch(err => console.log("Request Failed", err))
}


function late_submission() {
    fetch(`http://${host}/sitting/late_submission`,{
        method:"GET",
        headers:{"Content-type":"application/json; charset=UTF-8"},
    })
        .then(response => response.json())
        .then(function (json){

            var html_output = [];

            json.forEach(
                function (current_submission){
                    html_output.push(
                        `<tr>
                            <td class="card-title font-weight-bolder">${current_submission.participant_registration_number}</td>
                            <td class="card-title font-weight-bolder">${current_submission.assessment_title }</td>
                            <td>${current_submission.date_submitted}</td>
                            <td>${current_submission.time_submitted}</td>
                            <td><a href="/sitting/detail/${current_submission.id}" class="btn btn-success">View</a></td>
                        </tr>`
                    )
                }
            )
            late_submissions.innerHTML = html_output.join('')
        })
        .catch(err => console.log("Request Failed", err))

}

submission();
submission_length();
in_active_assessment();
assessment_count();
courses_count();
late_submission();
student_count();