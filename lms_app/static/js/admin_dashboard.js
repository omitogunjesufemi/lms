let students_counts = document.getElementById('student_counts');
let tutors_counts = document.getElementById('tutor_counts');
let courses_counts = document.getElementById('course_counts');
let assessments_counts = document.getElementById('assessment_counts');


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


student_head_count();
tutor_head_count();
course_count();
assessment_count();